# logs.py

Idea is, to collect different kind of error msgs from different log files on Linux system and display them all at the same time for easier troubleshooting.

For now, script works on Manjaro and probably on other Arch based Linux flavors that use systemd. I'm planning to modify script to make it also compatible with Debian based distributions. 

Before you use this script, you should run in terminal from your home: journalctl -b > journalctl.txt to pipe binary systemd log into journalctl.txt (journalctl -b > /path/to/your/home/journalctl.txt)

Right now, script parse these logs, with these key words:

    /var/log/Xorg.0.log <= failed, error, (WW)
    /var/log/Xorg.1.log <= failed, error, (WW)
    /var/log/pacman.log <= pacsave, pacnew, pacorig, warning    (Arch specific file)
    ~/journalctl.txt <= emergency, alert, critical, failed

It will work on Linux Mint but for now it will parse these two files only:

    /var/log/Xorg.0.log <= failed, error, (WW)
    ~/journalctl.txt <= emergency, alert, critical, failed
