from kuksa_client.grpc import VSSClient
from kuksa_client.grpc import Datapoint

import subprocess
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit,\
     QPushButton,QToolButton, QFileDialog, QLabel, QTabWidget, \
     QPlainTextEdit,QTableWidget, QProgressBar, QListWidget,QDockWidget, QMessageBox
from PyQt5.QtCore import *
from PyQt5 import QtWidgets 
from PyQt5 import uic
import sys
import os
from threading import *

import time

with VSSClient('127.0.0.1', 55555) as client:
    for speed in range(0,100):
        client.set_current_values({
        'Vehicle.Speed': Datapoint(speed),
        })
        print(f"Feeding Vehicle.Speed to {speed}")
        time.sleep(1)
print("Finished.")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        # Load App
        uic.loadUi("Main_window.ui",self)
        # Show App
        self.show()

# init the app
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    Main_pg = MainWindow()
    sys.exit(app.exec())

