
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QFont, QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)

from PyQt5.QtWidgets import (
QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout, QMessageBox, QRadioButton)
from inst import *
from final_win import *

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.text_timer = QLabel(txt_timer)

        self.lFio = QLabel(txt_fio)
        self.tFio = QLineEdit()

        self.lAge = QLabel( txt_age )
        self.tAge = QLineEdit()

        self.lFT = QLabel( txt_first_test )
        self.bFT = QPushButton( txt_start_first )
        self.tScore1 = QLineEdit()

        self.lST = QLabel( txt_sec_test )
        self.bST = QPushButton( txt_start_sec )

        self.lTT = QLabel( txt_third_test )
        self.bTT = QPushButton( txt_start_third )

        self.tScore2 = QLineEdit()
        self.tScore3 = QLineEdit()
        self.bNext = QPushButton( txt_next_two )

        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.lFio, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.tFio, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.lAge, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.tAge, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.lFT, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.bFT, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.tScore1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.lST, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.bST, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.lTT, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.bTT, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.tScore2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.tScore3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.bNext, alignment = Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def connects(self):
        self.bNext.clicked.connect(self.next_click)
        self.bFT.clicked.connect(self.timer_test)
        self.bST.clicked.connect(self.timer_sits)
        self.bTT.clicked.connect(self.timer_final)

    def timer_test(self):
        global time
        time = QTime(0,0,15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer_sits(self):
        global time
        time = QTime(0,0,45)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer_final(self):
        global time
        time = QTime(0,1,0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
           self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
           self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def next_click(self):
       self.hide()
       self.exp = Experiment(int(self.tAge.text()),
                             int(self.tScore1.text()),
                             int(self.tScore2.text()),
                             int(self.tScore3.text()))
       self.fw = FinalWin(self.exp)
app = QApplication([])