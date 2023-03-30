import traceback
import time
import os
import json
activeHosts=[]

    
def addHost(hostAdres=""):
    if(hostAdres!=""):
        """This function is used to add automaticly a host from the list of active hosts"""
        valid = checkInputIP(hostAdres)
        if not valid:
            print("Geen geldig ip")
            exit()
        try:
            if hostAdres not in activeHosts:
                activeHosts.append(hostAdres)
        except:
            traceback.print_exc()
        writeHosts()
    else:
        hostAdres=input("Geef ip-adres van host op: ")
        valid = checkInputIP(hostAdres)
        if not valid:
            print("Geen geldig ip")
            time.sleep(0.5)
        else:
            if hostAdres not in activeHosts:
                activeHosts.append(hostAdres)
            writeHosts()

def checkInputIP(inputIP):
    segments=inputIP.split(".")
    validIp=True
    try:
        for segment in segments:
            if int(segment) < 0 or int(segment) > 255:
                validIp=False
        return validIp
    except:
        return False

def removeHost(hostAdres=""):
    if hostAdres!="":
        """This function is used to remove a host automaticly from the list of active hosts"""
        try:
            activeHosts.remove(hostAdres)
        except:
            traceback.print_exc()
        writeHosts()

    else:
        """This function is used to remove a host from the list of active hosts"""
        os.system("cls||clear")
        if (len(activeHosts)!=0):
            showActiveHosts()
            numberOfHost=int(input("Geef nummer van host op: "))
            try:
                del activeHosts[numberOfHost-1]
                writeHosts()
            except IndexError:
                print("Nummer kwam niet voor in lijst.")
                time.sleep(0.5)
            except:
                traceback.print_exc()
        else:
            print("Geen hosts in lijst.")
            time.sleep(0.5)

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
    with open("hosts.json","w") as hosts:
        json.dump(activeHosts, hosts)

    
def loadHosts():
    """This function is used to load the active hosts from a file"""
    global activeHosts
    try:
        with open("hosts.json","r") as hosts:
            activeHosts=json.load(hosts)
    except FileNotFoundError:
        activeHosts=[]
    except json.decoder.JSONDecodeError:
        activeHosts=[]