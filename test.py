#!/usr/bin/python
import os
import subprocess

#Show menu
def menu():
    while True:
        print("*" * 30)
        print("HTB Recon Assistant")
        print("*" * 30)
        print ("1. Start HTB VPN")
        print ("2. Create HTB Folder")
        print ("3. Run Nmap")
        print ("-" * 30)

        try:
            menuChoice = int(input("Choose an option: \n"))
        except ValueError:
            print("Choose an option from the list above.")
            continue
        else:
            choice(menuChoice)
            
# MenuItems
def choice(menuChoice):
    if menuChoice == 1:
        print("Starting HTB.vpn")
        HTBVpn()
    elif menuChoice == 2:
        print("Making HTB folder")
        machine = raw_input("enter machinename: ")
        mkdirHTB(machine, ip)
    elif menuChoice == 3:
        print("Run Nmap")
        ip = raw_input("enter IP address: " )
        nmap(ip)
    else:
        print("You did not choose a valid option")

# Functions
def HTBVpn():
    print("This is where I would put my code... If I had any")

def mkdirHTB(machine, ip):
    path = os.path.expanduser("~/HTB/Machines/")
    folder = path + machine + "/"

    try:
        os.mkdir(folder)
    except  OSError:
        print("Creation failed")
    else:
        print("created folder " + folder)
        print("making Nmap folder")
        nmapfolder = folder + "nmap/"

        try:
            os.mkdir(nmapfolder)
        except OSError:
            print("Creation failed")
        else:
            print("created folder" + nmapfolder)
            wait = raw_input("Press any key to return to main menu\n")

def nmap(ip):
    print("This is where I would put my code... If I had any")

#Call MainMenu
menu()