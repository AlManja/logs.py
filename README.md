# mlogsqt4.py (Manjaro Logs)

    mlogsqt4.py runs on Python 3.6, needs: python-pyqt4, python-sh & xdg-utils

Idea is, to collect different kind of error msgs from different (txt) log files on Manjaro (it should probably work also on other Arch based systems) and display them all at the same time for easier troubleshooting. This should be something behinner friendly :-)

Script runs: journalctl -b > journalctl.txt (current systemd boot errors) and place it into your /tmp/ folder before it uses.

Select files/logs you want to search. 
If you select Inxi, make sure you have it installed :-)

For better control over the size of the output, journalctl is split into 4 searches each for each keyword: emergency, alert, critical, failed

    /var/log/Xorg.0.log <= failed, error, (WW)
    /var/log/pacman.log <= pacsave, pacnew, pacorig, warning    (Arch specific file)
    /tmp/journalctl.txt <= emergency, alert, critical, failed

On OpenRC system, it will search for 'WARNINGS' if you have logging enabled in rc.conf

Big thanks to:

https://github.com/xircon

https://github.com/novel-yet-trivial

https://www.reddit.com/user/K900_

For all the help on Reddit, Manjaro forum and here!

#![alt tag](https://raw.githubusercontent.com/AlManja/logs.py/master/mlogs02.png)
