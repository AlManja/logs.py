# mlogs.py (Manjaro Logs)

    mlogs.py    (PyQt5)
    mlogsqt4.py (PyQt4)

Idea is, to collect different kind of error msgs from different (txt) log files on Linux system and display them all at the same time for easier troubleshooting. This should be something behinner friendly :-)

Currently, I'm making script for Manjaro Linux (Arch based)
I would be happy to add more log searches for different Linux distributions if I get following information:

1 - path to that log file
2 - what keywords to search for

Script runs: journalctl -b > journalctl.txt (current systemd boot errors) and place it into your /tmp/ folder before it uses.

For now, search keywords are hardcoded.
Select files/logs you want to search. 
If you select Inxi, make sure you have it installed :-)

For better control over output, journalctl is split into 4 searches each for each keyword: emergency, alert, critical, failed

    /var/log/Xorg.0.log <= failed, error, (WW)
    /var/log/Xorg.1.log <= failed, error, (WW)
    /var/log/pacman.log <= pacsave, pacnew, pacorig, warning    (Arch specific file)
    /tmp/journalctl.txt <= emergency, alert, critical, failed

On Linux Mint it parse these two files:

    /var/log/Xorg.0.log <= failed, error, (WW)
    /tmp/journalctl.txt <= emergency, alert, critical, failed

[mlogs.png]


