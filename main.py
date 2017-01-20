# From https://www.baldengineer.com/raspberry-pi-gui-tutorial.html 
# by James Lewis (@baldengineer)
# Minimal python code to start PyQt5 GUI
#
# If you make changes to the Qt form then
# pyuic5 mainwindow.ui > mainwindow_auto.py
#
# To run, python3 main.py

# always seem to need this
import sys

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *

# GPIO Related
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) #Use actual Broadcom GPIO numbering

GPIO.setup(27, GPIO.IN) #Over Current (OC) from Tester
GPIO.setup(17, GPIO.OUT) #TPS2149 Enable (EN1, default high) to Tester
GPIO.setup(04, GPIO.OUT, pull_up_down=GPIO.PUD_UP) #Program Start (Ctrl) to Tester
GPIO.setup(08, GPIO.IN) #Motor PWM Signal (PWM) from Tester

# This is our window from QtCreator
import mainwindow_auto

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    ### functions for the buttons to call
    def pressedbtnGo(self):
        print ("Pressed Start Button!")
        self.brd1A.setStyleSheet("background-color:green;")

    def pressedbtnShort(self):
        print ("Pressed Short Button!")

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        ### Hooks to for buttons
        self.btnGo.clicked.connect(lambda: self.pressedbtnGo())
        self.btnShort.clicked.connect(lambda: self.pressedbtnShort())

# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    # without this, the script exits immediately.
    GPIO.cleanup() #  Release GPIOs
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
    main()