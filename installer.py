
import os, time, subprocess
from sys import stdout
import sys
class colors:
    W  = '\033[0m'
    R  = '\033[31m'
    G  = '\033[32m'
    O  = '\033[33m'
    B  = '\033[34m'
    P  = '\033[35m'
    C  = '\033[36m'
    GR = '\033[40m'
    GY = '\033[43m'
    GE = '\033[41m'
    GW = '\033[4m'
    HH = '\033[1m'

def Command_exe(msg,cmd):
    i = "\033[1mSTATUS"+colors.W+":[Processing]"
    stdout.write(" " + msg + " %s" % i)
    stdout.flush()
    if subprocess.call(cmd+' >/dev/null 2>&1', shell=True)==0:
        i = "[\033[1m"+colors.G+"OK"+colors.W+"]"
    else:
        i = "["+colors.R+"\033[1mERROR"+colors.W+"]["+colors.O+"\033[1mWARNING"+colors.W+"]"
    stdout.write("\r " + msg +" STATUS:%s" % i)

class banner:
    logo = colors.G + """
                                                         `
                                                  `.:-  +yo`
                                                 .oohs/.hyy-
                                                 omhhssyy++.
                                                 omhyss+o+/
                                                 smdhdy+ss`
                                                 -mdyo++s:
                                        ..: -` `.+mdhsoo:`
                                        .:+:syyyhmmmdyso` `
                                     :::osyhdhhhyyhhdhyy+-:`
                                     -osyyhdyddys/++ohhyyyy/`
                                    /hyhmhhmhhdyo+//+sh+/++y+.
                                   :hhydhhmNmmmhsso/+ydo///shs.
                               `   yhyyhymmmmdddhhsoohmyso+sdy/
                              `:`.shyhyo.smmddydhdddddddhyydyhs.
                               :+hmyys-   ommdhydmdhysydydyddsy+
                               /hddsy`     ymdddddhdsoydhh+/mdys:
                               hyhdy/      `+mmmhhddyssssh: /ddds:`
                               dshys.        ydmdydhso++so` `hddhso`
                              `myss-         /mmmdhhsssyyo   .ohhhs+
                              :mys:          sddhdhdhhsoss`    /hhdy-
                              /mss          .dydddhdysooyy+     .shho
                              ymy/           yhhdmdhyyyhdhy.      +hd:
                              dmdo          +mdhdhdhssyhhhyo`      shs`
                             .mmds.        `mhddddyyhdhsyhyy`    `+hhy-
                             /mmdhy`       :dhhmddyshddhyhhs`    :dyhs.
                              :yddo        .dhhhmdshhhmdyhys.     +/+-
                               `o-         `mdhohdshymmmhyyh/
                                           smmyoohdyhNmmhhos/
                                           hddmsoyyhdNdmddos:
                                          .dmymhssho+mmdhdy+.
                                         `ydmsmhyho.`dmddhhs`
                                         odmdsmddy:  ommhhhs-
                                         ddmyhddhs.  .dmddhs.
                                        /mddydhyy`   .mNddd+
                                       :dmmhhdyy.    hmmdhy:
                                      /hmmdddhho    -mmmdhs:
                                      /mddmhhhh-    hmmddho`
                                      +mmmhddds    `mdmmhh:
                                      hmmddmmh/    `dmmmds`
                                     `dmddmddy.     ymmdd:
                                     .mmdmmdh/     .hmmdh-
                                    `oymddddh/     /dmmdhs-
                                     ++mdddhh/    `ymmmdhhh:`
                                     oymdddhh.    -mdmmdhdhyso:``
                                    /mmddddh+    -ymmdmmhyhhyyso+-
                                   -dmmdmddhs-  `-:oyoooohshys.
                                   ommdhmdhdhs-          :-
                                  -hdmddmdhydyy+`             ``
                                .+ysydhdddyhdyo/-.         .::::--`
                                    .++-ohsy::::-         .-:`````
                                        ..."""

print(banner.logo)

if os.getuid() != 0:
    print(" ["+colors.R+"-"+colors.W+"] ERROR:"+colors.B+" Install"+colors.B+" must be run as "+colors.R+"root"+colors.W+".")
    print(" ["+colors.R+"-"+colors.W+"] login as root ("+colors.R+"sudo"+colors.W+") or try "+colors.W+"sudo python4 installer.py"+colors.W+"\n")
    exit(1)

time.sleep(1)


print(colors.B   + """\n
1. ArchLinux
2. Debian/Ubuntu/Kali
3. Fedora
4. WSL Debian/Ubuntu
5. WSL Kali
""")
try:
    options = input("os > ")
    os.system('clear')
    worked = False
    if options == "1":
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing wine and winetricks.                    ",'pacman -S wine winetricks'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing android-tools-adb.                      ",'pacman -S android-tools-adb'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing android-tools-adb.                      ",'pacman -S android-tools-fastboot'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing other.                                  ",'pacman -S aircrack-ng telnet'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing python modules.                         ",'pip install -r requirements.txt --user'))
        worked = True
        if worked == True:
            print("Installation completed successfully! Starting DarkSpiritz..")
            os.system('python3 main.py')
    if options == "2":
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing wine and winetricks.                    ",'sudo apt-get install wine winetricks'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing android-tools-adb.                      ",'sudo apt-get install android-tools-adb'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing android-tools-adb.                      ",'sudo apt-get install android-tools-fastboot'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing other.                                  ",'sudo apt-get install aircrack-ng nmap telnet'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing python modules.                         ",'pip install -r requirements.txt --user'))
        worked = True
        if worked == True:
            print("Installation completed successfully! Starting DarkSpiritz..")
            os.system('python3 main.py')
    if options == "3":
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing wine and winetricks.                    ",'dnf wine winetricks'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing android-tools-adb.                      ",'dnf android-tools-adb'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing android-tools-adb.                      ",'dnf android-tools-fastboot'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing other.                                  ",'dnf aircrack-ng telnet'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing python modules.                         ",'pip install -r requirements.txt --user'))
        worked = True
        if worked == True:
            print("Installation completed successfully! Starting DarkSpiritz..")
            os.system('python3 main.py')
    if options == "4":
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing android-tools-adb.                      ",'sudo apt-get install android-tools-adb'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing android-tools-adb.                      ",'sudo apt-get install android-tools-fastboot'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing required tools.                         ",'sudo apt-get install aircrack-ng nmap telnet'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing python modules.                         ",'pip install -r requirements.txt --user'))
        worked = True
        if worked == True:
            print("Installation completed successfully! Starting DarkSpiritz..")
            os.system('python3 main.py')
    if options == "5":
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing android-tools-adb.                      ",'sudo apt-get install android-tools-adb'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing android-tools-adb.                      ",'sudo apt-get install android-tools-fastboot'))
        print(Command_exe("["+time.strftime('%H:%M:%S')+"] Installing python modules.                         ",'pip install -r requirements.txt --user'))
        worked = True
        if worked == True:
            print("Installation completed successfully! Starting DarkSpiritz..")
            os.system('python3 main.py')
    else:
        sys.exit()
except KeyboardInterrupt:
    sys.exit()
