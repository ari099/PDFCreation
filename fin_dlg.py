# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finesse_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FinesseDialog(object):
    def setupUi(self, FinesseDialog):
        FinesseDialog.setObjectName("FinesseDialog")
        FinesseDialog.resize(747, 646)
        self.buttonBox = QtWidgets.QDialogButtonBox(FinesseDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 600, 731, 32))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.tableWidget = QtWidgets.QTableWidget(FinesseDialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 721, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.listView = QtWidgets.QListView(FinesseDialog)
        self.listView.setGeometry(QtCore.QRect(10, 380, 721, 211))
        self.listView.setObjectName("listView")
        self.label_5 = QtWidgets.QLabel(FinesseDialog)
        self.label_5.setGeometry(QtCore.QRect(10, 340, 721, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_5.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(FinesseDialog)
        self.buttonBox.accepted.connect(FinesseDialog.accept)
        self.buttonBox.rejected.connect(FinesseDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FinesseDialog)

    def retranslateUi(self, FinesseDialog):
        _translate = QtCore.QCoreApplication.translate
        FinesseDialog.setWindowTitle(_translate("FinesseDialog", "Dialog"))
        self.label_5.setText(_translate("FinesseDialog", "DETAILS"))

