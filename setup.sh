#!/bin/bash

echo -e $'\e[1;91m\e[0m\e[1;91m\e[0m\e[1;96m\e[0m\e[1;91m   ----------------------------------------  \e[1;91m\e[0m'
echo -e $'\e[1;96m\e[0m\e[1;77m\e[0m\e[1;96m\e[0m\e[1;91m  !!         DOWNLOAD REQUIREMENTS         !!\e[0m'
echo -e $'\e[1;91m\e[0m\e[1;91m\e[0m\e[1;96m\e[0m\e[1;91m   ----------------------------------------- \e[1;91m\e[0m'

pkg update -y
pkg upgrade -y
pkg install git -y
pkg install python -y
pkg install figlet -y
sleep 1.0
clear
git clone https://github.com/Ak-Tools/FONTS
clear
cd FONTS
cp ASCII-Shadow.flf /data/data/com.termux/files/usr/share/figlet/

echo -e $'\e[1;91m\e[0m\e[1;91m\e[0m\e[1;96m\e[0m\e[1;91m   ----------------------------------------  \e[1;91m\e[0m'
echo -e $'\e[1;96m\e[0m\e[1;77m\e[0m\e[1;96m\e[0m\e[1;91m  !!         INSTALLATION COMPLETED         !!\e[0m'
echo -e $'\e[1;91m\e[0m\e[1;91m\e[0m\e[1;96m\e[0m\e[1;91m   ----------------------------------------- \e[1;91m\e[0m'
echo ""
echo NOW RUN THE start.sh file to run the tool
