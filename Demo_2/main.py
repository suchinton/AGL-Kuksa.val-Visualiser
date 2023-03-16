from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit,\
     QPushButton,QToolButton, QLabel, QTabWidget, QSpinBox, QSlider, \
     QLCDNumber
from PyQt5.QtCore import *
from PyQt5 import QtWidgets 
from PyQt5 import uic
import sys

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
        print("speed: ", speed)



# init the app
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    Main_pg = MainWindow()
    sys.exit(app.exec())

