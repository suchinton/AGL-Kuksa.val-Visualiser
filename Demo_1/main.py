# import kuksa_viss_client as kuksa
import kuksa_client as kuksa

from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit,\
     QPushButton, QToolButton, QLabel, QTabWidget, QSpinBox, QSlider, \
     QLCDNumber
from PyQt5.QtCore import *
from PyQt5 import QtWidgets 
from PyQt5 import uic
import sys
import os
from threading import *

import time

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        # Load App
        uic.loadUi("Main_window.ui",self)

        # Define Tab to navigat
        self.Tab = self.findChild(QTabWidget,"Tab")
                
        # Define Widgets

        ## for Live tab
        self.Top_speed_input = self.findChild(QSpinBox,"Top_speed_input")
        self.Speed_slider = self.findChild(QSlider, "Speed_slider")
        self.Speed_monitor = self.findChild(QLCDNumber, "Speed_monitor")
        self.Accept_Top_speed = self.findChild(QPushButton, "Accept_Top_speed")
        self.update_Top_speed()

        # Actions to events
        self.Accept_Top_speed.clicked.connect(self.update_Top_speed)
        self.Speed_slider.valueChanged.connect(self.update_Speed_monitor)

        # Show App
        self.show()

    def update_Top_speed(self):
        Top_speed = self.Top_speed_input.value()
        self.Speed_slider.setMinimum(0)
        self.Speed_slider.setMaximum(Top_speed)

    def update_Speed_monitor(self):
        speed = int(self.Speed_slider.value())
        self.Speed_monitor.display(speed)
        try:
            client.setValue('Vehicle.Speed',str(speed),'value')
            print(f"Feeding Vehicle.Speed to {speed}")
        except:
            print("Error!! kuksa_client not configured properly.")

# init the app
if __name__ == '__main__':

    config = {
    "hostname": '127.0.0.1',
    "port": 8090
    }

    try:
        client = kuksa.KuksaClientThread(config)
        client.authorize("/home/suchinton/.local/lib/python3.8/site-packages/kuksa_certificates/jwt/super-admin.json.token")
        client.start()
    except Exception as e:
        print(e)
    # for speed in range(0,100):
    #     client.setValue('Vehicle.Speed',str(float(speed)),'value')
    #     print(f"Feeding Vehicle.Speed to {speed}")
    #     time.sleep(1)
    
    app = QApplication(sys.argv)
    Main_pg = MainWindow()
    sys.exit(app.exec())
