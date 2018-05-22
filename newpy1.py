#! python2
import sys # We need sys so that we can pass argv to QApplication
import os
PYTHONROOT = "C:/Users/z003x7ma/AppData/Local/Continuum/anaconda2"
sys.path.append(PYTHONROOT)
PROGRAMROOT = "C:/Users/z003x7ma/source/repos/FlaskWebProject1/FlaskWebProject1/FlaskWebProject1/cad"
sys.path.append(PROGRAMROOT)
PLASMAROOT = PROGRAMROOT + "/Plasma"
ALPHAROOT = PROGRAMROOT + "/alpha"
sys.path.append(PLASMAROOT)
sys.path.append(ALPHAROOT)
sys.path.append(PLASMAROOT + "/bin_27")
sys.path.append(PYTHONROOT)
sys.path.append(ALPHAROOT + "/bin")
sys.path.append(ALPHAROOT + "/extern/bin")
sys.path.append(PROGRAMROOT + "/Plasma/extern/bin")
sys.path.append(PROGRAMROOT + "/Plasma/extern/bin/python")
sys.path.append(PYTHONROOT + "/lib")
sys.path.append(PLASMAROOT + "/scripts/python")
sys.path.append(PLASMAROOT + "/plugins/python27")
sys.path.append(ALPHAROOT + "/scripts/python")
sys.path.append(PROGRAMROOT + "/packages/PIL")
sys.path.append(PROGRAMROOT + "/packages")
import PyQt5.QtCore
import PyQt5.QtWidgets
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
import viewertools
import dicomloader
import subprocess
import plasma
import time
import win32gui
import ivtools
import random
import string
__metaclass__ = type

try:
    connection = mysql.connector.connect(user='admin',
                                         password= 'admin',
                                         host='127.0.0.1',
                                         port='3306',
                                         database = 'multivender_test')
    cursor = connection.cursor(buffered=True)

    # insertList(cursor)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Wrong Username/password')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    else:
        print(err)

class ExampleApp(QDialog):
    IMAGE = 0
    windowlevel= []


    def __init__(self):
        # super allows us to
        # access variables, methods etc in the design.py file
        super(ExampleApp, self).__init__()
        self.ui = untitled.Ui_Dialog()
        self.ui.setupUi(self) # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        self.setWindowState(Qt.WindowMaximized)
        self.ui.btn1.clicked.connect(self.insertList)
        self.ui.btn2.clicked.connect(self.loadDicomInfo)
        self.ui.tableWidget.cellDoubleClicked.connect(self.loadImage)
        self.ui.tableWidget_2.cellDoubleClicked.connect(self.showAnnotation)
        self.ui.btnR.clicked.connect(self.saveAnnotation)
        self.ui.btnC.clicked.connect(self.loadAnnotationInfo)
        self.show()

    def insertList(self):
        viewertools.show(r"D:\projects\share\data\CT\1.3.12.2.1107.5.1.4.12345.4.0.1740126031831309")
        sql = ('select * from volume_dicominfo');
        cursor.execute(sql)
        rows = cursor.fetchone()
        print(rows)

    def loadDicomInfo(self):
        query = ('select * from volume_dicominfo');
        tableWidget = self.ui.tableWidget
        self.loadData(query, tableWidget)

    def loadAnnotationInfo(self):
        loadquery = ('select * from windowlevel_annotation');
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
        global IMAGE
        IMAGE = self.ui.tableWidget.item(row, column_number).text()
        print ("CELL VALUE FROM LOAD IMAGE: ", IMAGE)
        plasma.die()
        plasma.start()
        viewertools.show(IMAGE)

    def saveAnnotation(self):
        uid = ''.join(random.Random().sample(string.letters + string.digits, random.randint(10,20)))
        world_FovSize = float(float(vpiv.getfov(vpiv.currentimage()))) #size of ROI
        world_cord = cad_utils.floatlist(vpiv.currentworldcoordinateswithwindowid(vpiv.currentimage())) #world location
        world_cord_str = str(world_cord)
        window_low, window_high = cad_utils.floatlist(vpiv.getscalarwindow(plasmatools.allsids()[0]))
        b0= ivtools.getBookmarkedView() #complete details
        strb0 = ' '.join(b0)
        insertQuery = """ INSERT INTO windowlevel_annotation(anno_id, world_coordination, world_dimension, window_low, window_high, annotation_details)
        VALUES(%s,%s,%s,%s,%s,%s) """
        cursor.execute(insertQuery,(uid, world_cord_str, world_FovSize, window_low, window_high, strb0))
        connection.commit()

    def showAnnotation(self, row, column_number):
        print ("Row: %d and Column is %d" %(row, column_number))
        annoDetailsColumn = 5
        windowHighColumn = 4
        windowLowColumn = 3
        worldCoordColumn = 1
        if not column_number == 5:
            temp_column_number = 5 - column_number #actual column_number
            annoDetailsColumn = temp_column_number + column_number #always 5
            print (column_number)
        annoDetailCell = self.ui.tableWidget_2.item(row,column_number).text()
        print (annoDetailCell)
        
        vpiv.goto(world_cord[0], world_cord[1], world_cord[2])
        vpiv.setfov(world_FovSize)
        vpiv.setscalarwindow(img, window_low, window_high, 1)


    # def ShowAnnotation(world_FovSize, window_low, window_high, world_cord, cell):
    #     vpiv.goto(world_cord[0], world_cord[1], world_cord[2])
    #     vpiv.setfov(world_FovSize)
    #     vpiv.setscalarwindow(img, window_low, window_high, 1)

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
