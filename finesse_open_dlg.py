# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finesse_open_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FinesseOpenDialog(object):
    def setupUi(self, FinesseOpenDialog):
        FinesseOpenDialog.setObjectName("FinesseOpenDialog")
        FinesseOpenDialog.resize(641, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FinesseOpenDialog.sizePolicy().hasHeightForWidth())
        FinesseOpenDialog.setSizePolicy(sizePolicy)
        FinesseOpenDialog.setMinimumSize(QtCore.QSize(641, 560))
        FinesseOpenDialog.setMaximumSize(QtCore.QSize(641, 560))
        self.buttonBox = QtWidgets.QDialogButtonBox(FinesseOpenDialog)
        self.buttonBox.setGeometry(QtCore.QRect(550, 10, 81, 541))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.buttonBox.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.resume_list = QtWidgets.QListWidget(FinesseOpenDialog)
        self.resume_list.setGeometry(QtCore.QRect(10, 10, 531, 541))
        self.resume_list.setObjectName("resume_list")

        self.retranslateUi(FinesseOpenDialog)
        self.buttonBox.accepted.connect(FinesseOpenDialog.accept)
        self.buttonBox.rejected.connect(FinesseOpenDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FinesseOpenDialog)

    def retranslateUi(self, FinesseOpenDialog):
        _translate = QtCore.QCoreApplication.translate
        FinesseOpenDialog.setWindowTitle(_translate("FinesseOpenDialog", "Open Resume"))

