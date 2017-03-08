# logsgui.py (Manjaro Logs)

    logsgui.py runs on Python 3.6, needs: python-pyqt4, python-sh & xdg-utils

Idea is, to collect different kind of computer info and error msgs from different log files on Arch based Manjaro Linux and display them all at the same time for easier troubleshooting. It is meant to help with troubleshoting in a simple and beginner friendly way :-).

Script also works on Arch linux, but since it also uses "mhwd" - Manjaro hardware detection tool, which is not awailable in Arch repositories, this part will of course not return any info. 

On Systemd based systems, script runs: journalctl -b > journalctl.txt (current systemd boot errors) and place it into your /tmp/ folder before it uses.
On OpenRC based systems, it will search for 'WARNINGS' if you have logging enabled in rc.conf

Select files/logs you want to search. If you select Inxi, make sure you have it installed :-)

For better control over the size of the output, journalctl is split into 4 searches each for each keyword: emergency, alert, critical, failed

    /var/log/Xorg.0.log <= failed, error, (WW)
    /var/log/pacman.log <= pacsave, pacnew, pacorig, warning    (Arch specific file)
    /tmp/journalctl.txt <= emergency, alert, critical, failed

Big thanks to:

https://github.com/xircon

https://github.com/novel-yet-trivial

https://www.reddit.com/user/K900_

For all the help on Reddit, Manjaro forum and here!

And to @Photon for packaking and adding it to AUR:

https://forum.manjaro.org/users/photon/activity

#![alt tag](https://raw.githubusercontent.com/AlManja/logs.py/master/mlogs02.png)
