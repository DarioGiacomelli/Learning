#!/usr/bin/python



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
            

def choice(menuChoice):
    if menuChoice == 1:
        print("Starting HTB.vpn")
        HTBVpn()
    else:
        print("You did not choose '1'")
        

def HTBVpn():
    print("This is where I would put my code... If I had any")

menu()