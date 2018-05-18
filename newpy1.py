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
sys.path.append(ALPHAROOT + "bin")
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
    cell = 0
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
        self.ui.btn2.clicked.connect(self.loadData)
        self.ui.tableWidget.cellDoubleClicked.connect(self.loadImage)
        self.ui.btnR.clicked.connect(self.saveAnnotation)
        # exePath = "C:\Users\z003x7ma\source\repos\FlaskWebProject1\FlaskWebProject1\FlaskWebProject1\cad\Plasma\bin_27\Plasma.exe"
        # subprocess.Popen(exePath)
        # hwnd = win32gui.FindWindowEx(0, 0, "PlasmaFrame", "1")
        # time.sleep(0.05)
        # window = QWindow.fromWindId(hwnd)
        # self.createWindowContainer(window, self)
        self.show()

    def insertList(self):
        viewertools.show(r"D:\projects\share\data\CT\1.3.12.2.1107.5.1.4.12345.4.0.1740126031831309")
        sql = ('select * from volume_dicominfo');
        cursor.execute(sql)
        rows = cursor.fetchone()
        print(rows)

    def loadData(self):
        query = ('select * from volume_dicominfo');
        cursor.execute(query)
        result = cursor.fetchall()
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                print("This is column ", column_number)
                print("This is row ", row_number)

    def loadImage(self, row, column_number):
        global cell
        cell = self.ui.tableWidget.item(row, column_number).text()
        print ("CELL VALUE FROM LOAD IMAGE: ", cell)
        plasma.die()
        plasma.start()
        viewertools.show(cell)

    def saveAnnotation(self):
        # Get the ROI size
        print ("Roi size is ", float(vpiv.getfov(0)))
        # Get the cursor center
        # print(ivtools.currentworldcord(vpiv.currentimage()))
        # Get the window levels
        print("Window levels ", cad_utils.floatlist(vpiv.getscalarwindow(plasmatools.allsids()[0])))
        # set the window levels
        Windowlevel = [200, 1700]
        print ("CELL IS ", cell)
        img = dicomloader.load(cell, "img")
        vpiv.setscalarwindow(img, windowlevel[0], windowlevel[1], 1)


def main():
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (design)
    form.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
    form.move(0,0)
    form.show()                         # Show the form
    sys.exit(app.exec_())                      # and execute the app

if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
