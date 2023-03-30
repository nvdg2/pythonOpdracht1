import traceback
import time
import os
activeHosts=[]

def addHost():
    """This function is used to add a host to the list of active hosts"""
    hostAdres=input("Geef ip-adres van host op: ")
    activeHosts.append(hostAdres)
    writeHosts()

def removeHost():
    """This function is used to remove a host from the list of active hosts"""
    os.system("cls||clear")
    showActiveHosts()
    numberOfHost=int(input("Geef nummer van host op: "))
    try:
        
        del activeHosts[numberOfHost-1]
    except IndexError:
        print("Nummer kwam niet voor in lijst.")
        time.sleep(0.5)
    except:
        traceback.print_exc()
    writeHosts()

def showActiveHosts():
    """This function is used to show the active hosts"""
    for i in range(0,len(activeHosts)):
        print(f"ip-adres host {i+1}: '{activeHosts[i]}'")

def showHostsInteractive():
    """This function is used to show the active hosts in an interactive way"""
    if len(activeHosts) !=0:
        showActiveHosts()
    else:
        print("Geen hosts in lijst.")
    input("Druk op enter om verder te gaan.")

def getActiveHosts():
    """This function is used to return the list of active hosts"""
    return activeHosts

def writeHosts():
    """This function is used to write the active hosts to a file"""
    with open("hosts.txt","w") as hosts:
        temp = open("hosts.txt","w")
        temp.close()
        for i in range(0,len(activeHosts)):
            if i == 0:
                hosts.write(f"{activeHosts[i]}")
            else:
                hosts.write(f",{activeHosts[i]}")

def loadHosts():
    """This function is used to load the active hosts from a file"""
    global activeHosts
    try:
        with open("hosts.txt","r") as hosts:
            while True:
                line = hosts.readline()
                if len(line)==0:
                    break
                else:
                    activeHosts =line.split(",")
    except FileNotFoundError:
        hosts = open("hosts.txt","w")
        hosts.close()