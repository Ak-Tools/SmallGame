#!/bin/bash
clear
figlet -f ASCII-Shadow A.K TOOLS | lolcat
sleep 0.5
echo -e "\e[96m        |-----------------------------------------------------|"
echo -e "\e[96m        |-------------------\e[92mSELECT OPTIONS\e[96m--------------------|"
echo -e "\e[96m        |-----------------------------------------------------|"
echo -e "\e[96m        |                                                     |"
echo -e "\e[96m        |                                                     |"
echo -e "\e[96m        |                                                     |"
echo -e "\e[96m        |                                                     |"
echo -e "\e[96m        |      [\e[92m1\e[96m]==> START GAME                              |"
echo -e "\e[96m        |      [\e[92m2\e[96m]==> CONTACT                                 |"
echo -e "\e[96m        |      [\e[92m3\e[96m]==> HELP                                    |"
echo -e "\e[96m        |      [\e[92m4\e[96m]==> EXIT                                    |"
echo -e "\e[96m        |                                                     |"
echo -e "\e[96m        |                                                     |"
echo -e "\e[96m        |                                                     |"
echo -e "\e[96m        |-----------------------------------------------------|"
echo -e "\e[96m        |-----------------------------------------------------|"
echo -e "\e[96m        |-----------------------------------------------------|"
read -p $'\n\e[1;96m[\e[0m\e[1;92m+\e[0m\e[1;96m] SELECT OPTION: \e[0m' option
if [[ $option == 1 || $option == 01 ]]; then
echo
clear
figlet -f ASCII-Shadow            A | lolcat
sleep 0.8
clear
figlet -f ASCII-Shadow            K | lolcat
sleep 0.8
clear
figlet -f ASCII-Shadow TOOLS | lolcat
sleep 0.8
clear
figlet -f ASCII-Shadow PRESENTS | lolcat
sleep 1.2
clear
figlet -f ASCII-Shadow M | lolcat && sleep 0.5 && figlet -f ASCII-Shadow A | lolcat && sleep 0.5 && figlet -f ASCII-Shadow D | lolcat && sleep 0.5 && figlet -f ASCII-Shadow L | lolcat && sleep 0.5 && figlet -f ASCII-Shadow I | lolcat && sleep 0.5 && figlet -f ASCII-Shadow B | lolcat && sleep 0.5 && figlet -f ASCII-Shadow S | lolcat 
sleep 0.5
clear
figlet -f ASCII-Shadow MAD LIBS | lolcat
sleep 1.0
clear
python main.py
fi
if [[ $option == 2 || $option == 02 ]]; then
echo -e "\e[96m MY EMAIL:- nocontact@gmail.com"
fi
if [[ $option == 3 || $option == 03 ]]; then
echo -e "\e[96m [ Simple to play. just complete the incomplete sentences.]"
fi
if [[ $option == 4 || $option == 04 ]]; then
printf "                    \e[1;96m GET LOST ........! \e[0m\n"
exit
fi

