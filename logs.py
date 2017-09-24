#!/usr/bin/env python

'''added dmesg_error & dmesg_fail, sept 26, 2017'''

import os

"""
This script prints out some computer info and errors from log files (Xorg.0.log, Xorg.1.log,
pacman.log and journalctl.txt. It is intended for Linux OS (Arch based: Manjaro)
"""


def inxi():
    """ Return some basic information about computer hardware, OS, software... """
    print()
    print('===============')
    print('| Inxi -Fxxxz |   Computer information')
    print('===============')
    try:
        os.system('inxi -Fxxxz')
        print()
    except:
        print('Do you have installed: "inxi" on your system? ')


def dmesg_error():
    print('======================')
    print('| dmesg | grep error |   Shows kernel errors')
    print('======================')
    try:
        os.system('dmesg | grep error')
        print()
    except:
        print('Nea working...')


def dmesg_fail():
    print('======================')
    print('| dmesg | grep error |   Shows kernel fails')
    print('======================')
    try:
        os.system('dmesg | grep fail')
        print()
    except:
        print('Nea working...')


def mhwd_li():
    """ Installed graphic drivers """
    print('===============')
    print('|   mhwd -li  |   Shows which graphic drivers are installed')
    print('===============')
    try:
        os.system('mhwd -li')
        print()
    except:
        print('Do you have installed: "mhwd" on your system? ')


def mhwd_l():
    """ Drivers supported on detected gpu's """
    print('==============')
    print("|   mhwd -l  |   List of all drivers supported on detected gpu's")
    print('==============')
    try:
        os.system('mhwd -l')
    except:
        print('Do you have installed: "mhwd" on your system? ')


def hwinfo_gfxcard():
    """ Info about installed graphic card """
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
    """ Info about memory and swap partition """
    print('=============')
    print("|  free -h  |   Shows memory and swap info")
    print('=============')
    os.system('free -h')
    print()


def lsblk():
    """ Info about drives and partitions """
    print('=============')
    print("|   lsblk   |   List drives and partitions")
    print('=============')
    os.system('lsblk')
    print()


def df():
    """ Info about remaining free space on partitions """
    print('==========')
    print("|   df   |   How much free disk space is left for each partition?")
    print('==========')
    os.system('df')
    print()


def blockdev():
    """ returns 0 is partitions on first HDD are properly aligned """
    print('============')
    print("| blockdev |   Checks your first (sda) disk, if 0, alignment is OK")
    print('============')
    os.system('blockdev --getalignoff /dev/sda')
    print()


def check_bios():
    """ Checks if installatuon type matches partition table type """
    print('=============')
    print("| parted -l |   Installation match partition table type?")
    print('=============')
    print(' Output need to match one of these two pairs: BIOS+msdos or UEFI+gpt')
    print(" -------------------- ")
    os.system('test -d /sys/firmware/efi && echo UEFI || echo BIOS')
    os.system('parted -l | grep "Partition Table: "')
    print(" -------------------- ")
    print()


def read_xorg0():
    """ from Xorg.0.log print lines that contain words: failed, error, (WW) """
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
    """ from Xorg.1.log print lines that contain words: failed, error, (WW) """
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


def orphaned():
    """ Installed graphic drivers """
    print('===============')
    print('|  pacman -Qdtq  |   Lists orphaned packages')
    print('===============')
    try:
        os.system('pacman -Qdtq')
        print()
    except:
        print('Not Arch based ditribution?')


def read_pacman():
    """ from pacman.log print lines that contain words: pacsave, pacnew, pacorig, warning """
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
    """ Lists lines that contain keywords: emergency, alert and critical """
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


inxi()
dmesg_error()
dmesg_fail()
mhwd_li()
mhwd_l()
hwinfo_gfxcard()
mem()
lsblk()
df()
blockdev()
check_bios()
read_xorg0()
read_xorg1()
read_journalctl()
orphaned()
read_pacman()
print('... finished :-)')
