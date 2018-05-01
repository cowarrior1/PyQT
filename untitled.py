#! python2

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
import mysql.connector


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1113, 908)
        Dialog.setStyleSheet("\n"
"background-color: black;")
        self.topFrame = QtWidgets.QFrame(Dialog)
        self.topFrame.setGeometry(QtCore.QRect(4, 9, 401, 141))
        self.topFrame.setAutoFillBackground(False)
        self.topFrame.setStyleSheet("\n"
"background-color:black\n"
"")
        self.topFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topFrame.setObjectName("topFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.topFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.btn1 = QtWidgets.QPushButton(self.topFrame)
        self.btn1.setStyleSheet("background-color: #b8cced")
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.topFrame)
        self.btn2.setStyleSheet("background-color: #b8cced")
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)
        self.btnR = QtWidgets.QPushButton(self.topFrame)
        self.btnR.setStyleSheet("background-color: #b8cced")
        self.btnR.setObjectName("btnR")
        self.gridLayout.addWidget(self.btnR, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.topFrame)
        self.lineEdit.setStyleSheet("background-color: white")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 3, 1, 1)
        self.btnC = QtWidgets.QPushButton(self.topFrame)
        self.btnC.setStyleSheet("background-color: #b8cced")
        self.btnC.setObjectName("btnC")
        self.gridLayout.addWidget(self.btnC, 1, 2, 2, 1)
        self.browse = QtWidgets.QPushButton(self.topFrame)
        self.browse.setStyleSheet("background-color: #b8cced")
        self.browse.setObjectName("browse")
        self.gridLayout.addWidget(self.browse, 1, 3, 1, 1)
        self.voiceControl = QtWidgets.QPushButton(self.topFrame)
        self.voiceControl.setStyleSheet("background-color: #b8cced")
        self.voiceControl.setObjectName("voiceControl")
        self.gridLayout.addWidget(self.voiceControl, 2, 0, 1, 1)
        self.original = QtWidgets.QRadioButton(self.topFrame)
        self.original.setStyleSheet("")
        self.original.setObjectName("original")
        self.gridLayout.addWidget(self.original, 2, 3, 1, 1)
        self.btnS = QtWidgets.QPushButton(self.topFrame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(184, 204, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 204, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 204, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 204, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 204, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 204, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 204, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 204, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 204, 237))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.btnS.setPalette(palette)
        self.btnS.setStyleSheet("background-color: #b8cced")
        self.btnS.setObjectName("btnS")
        self.gridLayout.addWidget(self.btnS, 3, 2, 1, 1)
        self.aligned = QtWidgets.QRadioButton(self.topFrame)
        self.aligned.setObjectName("aligned")
        self.gridLayout.addWidget(self.aligned, 3, 3, 1, 1)
        self.btn2.raise_()
        self.btn1.raise_()
        self.btnR.raise_()
        self.btnC.raise_()
        self.btnS.raise_()
        self.original.raise_()
        self.aligned.raise_()
        self.lineEdit.raise_()
        self.browse.raise_()
        self.voiceControl.raise_()
        self.bottomFrame = QtWidgets.QTabWidget(Dialog)
        self.bottomFrame.setGeometry(QtCore.QRect(-1, 129, 411, 900))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.bottomFrame.setFont(font)
        self.bottomFrame.setAutoFillBackground(False)
        self.bottomFrame.setStyleSheet("QTabWidget{\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.bottomFrame.setTabPosition(QtWidgets.QTabWidget.North)
        self.bottomFrame.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.bottomFrame.setIconSize(QtCore.QSize(16, 16))
        self.bottomFrame.setElideMode(QtCore.Qt.ElideNone)
        self.bottomFrame.setObjectName("bottomFrame")
        self.va30 = QtWidgets.QWidget()
        self.va30.setObjectName("va30")
        self.referenceImages = QtWidgets.QGroupBox(self.va30)
        self.referenceImages.setGeometry(QtCore.QRect(9, 9, 391, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.referenceImages.sizePolicy().hasHeightForWidth())
        self.referenceImages.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Siemens Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.referenceImages.setFont(font)
        self.referenceImages.setAutoFillBackground(False)
        self.referenceImages.setStyleSheet("QGroupBox{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QGroupBox::title{\n"
"    background-color: #374af2\n"
"\n"
"}\n"
"")
        self.referenceImages.setObjectName("referenceImages")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.referenceImages)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.referenceImageFrame = QtWidgets.QFrame(self.referenceImages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.referenceImageFrame.sizePolicy().hasHeightForWidth())
        self.referenceImageFrame.setSizePolicy(sizePolicy)
        self.referenceImageFrame.setStyleSheet("background-color: white\n"
"")
        self.referenceImageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.referenceImageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.referenceImageFrame.setObjectName("referenceImageFrame")
        self.verticalLayout_2.addWidget(self.referenceImageFrame)
        self.rangeTypes = QtWidgets.QGroupBox(self.va30)
        self.rangeTypes.setGeometry(QtCore.QRect(10, 260, 391, 895))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rangeTypes.sizePolicy().hasHeightForWidth())
        self.rangeTypes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Siemens Serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rangeTypes.setFont(font)
        self.rangeTypes.setStyleSheet("QGroupBox{\n"
"background-color: black;\n"
"color: white;\n"
"}\n"
"\n"
"\n"
"QGroupBox::title{\n"
"    background-color: #374af2\n"
"\n"
"}\n"
"")
        self.rangeTypes.setObjectName("rangeTypes")
        self.tableWidget = QtWidgets.QTableWidget(self.rangeTypes)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 351, 441))
        self.tableWidget.setRowCount(29)
        self.tableWidget.setColumnCount(59)
        self.tableWidget.setObjectName("tableWidget")
        self.referenceImages.raise_()
        self.rangeTypes.raise_()
        self.bottomFrame.addTab(self.va30, "")
        self.vb10 = QtWidgets.QWidget()
        self.vb10.setObjectName("vb10")
        self.bottomFrame.addTab(self.vb10, "")
        self.vb20 = QtWidgets.QWidget()
        self.vb20.setObjectName("vb20")
        self.bottomFrame.addTab(self.vb20, "")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(420, 10, 671, 891))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.retranslateUi(Dialog)
        self.bottomFrame.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn1.setText(_translate("Dialog", "1"))
        self.btn2.setText(_translate("Dialog", "2"))
        self.btnR.setText(_translate("Dialog", "R"))
        self.btnC.setText(_translate("Dialog", "C"))
        self.browse.setText(_translate("Dialog", "Browse.."))
        self.voiceControl.setText(_translate("Dialog", "Voice Control"))
        self.original.setText(_translate("Dialog", "Original"))
        self.btnS.setText(_translate("Dialog", "S"))
        self.aligned.setText(_translate("Dialog", "Aligned"))
        self.referenceImages.setTitle(_translate("Dialog", "Reference Images"))
        self.rangeTypes.setTitle(_translate("Dialog", "Range Types"))
        self.bottomFrame.setTabText(self.bottomFrame.indexOf(self.va30), _translate("Dialog", "VA30"))
        self.bottomFrame.setTabText(self.bottomFrame.indexOf(self.vb10), _translate("Dialog", "VB10"))
        self.bottomFrame.setTabText(self.bottomFrame.indexOf(self.vb20), _translate("Dialog", "VB20"))
