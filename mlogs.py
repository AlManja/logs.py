#!/usr/bin/env python

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
#os.system("journalctl -b > /tmp/journalctl.txt")

def inxi():
    """Full system and hardware information (Inxi -Fxzc0)"""
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


def read_pacman1():
    """from pacman.log print lines that contain words: pacsave, pacnew, pacorig"""
    try:
        with open('/var/log/pacman.log', 'r') as f:
            print('==============')
            print('| pacman.log |   (searching for: pacsave, pacnew, pacorig keywords')
            print('==============')
            for line in f:
                if 'pacsave' in line or 'pacnew' in line or 'pacorig' in line:
                    print(line, end='')
        print()
    except:
        print('Missing file: pacman.log   This is not Arch based distribution?')


def read_pacman2():
    """from pacman.log print lines that contain words: warning"""
    try:
        with open('/var/log/pacman.log', 'r') as f:
            print('==============')
            print('| pacman.log |   (searching for: warning keyword')
            print('==============')
            for line in f:
                if 'warning' in line:
                    print(line, end='')
        print()
    except:
        print('Missing file: pacman.log   This is not Arch based distribution?')


def read_journalctl_1():
    """from journalctl.txt returns lines that contain keyword: emergency"""
    try:
        os.system("journalctl -b > /tmp/journalctl.txt")
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
        os.system("journalctl -b > /tmp/journalctl.txt")
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
        os.system("journalctl -b > /tmp/journalctl.txt")
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
        os.system("journalctl -b > /tmp/journalctl.txt")
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
        self.checkbox1 = QCheckBox('&Inxi - (inxi -Fxzc0)')
        self.checkbox2 = QCheckBox('&Xorg.0 - (/var/log/Xorg.0.log)')
        self.checkbox3 = QCheckBox('X&org.1 - (/var/log/Xorg.1.log)')
        self.checkbox4 = QCheckBox('&pacman.log - (/var/log/pacman.log)')
        # self.checkbox5 = QCheckBox('pac&man.log - (+warnings)')
        self.checkbox6 = QCheckBox('journalctl.txt - (&Emergency)')
        self.checkbox7 = QCheckBox('journalctl.txt - (&Alert)')
        self.checkbox8 = QCheckBox('journalctl.txt - (&Critical)')
        self.checkbox9 = QCheckBox('journalctl.txt - (&Failed)')
        self.button = QPushButton('&Search Log files')

        self.init_ui()

    def init_ui(self):
        self.setFont(QFont('SansSherif', 13))
        QToolTip.setFont(QFont('SansSherif', 12))

        self.checkbox1.setToolTip('Full system and hardware information')
        self.checkbox1.toggle()
        self.checkbox2.setToolTip('Graphical interface log from current session')
        self.checkbox2.toggle()
        self.checkbox3.setToolTip('Graphical interface log from previous session')
        self.checkbox3.toggle()
        self.checkbox4.setToolTip('Package manager log')
        self.checkbox4.toggle()
        # self.checkbox5.setToolTip('Package manager log')
        # self.checkbox5.toggle()
        self.checkbox6.setToolTip('Current full system log (to run it manually: journalctl -b')
        self.checkbox6.toggle()
        self.checkbox7.setToolTip('Current full system log; Search for "Alert"')
        self.checkbox7.toggle()
        self.checkbox8.setToolTip('Current full system log; Search for "Critical"')
        self.checkbox8.toggle()
        self.checkbox9.setToolTip('Current full system log; Search for "Failed"')

        layout = QVBoxLayout()
        layout.addWidget(self.checkbox1)
        layout.addWidget(self.checkbox2)
        layout.addWidget(self.checkbox3)
        layout.addWidget(self.checkbox4)
        # layout.addWidget(self.checkbox5)
        layout.addWidget(self.checkbox6)
        layout.addWidget(self.checkbox7)
        layout.addWidget(self.checkbox8)
        layout.addWidget(self.checkbox9)
        layout.addWidget(self.button)
        self.setLayout(layout)

        self.button.clicked.connect(self.button_click)
        self.show()

    def button_click(self):
        if self.checkbox1.isChecked():
            inxi()
        if self.checkbox2.isChecked():
            read_xorg0()
        if self.checkbox3.isChecked():
            read_xorg1()
        if self.checkbox4.isChecked():
            read_pacman1()
        # if self.checkbox5.isChecked():
        #     read_pacman2()
        if self.checkbox6.isChecked():
            read_journalctl_1()
        if self.checkbox7.isChecked():
            read_journalctl_2()
        if self.checkbox8.isChecked():
            read_journalctl_3()
        if self.checkbox9.isChecked():
            read_journalctl_4()

app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
