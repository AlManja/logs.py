#!/usr/bin/env python

import os

"""
This script prints out some computer info and errors from log files (Xorg.0.log, Xorg.1.log,
pacman.log, journalctl.txt and rc.log. It is intended for Linux OS (Arch based: Manjaro)
"""


def inxi():
    print()
    print('==================')
    print('| inxi -Fxmnxopz |   Need password! Listing computer information')
    print('==================')
    try:
        os.system('sudo inxi -Fxmnxopz')
        print()
    except:
        print('Do you have installed: "inxi" on your system? ')


def mhwd_li():
    print('===============')
    print('|   mhwd -li  |   Shows which graphic driver is installed')
    print('===============')
    try:
        os.system('mhwd -li')
        print()
    except:
        print('Do you have installed: "mhwd" on your system? ')


def mhwd_l():
    print('===============')
    print("|   mhwd -l  |   List of all drivers supported on detected gpu's")
    print('===============')
    try:
        os.system('mhwd -l')
    except:
        print('Do you have installed: "mhwd" on your system? ')


def direct_rendering():
    print()
    print('====================')
    print('| Direct Rendering |   Yes/No')
    print('====================')
    try:
        os.system('glxinfo | grep "direct rendering"')
        print()
    except:
        print(' No "glxinfo" on your system? ')


def hwinfo_gfxcard():
    print('====================')
    print("| hwinfo --gfxcard |   Detailed info about your graphic card.")
    print('====================')
    try:
        os.system('hwinfo --gfxcard')
        print()
        print()
    except:
        print('Do you have installed: "mhwd" on your system? ')


def lsblk():
    print('=============')
    print("|   lsblk   |   List drives and partitions")
    print('=============')
    os.system('lsblk')
    print()


def check_bios():
    print('=============')
    print("| parted -l |   Need password!   Checking if system is miss configured")
    print('=============')
    print(' Output need to match one of these two pairs: BIOS-msdos or UEFI-gpt')
    print(" -------------------- ")
    os.system('test -d /sys/firmware/efi && echo UEFI || echo BIOS')
    os.system('sudo parted -l | grep "Partition Table"')
    print(" -------------------- ")
    print()


def read_xorg0():
    """from Xorg.0.log print lines that contain words: failed, error, (WW)"""
    try:
        with open('/var/log/Xorg.0.log', 'r') as f:
            print('==============')
            print('| Xorg.0.log |  "Xorg.0.log", Listing entries with failed, error & (WW) keywords')
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
            print('| Xorg.1.log |  "Xorg.1.log", Listing entries with failed, error & (WW) keywords')
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
            print('| pacman.log |   Listing entries with pacsave, pacnew, pacorig keywords')
            print('==============')
            for line in f:
                if 'pacsave' in line or 'pacnew' in line or 'pacorig' in line or 'warning' in line:
                    print(line, end='')
        print()
    except:
        print('Missing file: pacman.log   This is not Arch based distribution?')


def read_journalctl():
    print('==============')
    print('| journalctl |   (systed only!) - Listing entries with Emergency, Alert & Critical keywords')
    print('==============')
    key_word = ['emergency', 'Emergency', 'EMERGENCY', 'alert', 'Alert', 'ALERT', 'critical', 'Critical',
                'CRITICAL']
    os.system("journalctl -b > /tmp/journalctl.txt")
    try:
        with open('/tmp/journalctl.txt', 'r') as f:
            for line in f:
                for word in key_word:
                    if word in line:
                        print(line, end='')
    except:
        print('Missing file: journalctl.txt;  Not systed based system?')
    print()


def read_rc_log():
    print('==============')
    print('|   rc.log   |   (OpenRC only!) - Listing entries with WARNING: keywords')
    print('==============')
    try:
        with open('/var/log/rc.log', 'r') as f:
            for line in f:
                if 'WARNING:' in line:
                    print(line, end='')
        print()
    except:
        print('Missing file: rc.log   If this is OpenRC, did you enable logging?')


def rc_status():
    print('===============')
    print('|  rc_status  |   (OpenRC only!) - Lists all services "rc-status --all" ')
    print('===============')
    try:
        os.system('rc-status --all')
        print()
    except:
        print('Is this OpenRC init based system?')


# -------------------
# test -d /sys/firmware/efi && echo UEFI || echo BIOS  <= run first
# parted -l | grep "Partition Table"                   <= run second
# -------------------

inxi()
mhwd_li()
mhwd_l()
direct_rendering()
hwinfo_gfxcard()
read_xorg0()
read_xorg1()
lsblk()
check_bios()
read_journalctl()
read_pacman()
rc_status()
read_rc_log()