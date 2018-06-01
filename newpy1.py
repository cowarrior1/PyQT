#! python2
import sys # We need sys so that we can pass argv to QApplication
import os
#PYTHONROOT = "C:/Users/z003x7ma/AppData/Local/Continuum/anaconda2"
#sys.path.append(PYTHONROOT)
PROGRAMROOT = "C:/Users/z003x7ma/source/repos/FlaskWebProject1/FlaskWebProject1/FlaskWebProject1/cad"
sys.path.append(PROGRAMROOT)
PLASMAROOT = PROGRAMROOT + "/Plasma"
ALPHAROOT = PROGRAMROOT + "/alpha"
sys.path.append(PLASMAROOT)
sys.path.append(ALPHAROOT)
sys.path.append(PLASMAROOT + "/bin_27")
#sys.path.append(PYTHONROOT)
sys.path.append(ALPHAROOT + "/bin")
sys.path.append(ALPHAROOT + "/extern/bin")
sys.path.append(PROGRAMROOT + "/Plasma/extern/bin")
sys.path.append(PROGRAMROOT + "/Plasma/extern/bin/python")
#sys.path.append(PYTHONROOT + "/lib")
sys.path.append(PLASMAROOT + "/scripts/python")
sys.path.append(PLASMAROOT + "/plugins/python27")
sys.path.append(ALPHAROOT + "/scripts/python")
sys.path.append(PROGRAMROOT + "/packages/PIL")
sys.path.append(PROGRAMROOT + "/packages")
#sys.path.append(PYTHONROOT + "/Lib/site-packages")
Path = PLASMAROOT + "/scripts/python/path.pyc"
sys.path.append(Path)
import path
import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import mysql.connector
from mysql.connector import errorcode
import json
import base64
import untitled
import dicom
import imagetools
import re
import pdb
import vpiv
import cad_utils
import plasmatools
import plasmatools
import vputils
try:
    import tools  #throws error because import path gets the path.pyc from python instead of path file from conda
except:
    import viewertools
    import ivtools
import dicomloader
import subprocess
import plasma
import time
import win32gui
import random
import string
import datetime
import time
import easygui

__metaclass__ = type

try:
    connection = mysql.connector.connect(user='admin',
                                         password= 'admin',
                                         host='127.0.0.1',
                                         port='3306',
                                         database = 'multivender_test')
    cursor = connection.cursor(buffered=True)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Wrong Username/password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    else:
        print(err)

class ExampleApp(QDialog):
    IMAGE_PATH = None
    windowlevel= []

    def __init__(self):
        # super allows us to
        # access variables, methods etc in the design.py file
        super(ExampleApp, self).__init__()
        self.ui = untitled.Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowState(Qt.WindowMaximized)
        self.ui.btn2.clicked.connect(self.loadDicomInfo)
        self.ui.tableWidget.cellDoubleClicked.connect(self.loadImage)
        self.ui.tableWidget_2.cellDoubleClicked.connect(self.showAnnotationImage)
        self.ui.btnR.clicked.connect(self.saveAnnotation)
        self.ui.btnC.clicked.connect(self.loadAnnotationInfo)
        self.show()

    def loadDicomInfo(self):
        query = ('select * from volume_dicominfo');
        tableWidget = self.ui.tableWidget
        self.loadData(query, tableWidget)

    def loadAnnotationInfo(self):
        loadquery = ('select * from windowlevel_annotation ORDER BY Last_Accessed');
        tableWidget = self.ui.tableWidget_2
        self.loadData(loadquery, tableWidget)

    def loadData(self, query, tableWidgetName):
        cursor.execute(query)
        result = cursor.fetchall()
        tableWidgetName.setRowCount(0)
        for row_number, row_data in enumerate(result):
            tableWidgetName.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                tableWidgetName.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def loadImage(self, row, column_number):
        global PATIENT_NAME #in unicode and need to change to json
        global VOLUME_ID
        #TODO only "Dicom Path" can be clicked.
        patientNameColumn = column_number + 3
        volumeIdColumn= column_number - 1
        PATIENT_NAME = self.ui.tableWidget.item(row, patientNameColumn).text()
        VOLUME_ID = self.ui.tableWidget.item(row, volumeIdColumn).text()
        self.IMAGE_PATH = self.ui.tableWidget.item(row, column_number).text()

        print ("CELL VALUE FROM LOAD IMAGE: ", self.IMAGE_PATH)
        plasma.die()
        plasma.start()
        viewertools.show(self.IMAGE_PATH)

    def saveAnnotation(self):
        try:
            ts = time.time()
            lastAccessed = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') #need to parse to str/date
            uid = ''.join(random.Random().sample(string.letters + string.digits, random.randint(10,20)))
            world_FovSize = float(float(vpiv.getfov(vpiv.currentimage()))) #size of ROI
            world_cord = cad_utils.floatlist(vpiv.currentworldcoordinateswithwindowid(vpiv.currentimage())) #world location #type is list
            world_cord_str = json.dumps(world_cord) #serialize to str
            window_low, window_high = cad_utils.floatlist(vpiv.getscalarwindow(plasmatools.allsids()[0]))
            b0= ivtools.getBookmarkedView() #complete details
            strb0 = ' '.join(b0)
            print "\nsave anns"
            print world_FovSize
            print world_cord_str
            print window_low, window_high
            print strb0
            insertQuery = """INSERT INTO windowlevel_annotation(anno_id, world_coordination, world_dimension, window_low, window_high, annotation_details, Last_Accessed, patient_name, volume_id, dicom_path) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
            cursor.execute(insertQuery,(uid, world_cord_str, world_FovSize, window_low, window_high, strb0, lastAccessed, PATIENT_NAME, VOLUME_ID, self.IMAGE_PATH ))
            connection.commit()
        except:
            easygui.msgbox('Try loading data first before saving.', 'Invalid Input')
            pass


    def showAnnotationImage(self, row, column_number):
        print ("Row: %d and Column is %d" %(row, column_number))
        print(self.ui.tableWidget_2.item(row, column_number).text())
        if not column_number == 5:
            temp_column_number = 5 - column_number #actual column_number
            annoDetailsColumn = temp_column_number + column_number #always 5
            windowHighColumn = annoDetailsColumn - 1
            windowLowColumn = annoDetailsColumn -2
            worldDimensionColumn = annoDetailsColumn - 3
            windowCoordColumn = annoDetailsColumn - 4
            dicomPathColumn = annoDetailsColumn + 4
        annoDetailsCell = self.ui.tableWidget_2.item(row, annoDetailsColumn).text()
        windowHighCell = self.ui.tableWidget_2.item(row, windowHighColumn).text()
        windowLowCell = self.ui.tableWidget_2.item(row,windowLowColumn).text()
        worldDimensionCell = self.ui.tableWidget_2.item(row,worldDimensionColumn).text()
        windowCoordCell = self.ui.tableWidget_2.item(row, windowCoordColumn).text() #type is unicode
        windowCoordCell = json.loads(windowCoordCell) #deserialize bytestream to object
        dicomPathCell = self.ui.tableWidget_2.item(row, dicomPathColumn).text()
        if self.IMAGE_PATH == None or self.IMAGE_PATH != dicomPathCell: #compare the column path with the path name
            IMAGE_PATH = dicomPathCell
            plasma.die()
            plasma.start()
            viewertools.show(IMAGE_PATH)
            vpiv.goto(windowCoordCell[0], windowCoordCell[1], windowCoordCell[2])
            vpiv.setfov(worldDimensionCell)
            try:
                vpiv.setscalarwindow(self.IMAGE_PATH, windowLowCell, windowHighCell, 1)
            except RuntimeError:
                pass
        else: 
            vpiv.goto(windowCoordCell[0], windowCoordCell[1], windowCoordCell[2])
            vpiv.setfov(worldDimensionCell)
            try:
                vpiv.setscalarwindow(self.IMAGE_PATH, windowLowCell, windowHighCell, 1)
            except RuntimeError:
                pass

def main():
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
    form.move(0,0)
    # import pdb
    # pdb.set_trace()
    form.show()                         # Show the form
    sys.exit(app.exec_())                      # and execute the app

if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
