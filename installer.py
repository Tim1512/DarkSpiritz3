
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

print banner.logo

if os.getuid() != 0:
    	print(" ["+colors.R+"-"+colors.W+"] ERROR:"+colors.B+" Install"+colors.B+" must be run as "+colors.R+"root"+colors.W+".")
	print(" ["+colors.R+"-"+colors.W+"] login as root ("+colors.R+"sudo"+colors.W+") or try "+colors.W+"sudo python installer.py"+colors.W+"\n")
	exit(1)

time.sleep(1)
print(Command_exe("["+time.strftime('%H:%M:%S')+"] Making python2 as default.                 ",'mv /usr/bin/python2 /usr/bin/python'))
print(Command_exe("["+time.strftime('%H:%M:%S')+"] Fixing python3.                 ",'mv /usr/bin/python3 /usr/bin/python3'))


print(colors.B   + """\n)
1. ArchLinux
2. Debian/Ubuntu/Kali
3. Fedora
4. WSL Debian/Ubuntu/Kali (Some plugins may not work correctly. A VM would be optimal)
"""
try:
    options = raw_input("os > ")
    os.system('clear')
    worked = False
    if options == "1":
        print()
