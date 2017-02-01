# mlogs.py (Manjaro Logs)

logs.py is cli
mlogs.py is GUI (PyQt5)

Idea is, to collect different kind of error msgs from different (txt) log files on Linux system and display them all at the same time for easier troubleshooting. This should be something behinner friendly :-)

Currently, I'm making script for Manjaro Linux (Arch based)
I would be happy to add more log searches for different Linux distributions if I get following information:

1 - path to that log file
2 - what keywords to search for

Before you use this script, you should run in terminal from your home: journalctl -b > journalctl.txt to pipe binary systemd log into journalctl.txt (journalctl -b > /path/to/your/home/journalctl.txt)

Right now, this script on Manjaro parse these 4 logs, with these key words:

    /var/log/Xorg.0.log <= failed, error, (WW)
    /var/log/Xorg.1.log <= failed, error, (WW)
    /var/log/pacman.log <= pacsave, pacnew, pacorig, warning    (Arch specific file)
    ~/journalctl.txt <= emergency, alert, critical, failed

On Linux Mint it parse these two files:

    /var/log/Xorg.0.log <= failed, error, (WW)
    ~/journalctl.txt <= emergency, alert, critical, failed
