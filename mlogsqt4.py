#!/usr/bin/env python

import os
import sys                           # provides interaction with the Python interpreter
from functools import partial
from PyQt4 import QtGui              # provides the graphic elements
from PyQt4.QtCore import pyqtSlot    # provides the 'pyqtSlot()' decorator
from PyQt4.QtCore import Qt          # provides Qt identifiers
from PyQt4.QtGui import QPushButton, QApplication
from sh import inxi                  # The sh library is awesome for linux users

chkbut1=0
chkbut2=0
chkbut3=0
chkbut4=0
chkbut6=0
chkbut7=0
chkbut8=0
chkbut9=0


class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # creates the checkbox
        checkbox1 = QtGui.QCheckBox('&Inxi - (inxi -Fxzc0)')                # the shortcut key is ALT + I
        checkbox2 = QtGui.QCheckBox('&Xorg.0 - (/var/log/Xorg.0.log)')      # the shortcut key is ALT + x
        checkbox3 = QtGui.QCheckBox('X&org.1 - (/var/log/Xorg.1.log)')
        checkbox4 = QtGui.QCheckBox('&pacman.log - (/var/log/pacman.log)')
        checkbox6 = QtGui.QCheckBox('journalctl.txt - (&Emergency)')
        checkbox7 = QtGui.QCheckBox('journalctl.txt - (&Alert)')
        checkbox8 = QtGui.QCheckBox('journalctl.txt - (&Critical)')
        checkbox9 = QtGui.QCheckBox('journalctl.txt - (&Failed)')

        btn = QPushButton("&Show Errors (/tmp/mlogsout.txt))", self)
        btn2 = QPushButton("&PasteBin - not working yet", self)

        # connects the 'stateChanged()' signal with the 'checkbox_state_changed()' slot
        checkbox1.stateChanged.connect(self.checkbox1_state_changed)
        checkbox2.stateChanged.connect(self.checkbox2_state_changed)
        checkbox3.stateChanged.connect(self.checkbox3_state_changed)
        checkbox4.stateChanged.connect(self.checkbox4_state_changed)
        checkbox6.stateChanged.connect(self.checkbox6_state_changed)
        checkbox7.stateChanged.connect(self.checkbox7_state_changed)
        checkbox8.stateChanged.connect(self.checkbox8_state_changed)
        checkbox9.stateChanged.connect(self.checkbox9_state_changed)

        btn.clicked.connect(partial(self.to_computer))
        btn.clicked.connect(self.to_editor)
        # btn.clicked.connect(partial(self.to_computer))
        # btn2.clicked.connect(self.to_web)


        # creates a vertical box layout for the window
        vlayout = QtGui.QVBoxLayout()
        vlayout.addWidget(checkbox1)  # adds the checkbox to the layout
        vlayout.addWidget(checkbox2)
        vlayout.addWidget(checkbox3)
        vlayout.addWidget(checkbox4)
        vlayout.addWidget(checkbox6)
        vlayout.addWidget(checkbox7)
        vlayout.addWidget(checkbox8)
        vlayout.addWidget(checkbox9)
        vlayout.addWidget(btn)
        vlayout.addWidget(btn2)
        vlayout.addStretch()
        self.setLayout(vlayout)  # sets the window layout

    # 'checkbox_state_changed()' slot
    @pyqtSlot(int)
    def checkbox1_state_changed(self, state):
        """Full system and hardware information (Inxi -Fxzc0)"""
        if state == Qt.Checked:
            global chkbut1
            chkbut1=1
        if state != Qt.Checked:
            chkbut1=0

    def checkbox2_state_changed(self, state):
        """from Xorg.0.log print lines that contain words: failed, error, (WW)"""
        if state == Qt.Checked:
            global chkbut2
            chkbut2=1
        if state != Qt.Checked:
            chkbut2=0

    def checkbox3_state_changed(self, state):
        """from Xorg.1.log print lines that contain words: failed, error, (WW)"""
        if state == Qt.Checked:
            global chkbut3
            chkbut3=1
        if state != Qt.Checked:
            chkbut3=0

    def checkbox4_state_changed(self, state):
        """from pacman.log print lines that contain words: pacsave, pacnew, pacorig"""
        if state == Qt.Checked:
            global chkbut4
            chkbut4=1
        if state != Qt.Checked:
            chkbut4=0

    def checkbox6_state_changed(self, state):
        """from journalctl.txt returns lines that contain keyword: emergency"""
        if state == Qt.Checked:
            global chkbut6
            chkbut6 = 1
        if state != Qt.Checked:
            chkbut6=0

    def checkbox7_state_changed(self, state):
        """from journalctl.txt returns lines that contain: alert"""
        if state == Qt.Checked:
            global chkbut7
            chkbut7 = 1
        if state != Qt.Checked:
            chkbut7=0

    def checkbox8_state_changed(self, state):
        """from journalctl.txt returns lines that contain: critical"""
        if state == Qt.Checked:
            global chkbut8
            chkbut8 = 1
        if state != Qt.Checked:
            chkbut8=0

    def checkbox9_state_changed(self, state):
        """from journalctl.txt returns lines that contain: failed"""
        if state == Qt.Checked:
            global chkbut9
            chkbut9 = 1
        if state != Qt.Checked:
            chkbut9=0

    def to_computer(self, text):
        f = open('/tmp/mlogsout.txt', 'w')  # write mode clears any previous content from the file if it exists

        if chkbut1 == 1:
            # write output of 'Inxi -Fxzc0' into /tmp/mlogsout.txt
            print("Saving: inxi to file")
            f.write('===============\n')
            f.write('| Inxi -Fxzc0 |   Listing computer information\n')
            f.write('===============\n')
            f.write(str(inxi('-Fxzc0')))
            f.write('\n')

        if chkbut2 == 1:
            print("Saving: Xorg.0.log to file")
            with open('/var/log/Xorg.0.log', 'r') as f1:
                f.write('==============\n')
                f.write('| Xorg.0.log |   (searching for: failed, error & (WW) keywords\n')
                f.write('==============\n')
                for line in f1:
                    if 'failed' in line or 'error' in line or '(WW)' in line:
                        f.write(line)
            f.write('\n')

        if chkbut3 == 1:
            print("Saving: Xorg.1.log to file")
            with open('/var/log/Xorg.1.log', 'r') as f2:
                f.write('==============\n')
                f.write('| Xorg.1.log |   (searching for: failed, error & (WW) keywords\n')
                f.write('==============\n')
                for line in f2:
                    if 'failed' in line or 'error' in line or '(WW)' in line:
                        f.write(line)
            f.write('\n')

        if chkbut4 == 1:
            print("Saving: pacman.log to file")
            with open('/var/log/pacman.log', 'r') as f3:
                f.write('==============\n')
                f.write('| pacman.log |   (searching for: pacsave, pacnew, pacorig keywords\n')
                f.write('==============\n')
                for line in f3:
                    if 'pacsave' in line or 'pacnew' in line or 'pacorig' in line:
                        f.write(line)
            f.write('\n')

        if chkbut6 == 1:
            print("Saving: journalctl (mergency) to file")
            os.system("journalctl -b > /tmp/journalctl.txt")
            with open('/tmp/journalctl.txt', 'r') as f4:
                f.write('==================\n')
                f.write('| journalctl.txt |   Searching for: Emergency keywords\n')
                f.write('==================\n')
                key_word = ['emergency', 'Emergency', 'EMERGENCY']
                for line in f4:
                    for word in key_word:
                        if word in line:
                            f.write(line)
            f.write('\n')

        if chkbut7 == 1:
            print("Saving: journalctl (alert) to file")
            os.system("journalctl -b > /tmp/journalctl.txt")
            with open('/tmp/journalctl.txt', 'r') as f5:
                f.write('==================\n')
                f.write('| journalctl.txt |   Searching for: Alert keywords\n')
                f.write('==================\n')
                key_word = ['alert', 'Alert', 'ALERT']
                for line in f5:
                    for word in key_word:
                        if word in line:
                            f.write(line)
            f.write('\n')

        if chkbut8 == 1:
            print("Saving: journalctl (critical) to file")
            os.system("journalctl -b > /tmp/journalctl.txt")
            with open('/tmp/journalctl.txt', 'r') as f6:
                f.write('==================\n')
                f.write('| journalctl.txt |   Searching for: Critical keywords\n')
                f.write('==================\n')
                key_word = ['critical', 'Critical', 'CRITICAL']
                for line in f6:
                    for word in key_word:
                        if word in line:
                            f.write(line)
            f.write('\n')

        if chkbut9 == 1:
            print("Saving: journalctl (failed) to file")
            os.system("journalctl -b > /tmp/journalctl.txt")
            with open('/tmp/journalctl.txt', 'r') as f7:
                f.write('==================\n')
                f.write('| journalctl.txt |   Searching for: Failed keywords\n')
                f.write('==================\n')
                key_word = ['failed', 'Failed', 'FAILED']
                for line in f7:
                    for word in key_word:
                        if word in line:
                            f.write(line)
            f.write('\n')

        f.close()

    def to_editor(self):
        os.system("xdg-open /tmp/mlogsout.txt")

    def to_web(self):
        pass

# creates the application and takes arguments from the command line
application = QtGui.QApplication(sys.argv)

# creates the window and sets its properties
window = Window()
window.setWindowTitle('QCheckBox')  # title
window.resize(280, 50)  # size
window.show()  # shows the window

# runs the application and waits for its return value at the end
sys.exit(application.exec_())
