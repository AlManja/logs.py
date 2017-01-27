# logs.py

Idea is, to collect different kind of error msgs from different log files on Linux system

For now, script works on Manjaro and probably on other Arch based Linux flavors that use systemd. I'm planning to modify script to make it also compatible with Debian based distributions. 

Before you use this script, you should run in terminal: journalctl > journalctl.txt to pipe binary systemd log into journalctl.txt

Right now, script parse these logs, with these key words:

    /var/log/Xorg.0.log <= failed, error, (WW)
    /var/log/Xorg.1.log <= failed, error, (WW)
    /var/log/pacman.log <= pacsave, pacnew, pacorig, warning    (Arch specific file)
    ~/journalctl.txt <= emergency, alert, critical, failed

