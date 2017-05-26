#!/usr/bin/env python

import os
import sys                           # provides interaction with the Python interpreter
from functools import partial
from PyQt4 import QtGui              # provides the graphic elements
from PyQt4.QtCore import Qt          # provides Qt identifiers
from PyQt4.QtGui import QPushButton
try:
    from sh import inxi
except:
    print(" 'inxi' not found, install it to get this info")
try:
    from sh import mhwd
except:
    print(" 'mhwd' not found, this is not Manjaro?")
try:
    from sh import hwinfo
except:
    print(" 'hwinfo' not found")
try:
    from sh import free
except:
    print(" 'free' not found")
try:
    from sh import lsblk
except:
    print(" 'lsblk' not found")
try:
    from sh import df
except:
    print(" 'df' not found")
try:
    from sh import blockdev
except:
    print(" 'blockdev' not found")
try:
    from sh import test
except:
    print(" 'test' not found")
try:
    from sh import parted
except:
    print(" 'parted' not found")

TMP_FILE = "/tmp/mlogsout.txt"

HEADER = '''
===================
|{:^17}|   {}
===================
'''

checkbuttons = [
    'Inxi',
    'Installed g. drivers',
    'List all g. drivers',
    'Graphic Card Info',
    'Memory Info',
    'Partitions',
    'Free Disk Space',
    'Xorg.0',
    'Xorg.1',
    'pacman.log',
    'journalctl - Emergency',
    'journalctl - Alert',
    'journalctl - Critical',
    'journalctl - Failed',
    'Open&Rc - rc.log',
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

        btn = QPushButton("&Show Info ({})".format(TMP_FILE), self)
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
            print("Saving: inxi to file")
            f.write(HEADER.format("Inxi -Fxzc0", "Listing computer information"))
            try:
                f.write(str(inxi('-Fxxxzc0')))
            except:
                " 'inxi' not found, install it to get this info"
            f.write('\n')

        if self.checks[1]:
            print("Getting info about installed graphical driver")
            f.write(HEADER.format("Installed drivers", "Shows which graphic driver is installed"))
            try:
                f.write(str(mhwd('-li')))
            except:
                print(" 'mhwd' not found, this is not Manjaro?")
            f.write('\n')

        if self.checks[2]:
            print("Getting list of all drivers supported on detected gpu's")
            f.write(HEADER.format("Available drivers", "list of all drivers supported on detected gpu's"))
            try:
                f.write(str(mhwd('-l')))
            except:
                print(" 'mhwd' not found, this is not Manjaro?")
            # f.write('\n')

        if self.checks[3]:
            print('hwinfo -graphic card')
            # os.system('hwinfo --gfxcard')
            f.write(HEADER.format("hwinfo --gfxcard", "Show Graphic Card info"))
            try:
                f.write(str(hwinfo('--gfxcard')))
            except:
                print('hwinfo graphic card info error')
                f.write('hwinfo graphic card info error')
            f.write('\n')

        if self.checks[4]:
            print('memory info')
            # os.system('free -h')
            f.write(HEADER.format("Memory Info", "Info about Memory and Swap"))
            try:
                f.write(str(free(' -h')))
            except:
                print('memory info error')
                f.write('memory info error')
            f.write('\n')

        if self.checks[5]:
            print('disk info')
            # os.system('lsblk')
            f.write(HEADER.format("Disk Info", "Disks and Partitions"))
            try:
                f.write(str(lsblk()))
            except:
                print('lsblk error')
                f.write('lsblk error')
            f.write('\n')

        if self.checks[6]:
            print('free disk space')
            # os.system('df')
            f.write(HEADER.format("Free Disk Space", "Free space per pertition"))
            try:
                f.write(str(df()))
            except:
                print('free disk space error')
                f.write('free disk space error')
            f.write('\n')

        if self.checks[9]:
            print("Saving: Xorg.0.log to file")
            f.write(HEADER.format("Xorg.0.log", "searching for: failed, error & (WW) keywords"))
            try:
                f.write(look_in_file('/var/log/Xorg.0.log', ['failed', 'error', '(WW)']))
            except FileNotFoundError:
                print("/var/log/Xorg.0.log not found!")
                f.write("Xorg.0.log not found!")
            f.write('\n')

        if self.checks[10]:
            print("Saving: Xorg.1.log to file")
            f.write(HEADER.format("Xorg.1.log", "searching for: failed, error & (WW) keywords"))
            try:
                f.write(look_in_file('/var/log/Xorg.1.log', ['failed', 'error', '(WW)']))
            except FileNotFoundError:
                print("/var/log/Xorg.1.log not found!")
                f.write("Xorg.1.log not found!")
            f.write('\n')

        if self.checks[11]:
            print("Saving: pacman.log to file")
            f.write(HEADER.format("pacman.log", "searching for: pacsave, pacnew, pacorig keywords"))
            try:
                f.write(look_in_file('/var/log/pacman.log', ['pacsave', 'pacnew', 'pacorig']))
            except FileNotFoundError:
                print("/var/log/pacman.log not found, this is not Manjaro or Arch based Linux?")
                f.write("pacman.log not found!  Not Arch based OS?")
            f.write('\n')

        if self.checks[12]:
            print("Saving: journalctl (emergency) to file")
            os.system("journalctl -b > /tmp/journalctl.txt")
            f.write(HEADER.format("journalctl.txt", "Searching for: Emergency keywords"))
            f.write(look_in_file('/tmp/journalctl.txt', ['emergency', 'Emergency', 'EMERGENCY']))
            f.write('\n')

        if self.checks[13]:
            print("Saving: journalctl (alert) to file")
            os.system("journalctl -b > /tmp/journalctl.txt")
            f.write(HEADER.format("journalctl.txt", "Searching for: Alert keywords"))
            f.write(look_in_file('/tmp/journalctl.txt', ['alert', 'Alert', 'ALERT']))
            f.write('\n')

        if self.checks[14]:
            print("Saving: journalctl (critical) to file")
            os.system("journalctl -b > /tmp/journalctl.txt")
            f.write(HEADER.format("journalctl.txt", "Searching for: Critical keywords"))
            f.write(look_in_file('/tmp/journalctl.txt', ['critical', 'Critical', 'CRITICAL']))
            f.write('\n')

        if self.checks[15]:
            print("Saving: journalctl (failed) to file")
            os.system("journalctl -b > /tmp/journalctl.txt")
            f.write(HEADER.format("journalctl.txt", "Searching for: Failed keywords"))
            f.write(look_in_file('/tmp/journalctl.txt', ['failed', 'Failed', 'FAILED']))
            f.write('\n')

        if self.checks[16]:
            print("Saving: rc.log to file")
            f.write(HEADER.format("rc.log", "OpenRc only! searching for: WARNING: keywords"))
            try:
                f.write(look_in_file('/var/log/rc.log', ['WARNING:']))
            except FileNotFoundError:
                print("/var/log/rc.log not found!     Systemd based OS?")
                f.write("rc.log not found!   Systemd based OS?")
            f.write('\n')

        f.close()

    def to_editor(self):
        os.system("xdg-open "+TMP_FILE)

# creates the application and takes arguments from the command line
application = QtGui.QApplication(sys.argv)

# creates the window and sets its properties
window = Window()
window.setWindowTitle('Manjaro Logs')  # title
window.resize(280, 50)  # size
window.show()  # shows the window

# runs the application and waits for its return value at the end
sys.exit(application.exec_())
