import os
import sys
from os.path import expanduser
from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QApplication, QWidget, QCheckBox

"""
This script prints out some errors from log files (Xorg.0.log, Xorg.1.log, pacman.log and journalctl.txt
It is intended for Linux OS (Arch based: Manjaro) For other Linux versions comment out function: read_pacman()
Before you run the script, in terminal run: journalctl -b > /path/to/your/home/journalctl.txt to pipe binary log to txt
"""

home = expanduser("~")

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


def read_journalctl():
    """from journalctl.txt print lines that contain: emergency, alert, critical & failed; 0: emerg, 1: alert 2: crit"""

    try:
        #with open(home + '/journalctl.txt', 'r') as f:
        os.system("journalctl -b > /tmp/journalctl.txt")
        with open("/tmp/journalctl.txt") as f:
            print('==================')
            print('| journalctl.txt |   Searching for: emergency, alert, critical & failed keywords')
            print('==================')
            key_word = ['emergency', 'Emergency', 'EMERGENCY', 'alert', 'Alert', 'ALERT', 'critical', 'Critical',
                        'CRITICAL', 'failed']
            for line in f:
                for word in key_word:
                    if word in line:
                        print(line, end='')
    except:
        print('Missing file: /tmp/journalctl.txt')


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.chkb_1 = QCheckBox('Xorg.0.log')
        self.chkb_2 = QCheckBox('Xorg.1.log')
        self.chkb_3 = QCheckBox('pacman.log')
        self.chkb_4 = QCheckBox('journalctl.txt')
        self.btn = QPushButton('Search Log files')

        layout = QVBoxLayout()
        layout.addWidget(self.chkb_1)
        layout.addWidget(self.chkb_2)
        layout.addWidget(self.chkb_3)
        layout.addWidget(self.chkb_4)
        layout.addWidget(self.btn)

        self.setLayout(layout)

        self.btn.clicked.connect(self.btn_clk)
        self.show()

    def btn_clk(self):
        if self.chkb_1.isChecked():
            read_xorg0()
        if self.chkb_2.isChecked():
            read_xorg1()
        if self.chkb_3.isChecked():
            read_pacman()
        if self.chkb_4.isChecked():
            read_journalctl()


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())