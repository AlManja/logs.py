#!/usr/bin/env python

# todo: added memory & swap info

import os

"""
This script prints out some computer info and errors from log files (Xorg.0.log, Xorg.1.log,
pacman.log, journalctl.txt and rc.log. It is intended for Linux OS (Arch based: Manjaro)
"""


def inxi():
    print()
    print('===============')
    print('| Inxi -Fxxxz |   Computer information')
    print('===============')
    try:
        os.system('inxi -Fxxxz')
        print()
    except:
        print('Do you have installed: "inxi" on your system? ')


def mhwd_li():
    print('===============')
    print('|   mhwd -li  |   Shows which graphic drivers are installed')
    print('===============')
    try:
        os.system('mhwd -li')
        print()
    except:
        print('Do you have installed: "mhwd" on your system? ')


def mhwd_l():
    print('==============')
    print("|   mhwd -l  |   List of all drivers supported on detected gpu's")
    print('==============')
    try:
        os.system('mhwd -l')
    except:
        print('Do you have installed: "mhwd" on your system? ')


def hwinfo_gfxcard():
    print('====================')
    print("| hwinfo --gfxcard |   Info about your graphic card.")
    print('====================')
    try:
        os.system('hwinfo --gfxcard')
        print()
        print()
    except:
        print('Do you have installed: "mhwd" on your system? ')


def mem():
    print('=============')
    print("|  free -h  |   Shows memory and swap info")
    print('=============')
    os.system('free -h')
    print()


def lsblk():
    print('=============')
    print("|   lsblk   |   List drives and partitions")
    print('=============')
    os.system('lsblk')
    print()


def df():
    print('==========')
    print("|   df   |   How much free disk space is left for each partition?")
    print('==========')
    os.system('df')
    print()


def blockdev():
    print('==++========')
    print("| blockdev |   Checks your first (sda) disk, if 0, alignment is OK")
    print('=========++=')
    os.system('blockdev --getalignoff /dev/sda')
    print()


def check_bios():
    ''' 
    entter explanation here :-)
    '''
    print('=============')
    print("| parted -l |   Installation mach partition table type?")
    print('=============')
    print(' Output need to match one of these two pairs: BIOS+msdos or UEFI+gpt')
    print(" -------------------- ")
    os.system('test -d /sys/firmware/efi && echo UEFI || echo BIOS')
    os.system('parted -l | grep "Partition Table: "')
    print(" -------------------- ")
    print()


def read_xorg0():
    """from Xorg.0.log print lines that contain words: failed, error, (WW)"""
    try:
        with open('/var/log/Xorg.0.log', 'r') as f:
            print('==============')
            print('| Xorg.0.log |  "Xorg.0.log", Lists entries with failed, error & (WW) keywords')
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
            print('| Xorg.1.log |  "Xorg.1.log", Lists entries with failed, error & (WW) keywords')
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
            print('| pacman.log |   Lists entries with pacsave, pacnew, pacorig keywords')
            print('==============')
            for line in f:
                if 'pacsave' in line or 'pacnew' in line or 'pacorig' in line or 'warning' in line:
                    print(line, end='')
        print()
    except:
        print('Missing file: pacman.log   This is not Arch based distribution?')


def read_journalctl():
    print('==============')
    print('| journalctl |   Lists entries with Emergency, Alert & Critical keywords - (systemd only)')
    print('==============')
    key_word = ['emergency', 'Emergency', 'EMERGENCY', 'alert', 'Alert', 'ALERT', 'critical', 'Critical', 'CRITICAL']
    # key_word = ['error', 'Error', 'ERROR', 'emergency', 'Emergency', 'EMERGENCY', 'alert', 'Alert', 'ALERT',
    #             'critical', 'Critical', 'CRITICAL']
    os.system("journalctl -b > /tmp/journalctl.txt")
    try:
        with open('/tmp/journalctl.txt', 'r') as f:
            for line in f:
                for word in key_word:
                    if word in line:
                        print(line, end='')
    except:
        print('Missing file: journalctl.txt;  Not systemd based system?')
    print()


def read_rc_log():
    print('==============')
    print('|   rc.log   |   Lists entries with WARNING: keywords - (OpenRC only, logging need to be enabled)')
    print('==============')
    try:
        with open('/var/log/rc.log', 'r') as f:
            for line in f:
                if 'WARNING:' in line:
                    print(line, end='')
        print()
    except:
        print('Missing file: rc.log   If this is OpenRC with logging enabled?')


def rc_status():
    print('===============')
    print('|  rc_status  |   Lists all services "rc-status --all" - (OpenRC only, logging need to be enabled)')
    print('===============')
    try:
        os.system('rc-status --all')
        print()
    except:
        print('Is this OpenRC init based system?')

inxi()
mhwd_li()
mhwd_l()
hwinfo_gfxcard()
read_xorg0()
read_xorg1()
mem()
lsblk()
df()
blockdev()
check_bios()
read_journalctl()
read_pacman()
rc_status()
read_rc_log()
