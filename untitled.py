# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.referenceImages.setGeometry(QtCore.QRect(110, 0, 191, 191))
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
        self.referenceImageFrame.setStyleSheet("")
        self.referenceImageFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.referenceImageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.referenceImageFrame.setLineWidth(8)
        self.referenceImageFrame.setObjectName("referenceImageFrame")
        self.verticalLayout_2.addWidget(self.referenceImageFrame)
        self.rangeTypes = QtWidgets.QGroupBox(self.va30)
        self.rangeTypes.setGeometry(QtCore.QRect(0, 190, 391, 611))
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
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 371, 231))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet("background-color: rgb(13,13,13);\n"
"color: rgb(128,128,128);\n"
"\n"
"\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(29)
        self.tableWidget.setColumnCount(58)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(31, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(32, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(33, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(34, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(35, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(36, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(37, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(38, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(39, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(40, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(41, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(42, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(43, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(44, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(45, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(46, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(47, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(48, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(49, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(50, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(51, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(52, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(53, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(54, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(55, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(56, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(57, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(253, 253, 253))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.rangeTypes)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 300, 371, 231))
        self.tableWidget_2.setAutoFillBackground(True)
        self.tableWidget_2.setStyleSheet("background-color: rgb(13,13,13);\n"
"color: rgb(128,128,128);\n"
"\n"
"\n"
"")
        self.tableWidget_2.setAlternatingRowColors(False)
        self.tableWidget_2.setRowCount(7)
        self.tableWidget_2.setColumnCount(10)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(62, 97, 60))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tableWidget_2.setItem(0, 0, item)
        self.bottomFrame.addTab(self.va30, "")
        self.vb10 = QtWidgets.QWidget()
        self.vb10.setObjectName("vb10")
        self.bottomFrame.addTab(self.vb10, "")
        self.vb20 = QtWidgets.QWidget()
        self.vb20.setObjectName("vb20")
        self.bottomFrame.addTab(self.vb20, "")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(430, 10, 671, 891))
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
        self.btn2.setText(_translate("Dialog", "Load Dicom"))
        self.btnR.setText(_translate("Dialog", "Save Annotation"))
        self.btnC.setText(_translate("Dialog", "Refresh"))
        self.browse.setText(_translate("Dialog", "Browse.."))
        self.voiceControl.setText(_translate("Dialog", "Voice Control"))
        self.original.setText(_translate("Dialog", "Original"))
        self.btnS.setText(_translate("Dialog", "S"))
        self.aligned.setText(_translate("Dialog", "Aligned"))
        self.referenceImages.setTitle(_translate("Dialog", "Reference Images"))
        self.referenceImageFrame.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.rangeTypes.setTitle(_translate("Dialog", "Range Types"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Volume_Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "DicomPath"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Series"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "SeriesDescription"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "PatientsName"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "PatientsAge"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "PatientsSex"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "Modality"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "BodyPartExamined"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "Manufacturer"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "ProtocolName"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Dialog", "StudyDescription"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Dialog", "StudyInstanceUID"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Dialog", "FrameOfReferenceUID"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Dialog", "RequestedProcedureDescription"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Dialog", "PixelSpacing"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Dialog", "ImageOrientationPatient"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("Dialog", "PatientPosition"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("Dialog", "SliceThickness"))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("Dialog", "ConvolutionKernel"))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("Dialog", "PhotometricInterpretation"))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("Dialog", "WindowCenter"))
        item = self.tableWidget.horizontalHeaderItem(22)
        item.setText(_translate("Dialog", "WindowWidth"))
        item = self.tableWidget.horizontalHeaderItem(23)
        item.setText(_translate("Dialog", "ImageType"))
        item = self.tableWidget.horizontalHeaderItem(24)
        item.setText(_translate("Dialog", "ImageComments"))
        item = self.tableWidget.horizontalHeaderItem(25)
        item.setText(_translate("Dialog", "NumOfSlices"))
        item = self.tableWidget.horizontalHeaderItem(26)
        item.setText(_translate("Dialog", "Width"))
        item = self.tableWidget.horizontalHeaderItem(27)
        item.setText(_translate("Dialog", "Height"))
        item = self.tableWidget.horizontalHeaderItem(28)
        item.setText(_translate("Dialog", "Depth"))
        item = self.tableWidget.horizontalHeaderItem(29)
        item.setText(_translate("Dialog", "x_min"))
        item = self.tableWidget.horizontalHeaderItem(30)
        item.setText(_translate("Dialog", "y_min"))
        item = self.tableWidget.horizontalHeaderItem(31)
        item.setText(_translate("Dialog", "z_min"))
        item = self.tableWidget.horizontalHeaderItem(32)
        item.setText(_translate("Dialog", "x_max"))
        item = self.tableWidget.horizontalHeaderItem(33)
        item.setText(_translate("Dialog", "y_max"))
        item = self.tableWidget.horizontalHeaderItem(34)
        item.setText(_translate("Dialog", "z_max"))
        item = self.tableWidget.horizontalHeaderItem(35)
        item.setText(_translate("Dialog", "origin_x"))
        item = self.tableWidget.horizontalHeaderItem(36)
        item.setText(_translate("Dialog", "origin_y"))
        item = self.tableWidget.horizontalHeaderItem(37)
        item.setText(_translate("Dialog", "origin_z"))
        item = self.tableWidget.horizontalHeaderItem(38)
        item.setText(_translate("Dialog", "space_x"))
        item = self.tableWidget.horizontalHeaderItem(39)
        item.setText(_translate("Dialog", "space_y"))
        item = self.tableWidget.horizontalHeaderItem(40)
        item.setText(_translate("Dialog", "space-z"))
        item = self.tableWidget.horizontalHeaderItem(41)
        item.setText(_translate("Dialog", "Orientation"))
        item = self.tableWidget.horizontalHeaderItem(42)
        item.setText(_translate("Dialog", "Box_str"))
        item = self.tableWidget.horizontalHeaderItem(43)
        item.setText(_translate("Dialog", "LastAccessed"))
        item = self.tableWidget.horizontalHeaderItem(44)
        item.setText(_translate("Dialog", "Comment"))
        item = self.tableWidget.horizontalHeaderItem(45)
        item.setText(_translate("Dialog", "MagneticFieldStrength"))
        item = self.tableWidget.horizontalHeaderItem(46)
        item.setText(_translate("Dialog", "Flip Angle"))
        item = self.tableWidget.horizontalHeaderItem(47)
        item.setText(_translate("Dialog", "RepetitionTime"))
        item = self.tableWidget.horizontalHeaderItem(48)
        item.setText(_translate("Dialog", "EchoTime"))
        item = self.tableWidget.horizontalHeaderItem(49)
        item.setText(_translate("Dialog", "Imaging Frequency"))
        item = self.tableWidget.horizontalHeaderItem(50)
        item.setText(_translate("Dialog", "EchoTrainLength"))
        item = self.tableWidget.horizontalHeaderItem(51)
        item.setText(_translate("Dialog", "SequenceName"))
        item = self.tableWidget.horizontalHeaderItem(52)
        item.setText(_translate("Dialog", "ImagedNucleus"))
        item = self.tableWidget.horizontalHeaderItem(53)
        item.setText(_translate("Dialog", "TransmitCoilName"))
        item = self.tableWidget.horizontalHeaderItem(54)
        item.setText(_translate("Dialog", "InversionTime"))
        item = self.tableWidget.horizontalHeaderItem(55)
        item.setText(_translate("Dialog", "ScanningSequence"))
        item = self.tableWidget.horizontalHeaderItem(56)
        item.setText(_translate("Dialog", "CoilList"))
        item = self.tableWidget.horizontalHeaderItem(57)
        item.setText(_translate("Dialog", "DicomFiles"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.tableWidget_2.setSortingEnabled(True)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "anno_id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "world-coordination"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "world_dimension"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "window_low"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "window_high"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "annotation_details"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Last_Accessed"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "patient_name"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "volume_id"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "dicom_path"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.bottomFrame.setTabText(self.bottomFrame.indexOf(self.va30), _translate("Dialog", "VA30"))
        self.bottomFrame.setTabText(self.bottomFrame.indexOf(self.vb10), _translate("Dialog", "VB10"))
        self.bottomFrame.setTabText(self.bottomFrame.indexOf(self.vb20), _translate("Dialog", "VB20"))

