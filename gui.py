import os, sys, string, inspect
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from db import *

# Dialog Windows
finesse_open_dialog = uic.loadUiType("finesse_open_dialog.ui")[0]
finesse_dialog = uic.loadUiType("finesse_dialog.ui")[0]
current_resume = ""

class FinesseOpenDialog(QtWidgets.QDialog, finesse_open_dialog):
   """ Open Resume Dialog Box """
   def __init__(self, resume_list, parent=None):
      QtWidgets.QDialog.__init__(self, parent)
      self.setupUi(self)
      self.resume_list = self.findChild(QtWidgets.QListWidget, 'resume_list')
      self.button_box = self.findChild(QtWidgets.QDialogButtonBox, 'resume_button_box')
      self.button_box.accepted.connect(self.open)
      for resume in resume_list:
         widgetItem = QtWidgets.QListWidgetItem(resume)
         self.resume_list.addItem(widgetItem)
         self.resume_list.setCurrentItem(widgetItem)
   
   def open(self):
      """ Open Resume """
      current_resume = self.resume_list.currentItem().text()
      self.resume_id = get_id(current_resume)

class FinesseDialog(QtWidgets.QDialog, finesse_dialog):
   """ Experience/Education Dialog Box """
   def __init__(self, resume_id, section, parent=None):
      QtWidgets.QDialog.__init__(self, parent)
      self.setupUi(self)
      self.resume_id = resume_id
      self.section = section
      self.setWindowTitle(section.capitalize())
      self.title = self.findChild(QtWidgets.QTextEdit, 'title')
      self.institution = self.findChild(QtWidgets.QTextEdit, 'institution')
      self.add_section = self.findChild(QtWidgets.QPushButton, 'add_section')
      self.add_section.clicked.connect(self.addSection)
      self.remove_section = self.findChild(QtWidgets.QPushButton, 'remove_section')
      self.remove_section.clicked.connect(self.removeSection)
      self.start_date = self.findChild(QtWidgets.QDateEdit, 'start_date')
      self.details_textedit = self.findChild(QtWidgets.QTextEdit, 'details_textedit')
      self.end_date = self.findChild(QtWidgets.QDateEdit, 'end_date')
      self.section_details = self.findChild(QtWidgets.QListWidget, 'section_details')
      self.save_detail = self.findChild(QtWidgets.QPushButton, 'save_detail')
      self.save_detail.clicked.connect(self.addDetail)
      self.remove_detail = self.findChild(QtWidgets.QPushButton, 'remove_detail')
      self.remove_detail.clicked.connect(self.removeDetail)
      self.section_list = self.findChild(QtWidgets.QTableWidget, 'section_list')
      subsections = get_job_experience(resume_id) if self.section == 'experience' else get_education(resume_id)
      for subsection in subsections:
         self.section_list.setRowCount(self.section_list.rowCount() + 1)
         self.section_list.setItem(self.section_list.rowCount() - 1, 0, subsection[0])
         self.section_list.setItem(self.section_list.rowCount() - 1, 1, subsection[1])
         self.section_list.setItem(self.section_list.rowCount() - 1, 2, subsection[2])
         self.section_list.setItem(self.section_list.rowCount() - 1, 3, subsection[3])
      
      self.dlgButtonBox = self.findChild(QtWidgets.QDialogButtonBox, 'dialog_button_box')
      self.dlgButtonBox.accepted.connect(self.saveSection)

   def saveSection(self):
      xml = "<Education></Education>" if self.section == 'education' else "<Experience></Experience>"
      root = ET.fromstring(xml)
      for i in range(0, self.section_list.rowCount()):
         # details = []
         # for i in range(self.section_details.count()):
         #    details.append(self.section_details.item(i).text())
         
         tag_name = 'Ed' if self.section == 'education' else 'Job'
         main_tag = ET.SubElement(ET.Element(tag_name), tag_name)
         title_tag = ET.SubElement(ET.Element('Title'), 'Title')
         title_tag.text = self.section_list.model().index(i, 0).data()
         institution_tag = ET.SubElement(ET.Element('Institution'), 'Institution')
         institution_tag.text = self.section_list.model().index(i, 1).data()
         start_date_tag = ET.SubElement(ET.Element('StartDate'), 'StartDate')
         start_date_tag.text = self.section_list.model().index(i, 2).data()
         end_date_tag = ET.SubElement(ET.Element('EndDate'), 'EndDate')
         end_date_tag.text = self.section_list.model().index(i, 3).data()
         main_tag.insert(0, end_date_tag)
         main_tag.insert(0, start_date_tag)
         main_tag.insert(0, institution_tag)
         main_tag.insert(0, title_tag)
         root.insert(1, main_tag)
      
      query("UPDATE Resume SET {} = '{}' WHERE ID = {}".format(self.section.capitalize(), ET.tostring(root).decode('utf-8'), self.resume_id))
   
   def addDetail(self):
      """ Add detail to 'section_details' ListView """
      if self.details_textedit.toPlainText() != "":
         newWidgetItem = QtWidgets.QListWidgetItem(self.details_textedit.toPlainText())
         self.section_details.addItem(newWidgetItem)
         self.details_textedit.setPlainText("")

   def removeDetail(self):
      """ Remove detail from 'section_details' ListView """
      # Check if any are selected
      if self.section_details.currentItem() != None:
         # If so, remove the selected item
         self.section_details.takeItem(self.section_details.currentRow())
   
   def addSection(self):
      if self.title.toPlainText() != "" and self.institution.toPlainText() != "":
         self.section_list.setRowCount(self.section_list.rowCount() + 1)
         self.section_list.setItem(self.section_list.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(self.title.toPlainText()))
         self.section_list.setItem(self.section_list.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(self.institution.toPlainText()))
         self.section_list.setItem(self.section_list.rowCount() - 1, 2, QtWidgets.QTableWidgetItem(self.start_date.date().toString("dd/MM/yyyy")))
         self.section_list.setItem(self.section_list.rowCount() - 1, 3, QtWidgets.QTableWidgetItem(self.end_date.date().toString("dd/MM/yyyy")))
         self.title.setPlainText("")
         self.institution.setPlainText("")

   def removeSection(self):
      if self.section_list.currentRow() != None:
         self.section_list.removeRow(self.section_list.currentRow())

class Finesse(QtWidgets.QMainWindow):
   """ Finesse Application MainWindow """
   def __init__(self):
      super(Finesse, self).__init__()
      uic.loadUi('finesse.ui', self)

      # Find all the fields....
      self.resume_title = self.findChild(QtWidgets.QTextEdit, 'resume_title')
      self.resume_address = self.findChild(QtWidgets.QTextEdit, 'resume_address')
      self.resume_phone_number = self.findChild(QtWidgets.QTextEdit, 'resume_phone_number')
      self.resume_email = self.findChild(QtWidgets.QTextEdit, 'resume_email')
      self.resume_profile = self.findChild(QtWidgets.QTextEdit, 'resume_profile')
      self.areas_of_expertise = self.findChild(QtWidgets.QListWidget, 'areas_of_expertise')
      self.resume_area = self.findChild(QtWidgets.QTextEdit, 'resume_area')
      
      # Find the controls....
      self.save_expertise = self.findChild(QtWidgets.QPushButton, 'save_expertise')
      self.save_expertise.clicked.connect(self.saveExpertise)
      self.remove_expertise = self.findChild(QtWidgets.QPushButton, 'remove_expertise')
      self.remove_expertise.clicked.connect(self.removeExpertise)

      # Top Bar Menu....
      self.finesse_menu_bar = self.findChild(QtWidgets.QMenuBar, 'finesse_menu_bar')
      self.open_resume = self.findChild(QtWidgets.QAction, 'actionOpen')
      self.open_resume.triggered.connect(self.openResume)
      self.new_resume = self.findChild(QtWidgets.QAction, 'actionNew')
      self.new_resume.triggered.connect(self.newResume)
      self.save_resume = self.findChild(QtWidgets.QAction, 'actionSave')
      self.save_resume.triggered.connect(self.saveResume)
      self.view_resume_pdf = self.findChild(QtWidgets.QAction, 'actionView_PDF')
      self.view_resume_pdf.triggered.connect(self.viewResumePDF)
      self.modify_experience = self.findChild(QtWidgets.QAction, 'actionModify_Experience')
      self.modify_experience.triggered.connect(lambda: self.openFinesseDialog('experience'))
      self.modify_education = self.findChild(QtWidgets.QAction, 'actionModify_Education')
      self.modify_education.triggered.connect(lambda: self.openFinesseDialog('education'))
      self.red_gold_theme = self.findChild(QtWidgets.QAction, 'actionRed_and_Gold')
      self.red_gold_theme.triggered.connect(self.switchTheme)
      self.blue_green_theme = self.findChild(QtWidgets.QAction, 'actionBlue_and_Green')
      self.blue_green_theme.triggered.connect(self.switchTheme)
      self.red_blue_theme = self.findChild(QtWidgets.QAction, 'actionRed_and_Blue')
      self.red_blue_theme.triggered.connect(self.switchTheme)
      self.blue_gold_theme = self.findChild(QtWidgets.QAction, 'actionBlue_and_Gold')
      self.blue_gold_theme.triggered.connect(self.switchTheme)

      self.show()
   
   def switchTheme(self):
      """ Switch Resume Color Theme """
      print(inspect.stack()[1][3])
   
   def openResume(self):
      """ Open Resume Dialog """
      resumes = get_all_names()
      dlg = FinesseOpenDialog(resumes)
      dlg.exec_()
      if hasattr(dlg, 'resume_id') == True:
         self.current_resume_id = dlg.resume_id[0]
         current_resume = get_resume(get_name(self.current_resume_id))
         self.resume_title.setPlainText(current_resume[1])
         self.resume_address.setPlainText(current_resume[2])
         self.resume_phone_number.setPlainText(current_resume[3])
         self.resume_email.setPlainText(current_resume[7])
         self.resume_profile.setPlainText(current_resume[8])
         self.areas_of_expertise.clear()
         for expertise in get_areas_of_expertise(current_resume[0]):
            widgetItem = QtWidgets.QListWidgetItem(expertise)
            self.areas_of_expertise.addItem(widgetItem)
            self.areas_of_expertise.setCurrentItem(widgetItem)
   
   def newResume(self):
      """ New Resume """
      pass

   def saveResume(self):
      """ Save Resume """
      expertises = []
      for i in range(self.areas_of_expertise.count()):
         expertises.append(self.areas_of_expertise.item(i).text())
      
      save_resume(self.current_resume_id, self.resume_title.toPlainText(), self.resume_address.toPlainText(), self.resume_profile.toPlainText(), self.resume_phone_number.toPlainText(), self.resume_email.toPlainText(), expertises)

   def viewResumePDF(self):
      """ View Resume PDF """
      pass

   def openFinesseDialog(self, section):
      """ Open Finesse Dialog """
      dlg = FinesseDialog(self.current_resume_id, section)
      dlg.exec_()

   def saveExpertise(self):
      """ Add expertise to 'areas_of_expertise' ListView and save to database """
      if self.resume_area.toPlainText() != "":
         newWidgetItem = QtWidgets.QListWidgetItem(self.resume_area.toPlainText())
         self.areas_of_expertise.addItem(newWidgetItem)
         self.resume_area.setPlainText("")


   def removeExpertise(self):
      """ Remove expertise from 'areas_of_expertise' ListView and remove from database """
      # Check if any are selected
      if self.areas_of_expertise.currentItem() != None:
         # If so, remove the selected item
         self.areas_of_expertise.takeItem(self.areas_of_expertise.currentRow())

app = QtWidgets.QApplication(sys.argv)
window = Finesse()
app.exec_()