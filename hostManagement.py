import traceback
import time
import os
activeHosts=[]

def addHost():
    hostAdres=input("Geef ip-adres van host op: ")
    activeHosts.append(hostAdres)
    writeHosts()

def removeHost():
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
    for i in range(0,len(activeHosts)):
        print(f"ip-adres host {i+1}: '{activeHosts[i]}'")

def showHostsInteractive():
    if len(activeHosts) !=0:
        showActiveHosts()
    else:
        print("Geen hosts in lijst.")
    input("Druk op enter om verder te gaan.")

def getActiveHosts():
    return activeHosts

def writeHosts():
    with open("hosts.txt","w") as hosts:
        temp = open("hosts.txt","w")
        temp.close()
        for i in range(0,len(activeHosts)):
            if i == 0:
                hosts.write(f"{activeHosts[i]}")
            else:
                hosts.write(f",{activeHosts[i]}")

def loadHosts():
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
