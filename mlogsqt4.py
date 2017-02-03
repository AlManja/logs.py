#!/usr/bin/env python

import os
import sys  # provides interaction with the Python interpreter

from functools import partial

from PyQt4 import QtGui  # provides the graphic elements
from PyQt4.QtCore import pyqtSlot  # provides the 'pyqtSlot()' decorator
from PyQt4.QtCore import Qt  # provides Qt identifiers
from PyQt4.QtGui import QApplication, QPushButton

chkbut1=0
chkbut2=0
chkbut3=0

class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # creates the checkbox
        checkbox1 = QtGui.QCheckBox('&Inxi - (inxi -Fxzc0)')                # the shortcut key is ALT + I
        checkbox2 = QtGui.QCheckBox('&Xorg.0 - (/var/log/Xorg.0.log)')      # the shortcut key is ALT + x
        checkbox3 = QtGui.QCheckBox('X&org.1 - (/var/log/Xorg.1.log)')
        checkbox4 = QtGui.QCheckBox('&pacman.log - (/var/log/pacman.log)')
        checkbox5 = QtGui.QCheckBox('&pacman.log - (+Warnings)')
        checkbox6 = QtGui.QCheckBox('journalctl.txt - (&Emergency)')
        checkbox7 = QtGui.QCheckBox('journalctl.txt - (&Alert)')
        checkbox8 = QtGui.QCheckBox('journalctl.txt - (&Critical)')
        checkbox9 = QtGui.QCheckBox('journalctl.txt - (&Failed)')

        btn = QPushButton("&Save to File (not working)", self)

        # connects the 'stateChanged()' signal with the 'checkbox_state_changed()' slot
        checkbox1.stateChanged.connect(self.checkbox1_state_changed)
        checkbox2.stateChanged.connect(self.checkbox2_state_changed)
        checkbox3.stateChanged.connect(self.checkbox3_state_changed)
        checkbox4.stateChanged.connect(self.checkbox4_state_changed)
        checkbox5.stateChanged.connect(self.checkbox5_state_changed)
        checkbox6.stateChanged.connect(self.checkbox6_state_changed)
        checkbox7.stateChanged.connect(self.checkbox7_state_changed)
        checkbox8.stateChanged.connect(self.checkbox8_state_changed)
        checkbox9.stateChanged.connect(self.checkbox9_state_changed)

        btn.clicked.connect(partial(self.doit))


        # creates a vertical box layout for the window
        vlayout = QtGui.QVBoxLayout()
        vlayout.addWidget(checkbox1)  # adds the checkbox to the layout
        vlayout.addWidget(checkbox2)  # adds the checkbox to the layout
        vlayout.addWidget(checkbox3)  # adds the checkbox to the layout
        vlayout.addWidget(checkbox4)
        vlayout.addWidget(checkbox5)
        vlayout.addWidget(checkbox6)
        vlayout.addWidget(checkbox7)
        vlayout.addWidget(checkbox8)
        vlayout.addWidget(checkbox9)
        vlayout.addWidget(btn)
        vlayout.addStretch()
        self.setLayout(vlayout)  # sets the window layout

    # 'checkbox_state_changed()' slot
    @pyqtSlot(int)
    def checkbox1_state_changed(self, state):
        """Full system and hardware information (Inxi -Fxzc0)"""
        if state == Qt.Checked:
            try:
                print()
                print('===============')
                print('| Inxi -Fxzc0 |   Listing computer information')
                print('===============')
                os.system('inxi -Fxzc0')
                print()
            except:
                print('Do you have installed: "inxi" on your system? ')
        # if state != Qt.Checked:
        #     chkbut1=0
        #     print(chkbut1)

    def checkbox2_state_changed(self, state):
        """from Xorg.0.log print lines that contain words: failed, error, (WW)"""
        if state == Qt.Checked:
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

        # if state != Qt.Checked:
        #     chkbut2=0
        #     print(chkbut2)

    def checkbox3_state_changed(self, state):
        """from Xorg.1.log print lines that contain words: failed, error, (WW)"""
        if state == Qt.Checked:
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

        # if state != Qt.Checked:
        #     chkbut3=0
        #     print(chkbut3)

    def checkbox4_state_changed(self, state):
        """from pacman.log print lines that contain words: pacsave, pacnew, pacorig"""
        if state == Qt.Checked:
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

    def checkbox5_state_changed(self, state):
        """from pacman.log print lines that contain words: warning"""
        if state == Qt.Checked:
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

    def checkbox6_state_changed(self, state):
        """from journalctl.txt returns lines that contain keyword: emergency"""
        if state == Qt.Checked:
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

    def checkbox7_state_changed(self, state):
        """from journalctl.txt returns lines that contain: alert"""
        if state == Qt.Checked:
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

    def checkbox8_state_changed(self, state):
        """from journalctl.txt returns lines that contain: critical"""
        if state == Qt.Checked:
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

    def checkbox9_state_changed(self, state):
        """from journalctl.txt returns lines that contain: failed"""
        if state == Qt.Checked:
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


    def doit(self, text):
        print(chkbut1, chkbut2, chkbut3)  # debug
        if chkbut1 == 1:
            print("Routine1")
            #run some code

        if chkbut2 == 1:
            print("Routine2")
            #run some code

        if chkbut3 == 1:
            print("Routine3")
            #run some code

# creates the application and takes arguments from the command line
application = QtGui.QApplication(sys.argv)

# creates the window and sets its properties
window = Window()
window.setWindowTitle('QCheckBox')  # title
window.resize(280, 50)  # size
window.show()  # shows the window

# runs the application and waits for its return value at the end
sys.exit(application.exec_())