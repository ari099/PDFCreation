import sqlite3
import ctypes
import xml.etree.ElementTree as ET
from PyQt5 import QtWidgets

def query(sql):
   """
   Query the Database

   Execute a query on the Finesse SQLite database

   Parameters:
   sql (string): SQL query text

   Returns:
   list: Query Results
   """
   # Connect to 'finesse.db'
   finesse = sqlite3.connect('.\\finesse.db')

   # Create database cursor for query execution....
   cursor = finesse.cursor()
   try:
      # Execute SQL Query....
      cursor.execute(sql)

      # Getting the SQL query results....
      results = cursor.fetchall()

      # Commit any new changes to the database....
      finesse.commit()

      # Return the results to function caller
      return results
   except sqlite3.Error as error:
      # Return any errors returned from the query....
      # app = QtWidgets.QApplication([])
      # error_dialog = QtWidgets.QErrorMessage()
      # error_dialog.showMessage("ERROR! {}".format(error.args[0]))
      # app.exec_()
      ctypes.windll.user32.MessageBoxW(0, "ERROR! {}".format(error.args[0]), "ERROR", 0)
      return []

def get_areas_of_expertise(resume_id):
   """
   Get areas of expertise

   Go through the Expertise XML for the resume associated with 'resume_id'

   Parameters:
   resume_id (int): Resume ID

   Returns:
   list: Expertise list
   """
   expertise_xml = query("SELECT Expertise FROM Resume WHERE ID = {}".format(resume_id))[0][0]
   root = ET.fromstring(expertise_xml)
   return [expertise.text for expertise in root]

def get_job_experience(resume_id):
   """
   Get experience

   Go through the Experience XML for the resume associated with 'resume_id'

   Parameters:
   resume_id (int): Resume ID

   Returns:
   list: Experience list
   """
   experience_xml = query("SELECT Experience FROM Resume WHERE ID = {}".format(resume_id))[0][0]
   root = ET.fromstring(experience_xml)
   acquireElement = lambda txt: list(root.iter(str(txt))) if len(list(root.iter(str(txt)))) > 0 else None
   eds = acquireElement('Job')
   results = []
   if eds != None:
      for ed in eds:
         row = [QtWidgets.QTableWidgetItem(t.text) for t in list(ed)]
         results.append(row)
      
   return results

def get_education(resume_id):
   """
   Get education

   Go through the Education XML for the resume associated with 'resume_id'

   Parameters:
   resume_id (int): Resume ID

   Returns:
   list: Education list
   """
   education_xml = query("SELECT Education FROM Resume WHERE ID = {}".format(resume_id))[0][0]
   root = ET.fromstring(education_xml)
   acquireElement = lambda txt: list(root.iter(str(txt))) if len(list(root.iter(str(txt)))) > 0 else None
   eds = acquireElement('Ed')
   results = []
   if eds != None:
      for ed in eds:
         row = [QtWidgets.QTableWidgetItem(t.text) for t in list(ed)]
         results.append(row)
      
   return results

def find_names(wildcard):
   """
   Find names by wildcard string

   Find the names that are like 'wildcard' in the database

   Parameters:
   wildcard (string): Search string

   Returns:
   list: List of names
   """
   names = query("SELECT FullName FROM Resume WHERE FullName LIKE '%{}%'".format(wildcard))
   return [name[0] for name in names]

def get_name(n):
   """
   Get name from database

   Find out if a name exists in the database

   Parameters:
   n (string): Search string

   Returns:
   list: List of names
   """
   name = query("SELECT FullName FROM Resume WHERE FullName = '{}'".format(n))
   return list(name[0]) if len(name) > 0 else []

def get_all_names():
   """Get every name from the database"""
   names = query("SELECT FullName FROM Resume")
   return [name[0] for name in names]

def find_resume(name):
   """
   Find resume by wildcard string

   Find the resumes associated with 'name' in the database

   Parameters:
   name (string): Search string

   Returns:
   list: List of resumes
   """
   resumes = query("SELECT * FROM Resume WHERE FullName LIKE '%{}%'".format(name))
   return [resume[0] for resume in resumes]

def get_resume(name):
   """
   Get resume by name

   Find the resumes associated with 'name' in the database

   Parameters:
   name (string): Search string

   Returns:
   list: List of resumes
   """
   resume = query("SELECT * FROM Resume WHERE FullName = '{}'".format(name))
   return list(resume[0]) if len(resume) > 0 else []

def get_id(name):
   """
   Get ID by name

   Find the ID associated with 'name' in the database

   Parameters:
   name (string): Search string

   Returns:
   list: List of resumes
   """
   resume_ids = query("SELECT ID FROM RESUME WHERE FullName LIKE '%{}%'".format(name))
   return [resume_id[0] for resume_id in resume_ids]

def get_name(resume_id):
   """
   Get name by ID

   Find the name associated with 'ID' in the database

   Parameters:
   id (int): Search string

   Returns:
   list: List of resumes
   """
   name = query("SELECT FullName FROM Resume WHERE ID = {}".format(resume_id))
   return name[0][0] if len(name) > 0 else []

def save_resume(resume_id, title, address, profile, phone, email, areas_of_expertise, experience, education):
   """
   Save current visible resume to database

   Save everything in form fields to the database for the current resume

   Parameters:
   resume_id (int): ID of Resume in database
   title (string): Resume Title (FullName)
   address (string): Resume Address Info (Address)
   phone (string): Resume Phone Number Info (Phone)
   experience (list): Resume Experience section info (Experience)
   education (list): Resume Education section info (Education)
   expertise (list): Resume Expertise section info (Expertise)
   email (string): Resume Email info (Email)
   profile (string): Resume profile (Profile)
   """ 
   expertise_xml = '<Expertises>{}</Expertises>'.format(''.join(['<Expertise>{}</Expertise>'.format(exp) for exp in areas_of_expertise]))
   experience_xml = str()
   sql = "UPDATE Resume SET FullName = {0}, Address = {1}, Phone = {2}, Expertise = {3}, Email = {4}, Profile = {5} WHERE ID = {6}".format(title, address, phone, expertise_xml, email, profile, resume_id)
   query(sql)

def save_resume(resume_id, title, address, profile, phone, email, areas_of_expertise):
   """
   Save current visible resume to database

   Save everything in form fields to the database for the current resume

   Parameters:
   resume_id (int): ID of Resume in database
   title (string): Resume Title (FullName)
   address (string): Resume Address Info (Address)
   phone (string): Resume Phone Number Info (Phone)
   expertise (list): Resume Expertise section info (Expertise)
   email (string): Resume Email info (Email)
   profile (string): Resume profile (Profile)
   """ 
   expertise_xml = '<Expertises>{}</Expertises>'.format(''.join(['<Expertise>{}</Expertise>'.format(exp) for exp in areas_of_expertise]))
   experience_xml = str()
   sql = "UPDATE Resume SET FullName = '{0}', Address = '{1}', Phone = '{2}', Expertise = '{3}', Email = '{4}', Profile = '{5}' WHERE ID = {6}".format(title, address, phone, expertise_xml, email, profile, resume_id)
   query(sql)
