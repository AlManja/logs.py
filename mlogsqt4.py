#!/usr/bin/env python

import os
import sys                           # provides interaction with the Python interpreter
from functools import partial
from PyQt4 import QtGui              # provides the graphic elements
from PyQt4.QtCore import Qt          # provides Qt identifiers
from PyQt4.QtGui import QPushButton
from sh import inxi                  # The sh library is awesome for linux users

TMP_FILE = "/tmp/mlogsout.txt"

HEADER = '''
==================
|{:^16}|   {}
==================
'''

checkbuttons = [
    '&Inxi - (inxi -Fxzc0)',
    '&Xorg.0 - (/var/log/Xorg.0.log)',
    'X&org.1 - (/var/log/Xorg.1.log)',
    '&pacman.log - (/var/log/pacman.log)',
    'journalctl.txt - (&Emergency)',
    'journalctl.txt - (&Alert)',
    'journalctl.txt - (&Critical)',
    'journalctl.txt - (&Failed)',
]


def look_in_file(file_name, kws):
    """reads a file and returns only the lines that contain one of the keywords"""
    with open(file_name) as f:
        return "".join(filter(lambda line: any(kw in line for kw in kws), f))


class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.checks = [False]*len(checkbuttons)  # initialize all buttons to False

        # creates a vertical box layout for the window
        vlayout = QtGui.QVBoxLayout()
        # creates the checkboxes
        for idx, text in enumerate(checkbuttons):
            checkbox = QtGui.QCheckBox(text)
            # connects the 'stateChanged()' signal with the 'checkbox_state_changed()' slot
            checkbox.stateChanged.connect(partial(self.checkbox_state_changed, idx))
            vlayout.addWidget(checkbox)  # adds the checkbox to the layout

        btn = QPushButton("&Show Errors ({})".format(TMP_FILE), self)
        btn.clicked.connect(self.to_computer)
        btn.clicked.connect(self.to_editor)

        vlayout.addWidget(btn)
        vlayout.addStretch()
        self.setLayout(vlayout)  # sets the window layout

    def checkbox_state_changed(self, idx, state):
        self.checks[idx] = state == Qt.Checked

    def to_computer(self, text):
        f = open(TMP_FILE, 'w')  # write mode clears any previous content from the file if it exists

        if self.checks[0]:
            # write output of 'Inxi -Fxzc0' into /tmp/mlogsout.txt
            # print("Saving: inxi to file")
            f.write(HEADER.format("Inxi -Fxzc0", "Listing computer information"))
            f.write(str(inxi('-Fxzc0')))
            f.write('\n')

        if self.checks[1]:
            # print("Saving: Xorg.0.log to file")
            f.write(HEADER.format("Xorg.0.log", "searching for: failed, error & (WW) keywords"))
            try:
                f.write(look_in_file('/var/log/Xorg.0.log', ['failed', 'error', '(WW)']))
            except FileNotFoundError:
                print("/var/log/Xorg.0.log not found!")
                f.write("Xorg.0.log not found!")
            f.write('\n')

        if self.checks[2]:
            # print("Saving: Xorg.1.log to file")
            f.write(HEADER.format("Xorg.1.log", "searching for: failed, error & (WW) keywords"))
            try:
                f.write(look_in_file('/var/log/Xorg.1.log', ['failed', 'error', '(WW)']))
            except FileNotFoundError:
                print("/var/log/Xorg.1.log not found, this is not Manjaro?")
                f.write("Xorg.1.log not found!")
            f.write('\n')

        if self.checks[3]:
            # print("Saving: pacman.log to file")
            f.write(HEADER.format("pacman.log", "searching for: pacsave, pacnew, pacorig keywords"))
            try:
                f.write(look_in_file('/var/log/pacman.log', ['pacsave', 'pacnew', 'pacorig']))
            except FileNotFoundError:
                print("/var/log/pacman.log not found, this is not Manjaro or Arch based Linux?")
                f.write("pacman.log not found!")
            f.write('\n')

        if self.checks[4]:
            # print("Saving: journalctl (mergency) to file")
            os.system("journalctl -b > /tmp/journalctl.txt")
            f.write(HEADER.format("journalctl.txt", "Searching for: Emergency keywords"))
            f.write(look_in_file('/tmp/journalctl.txt', ['emergency', 'Emergency', 'EMERGENCY']))
            f.write('\n')

        if self.checks[5]:
            # print("Saving: journalctl (alert) to file")
            os.system("journalctl -b > /tmp/journalctl.txt")
            f.write(HEADER.format("journalctl.txt", "Searching for: Alert keywords"))
            f.write(look_in_file('/tmp/journalctl.txt', ['alert', 'Alert', 'ALERT']))
            f.write('\n')

        if self.checks[6]:
            # print("Saving: journalctl (critical) to file")
            os.system("journalctl -b > /tmp/journalctl.txt")
            f.write(HEADER.format("journalctl.txt", "Searching for: Critical keywords"))
            f.write(look_in_file('/tmp/journalctl.txt', ['critical', 'Critical', 'CRITICAL']))
            f.write('\n')

        if self.checks[7]:
            # print("Saving: journalctl (failed) to file")
            os.system("journalctl -b > /tmp/journalctl.txt")
            f.write(HEADER.format("journalctl.txt", "Searching for: Failed keywords"))
            f.write(look_in_file('/tmp/journalctl.txt', ['failed', 'Failed', 'FAILED']))
            f.write('\n')

        f.close()

    def to_editor(self):
        os.system("xdg-open "+TMP_FILE)

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
