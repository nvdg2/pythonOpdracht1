import traceback
import time
import os
activeHosts=[]

def addHost():
    hostAdres=input("Geef ip-adres van host op: ")
    activeHosts.append(hostAdres)
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

def showActiveHosts():
    for i in range(0,len(activeHosts)):
        print(f"ip-adres host {i+1}: {activeHosts[i]}")
def showHostsInteractive():
    if len(activeHosts) !=0:
        showActiveHosts()
    else:
        print("Geen hosts in lijst.")
    input("Druk op enter om verder te gaan.")

