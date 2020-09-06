from stopwatch import Stopwatch
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication , QLCDNumber, QRadioButton
import sys
from time import strftime

var = True

class DigitalClock(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.Time)
        self.timer.start(10)

        self.clock_screen = QLCDNumber(self)
        self.clock_screen.resize(250,100)

        # Added self.lcd.move and moved the clock 30px down to make space for buttons
        self.clock_screen.move(0,30)
        self.clock_screen.display(strftime("%H" + ":" + "%M"))


        self.r1 = QRadioButton("Hide seconds", self)
        self.r1.move(10, 0)
        self.r2 = QRadioButton("Show seconds", self)
        self.r2.move(110, 0)

        self.r1.toggled.connect(self.woSecs)
        self.r2.toggled.connect(self.wSecs)

        # ---------Window settings --------------------------------

        # Expanded window height by 30px

        self.setGeometry(300, 300, 250, 130)
        self.setWindowTitle("Digital Clock")
        self.setWindowIcon(QtGui.QIcon(""))
        self.show()

    # -------- Slots ------------------------------------------

    def Time(self):
        global var
        if var == True:
            self.clock_screen.display(strftime("%H" + ":" + "%M"))
        elif var == False:
            self.clock_screen.display(strftime("%H" + ":" + "%M" + ":" + "%S"))

    def wSecs(self):
        global var
        var = False

        self.resize(375, 130)
        self.clock_screen.resize(375, 100)
        self.clock_screen.setDigitCount(8)

    def woSecs(self):
        global var
        var = True

        self.resize(250, 130)
        self.clock_screen.resize(250, 100)
        self.clock_screen.setDigitCount(5)


def main():
    app = QApplication(sys.argv)
    main = DigitalClock()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__" :
    main()