import random
import os
import sys
from os import system
clear = lambda: os.system('cls')
addRed=False
os.system('color ' +'c'+ " & cls & title Hosts Editor V0.5")
print("[INFO] https://github.com/hum4not")
print('''
        ██╗░░██╗██╗░░░██╗███╗░░░███╗░█████╗░███╗░░██╗░█████╗░████████╗
        ██║░░██║██║░░░██║████╗░████║██╔══██╗████╗░██║██╔══██╗╚══██╔══╝
        ███████║██║░░░██║██╔████╔██║███████║██╔██╗██║██║░░██║░░░██║░░░
        ██╔══██║██║░░░██║██║╚██╔╝██║██╔══██║██║╚████║██║░░██║░░░██║░░░
        ██║░░██║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║╚█████╔╝░░░██║░░░
        ╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░
''')
firstask = input("1) Add ip\n2) Check hosts\n3) Clear hosts\n\n[You]: ")

def idotnub():
        firstask = input("1) Add ip\n2) Check hosts\n3) Clear hosts\n\n[You]: ")

def logmenu():
        os.system('color ' +'c'+ " & cls & title Hosts Editor V0.5")
        print("[INFO] https://github.com/hum4not")
        print('''
        ██╗░░██╗██╗░░░██╗███╗░░░███╗░█████╗░███╗░░██╗░█████╗░████████╗
        ██║░░██║██║░░░██║████╗░████║██╔══██╗████╗░██║██╔══██╗╚══██╔══╝
        ███████║██║░░░██║██╔████╔██║███████║██╔██╗██║██║░░██║░░░██║░░░
        ██╔══██║██║░░░██║██║╚██╔╝██║██╔══██║██║╚████║██║░░██║░░░██║░░░
        ██║░░██║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║╚█████╔╝░░░██║░░░
        ╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░
        ''')
        idotnub()

if firstask == "1":
        togo = input("[SYSTEM] Server ip: ")
        with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'r') as file:
                if togo + "growtopia1.com" in file.read():
                        print("[SYSTEM] Hosts already has '" + togo + "'!")
                        input("[SYSTEM] Press ENTER to go back")
                        clear()
                        logmenu()
                else:
                        addRed=True;
                        file.close()
                if addRed:
                        with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'a') as file:
                                file.write('\n' + togo + ' growtopia1.com')
                                file.write('\n' + togo + ' growtopia2.com')
                        print("[SYSTEM] Hosts was added!")
                        file.close()
                        input("[SYSTEM] Press ENTER to go back")
                        clear()
                        logmenu()

if firstask == "2":
        with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'r') as file:
                print("==============================")
                print(file.read())
                print("==============================")
                input("[SYSTEM] Press ENTER to go back")
                clear()
                logmenu()
if firstask == "3":
        file = open("C:\\Windows\\System32\\drivers\\etc\\hosts","r+")
        file. truncate(0)
        print("==============================")
        print("[SYSTEM] OUTPUT: \n" + file.read())
        print("==============================")
        file.close()
        input("[SYSTEM] Press ENTER to go back")
        clear()
        logmenu()
