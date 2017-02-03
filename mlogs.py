import os
import sys
from os.path import expanduser
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QApplication, QWidget, QCheckBox, QToolTip
from PyQt5.QtGui import QFont

"""
This script prints out 'inxi -Fxzc0' and some errors from log files (Xorg.0.log, Xorg.1.log, pacman.log and journalctl.txt
It is primarily intended for Linux OS, Arch based: Manjaro. Will probably work on other Linux systems also, but make sure you have installed 'inxi'
"""

home = expanduser("~")


def inxi():
    try:
        print()
        print('===============')
        print('| Inxi -Fxzc0 |   Listing computer information')
        print('===============')
        os.system('inxi -Fxzc0')
        print()
    except:
        print('Do you have installed: "inxi" on your system? ')


def read_xorg0():
    """from Xorg.0.log print lines that contain words: failed, error, (WW)"""
    try:
        with open('/var/log/Xorg.0.log', 'r') as f:
            print('==============')
            print('| Xorg.0.log |   (searching for: failed, error & (WW) keywords')
            print('==============')
            for line in f:
                if 'failed' in line or 'error' in line or '(WW)' in line:
                    print(line, end='')
        print()
    except:
        print('Missing file: Xorg.0.log')


def read_xorg1():
    """from Xorg.1.log print lines that contain words: failed, error, (WW)"""
    try:
        with open('/var/log/Xorg.1.log', 'r') as f:
            print('==============')
            print('| Xorg.1.log |   (searching for: failed, error & (WW) keywords')
            print('==============')
            for line in f:
                if 'failed' in line or 'error' in line or '(WW)' in line:
                    print(line, end='')
        print()
    except:
        print('Missing file: Xorg.1.log')


def read_pacman():
    """from pacman.log print lines that contain words: pacsave, pacnew, pacorig, warning"""
    try:
        with open('/var/log/pacman.log', 'r') as f:
            print('==============')
            print('| pacman.log |   (searching for: pacsave, pacnew, pacorig and warning keywords')
            print('==============')
            for line in f:
                if 'pacsave' in line or 'pacnew' in line or 'pacorig' in line or 'warning' in line:
                    print(line, end='')
        print()
    except:
        print('Missing file: pacman.log   This is not Arch based distribution?')



def read_journalctl_1():
    """from journalctl.txt returns lines that contain keyword: emergency"""
    try:
        os.system("journalctl -b > /tmp/journalctl1.txt")
        with open("/tmp/journalctl.txt") as f:
            print('==================')
            print('| journalctl.txt |   Searching for: Emergency keywords')
            print('==================')
            key_word = ['emergency', 'Emergency', 'EMERGENCY']
            for line in f:
                for word in key_word:
                    if word in line:
                        print(line, end='')
    except:
        print('Missing file: /tmp/journalctl.txt')


def read_journalctl_2():
    """from journalctl.txt returns lines that contain: alert"""
    try:
        os.system("journalctl -b > /tmp/journalctl2.txt")
        with open("/tmp/journalctl.txt") as f:
            print('==================')
            print('| journalctl.txt |   Searching for: Alert keywords')
            print('==================')
            key_word = ['alert', 'Alert', 'ALERT']
            for line in f:
                for word in key_word:
                    if word in line:
                        print(line, end='')
    except:
        print('Missing file: /tmp/journalctl.txt')


def read_journalctl_3():
    """from journalctl.txt returns lines that contain: critical"""
    try:
        os.system("journalctl -b > /tmp/journalctl3.txt")
        with open("/tmp/journalctl.txt") as f:
            print('==================')
            print('| journalctl.txt |   Searching for: Critical keywords')
            print('==================')
            key_word = ['critical', 'Critical', 'CRITICAL']
            for line in f:
                for word in key_word:
                    if word in line:
                        print(line, end='')
    except:
        print('Missing file: /tmp/journalctl.txt')


def read_journalctl_4():
    """from journalctl.txt returns lines that contain: failed"""
    try:
        os.system("journalctl -b > /tmp/journalctl4.txt")
        with open("/tmp/journalctl.txt") as f:
            print('==================')
            print('| journalctl.txt |   Searching for: Failed keywords')
            print('==================')
            key_word = ['failed', 'Failed', 'FAILED']
            for line in f:
                for word in key_word:
                    if word in line:
                        print(line, end='')
    except:
        print('Missing file: /tmp/journalctl.txt')



class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.chkb_0 = QCheckBox('Inxi - (inxi -Fxzc0)')
        self.chkb_1 = QCheckBox('Xorg.0 - (/var/log/Xorg.0.log)')
        self.chkb_2 = QCheckBox('Xorg.1 - /var/log/Xorg.1.log')
        self.chkb_3 = QCheckBox('pacman.log - (/var/log/pacman.log)')
        self.chkb_4 = QCheckBox('journalctl.txt  (Emergency)')
        self.chkb_5 = QCheckBox('journalctl.txt (Alert)')
        self.chkb_6 = QCheckBox('journalctl.txt - Critical')
        self.chkb_7 = QCheckBox('journalctl.txt - (Failed)')
        self.btn = QPushButton('Search Log files')

        self.init_ui()

    def init_ui(self):
        self.setFont(QFont('SansSherif', 14))
        QToolTip.setFont(QFont('SansSherif', 12))

        self.chkb_0.setToolTip('Full system and hardware information')
        self.chkb_0.toggle()

        self.chkb_1.setToolTip('Graphical interface log from current session')
        self.chkb_1.toggle()

        self.chkb_2.setToolTip('Graphical interface log from previous session')
        self.chkb_2.toggle()

        self.chkb_3.setToolTip('Package manager log')
        self.chkb_3.toggle()

        self.chkb_4.setToolTip('Current full system log (to run it manually: journalctl -b')
        self.chkb_4.toggle()

        self.chkb_5.setToolTip('Current full system log; Search for "Alert"')
        self.chkb_5.toggle()

        self.chkb_6.setToolTip('Current full system log; Search for "Critical"')
        self.chkb_6.toggle()

        self.chkb_7.setToolTip('Current full system log; Search for "Failed"')

        layout = QVBoxLayout()
        layout.addWidget(self.chkb_0)
        layout.addWidget(self.chkb_1)
        layout.addWidget(self.chkb_2)
        layout.addWidget(self.chkb_3)
        layout.addWidget(self.chkb_4)
        layout.addWidget(self.chkb_5)
        layout.addWidget(self.chkb_6)
        layout.addWidget(self.chkb_7)
        layout.addWidget(self.btn)
        self.setLayout(layout)

        self.btn.clicked.connect(self.btn_clk)
        self.show()

    def btn_clk(self):
        if self.chkb_0.isChecked():
            inxi()
        if self.chkb_1.isChecked():
            read_xorg0()
        if self.chkb_2.isChecked():
            read_xorg1()
        if self.chkb_3.isChecked():
            read_pacman()
        if self.chkb_4.isChecked():
            read_journalctl_1()
        if self.chkb_5.isChecked():
            read_journalctl_2()
        if self.chkb_6.isChecked():
            read_journalctl_3()
        if self.chkb_7.isChecked():
            read_journalctl_4()

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())

