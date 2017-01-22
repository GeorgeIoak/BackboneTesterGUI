# Code based on
# From https://www.baldengineer.com/raspberry-pi-gui-tutorial.html 
# by James Lewis (@baldengineer)
# 
# Backbone Tester Operator Interface
#
# If you make changes to the Qt form then
# pyuic5 mainwindow.ui > mainwindow_auto.py
#
# To run, python3 main.py
#
# nano /home/pi/.config/lxsession/LXDE-pi/autostart
# And add this line:
# @/usr/bin/python3 /home/pi/main.py

# always seem to need this
import sys
import time
import serial

# This gets the Qt stuff
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, uic, QtCore
import RPi.GPIO as GPIO

# Serial port Config
port = "/dev/ttyACM0"
baud = 115200
 
ser = serial.Serial(port, baud, timeout=1)
    # open the serial port
if ser.isOpen():
     print(ser.name + ' is open...')
cmd = "G91 G0 X10" # For testing icremental move
motorOff = "M84" # This disables the motors so the power suppply fan will stop

# GPIO Setup
GPIO.setmode(GPIO.BCM) #Use actual Broadcom GPIO numbering
GPIO.setwarnings(False) #Disables the Warning

GPIO.setup(27, GPIO.IN) #Over Current (OC, default high) from Tester
GPIO.setup(17, GPIO.OUT) #TPS2149 Enable (EN1, default high) to Tester
GPIO.setup(4, GPIO.OUT) #Program Start (Ctrl) to Tester
GPIO.setup(8, GPIO.IN) #Motor PWM Signal (PWM) from Tester

# This is our window from QtCreator
import mainwindow_auto

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    ### functions for the buttons to call
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        ### Hooks to for buttons
        self.btnGo.clicked.connect(lambda: self.pressedbtnGo())
        self.btnShort.clicked.connect(lambda: self.pressedbtnShort())
        
    def pressedbtnGo(self):
        print ("Pressed Start Button!")
        GPIO.setmode(GPIO.BCM) #Use actual Broadcom GPIO numbering
        GPIO.setup(17, GPIO.OUT) #TPS2149 Enable (EN1, default high) to Tester
        GPIO.output(17, 1)
        ser.write(cmd.encode('UTF-8')+b'\r\n')
        self.brd1A.setStyleSheet("background-color:green;")

    def pressedbtnShort(self):
        print ("Pressed Short Button!")
        GPIO.setmode(GPIO.BCM) #Use actual Broadcom GPIO numbering
        GPIO.setup(17, GPIO.OUT) #TPS2149 Enable (EN1, default high) to Tester
        GPIO.output(17, 0)
        self.brd1A.setStyleSheet("background-color:red;")
        
    def closeEvent(self, event): # GPIO cleanup upon closing the GUI by terminal
        print ("GPIO CleanUP")
        GPIO.cleanup()
        ser.write(motorOff.encode('UTF-8')+b'\r\n')
        ser.close() 
        event.accept()

    

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
