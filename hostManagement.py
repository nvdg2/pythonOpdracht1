import traceback
import time
import os
import json

from rich.console import Console
from rich.prompt import Prompt
from rich.traceback import Traceback
console = Console()

activeHosts=[]
def addHost(hostAdres=""):
    if(hostAdres!=""):
        """This function is used to add automatically a host from the list of active hosts"""
        valid = checkInputIP(hostAdres)
        if not valid:
            console.print("Geen geldig ip")
            exit()
        try:
            if hostAdres not in activeHosts:
                activeHosts.append(hostAdres)
        except:
            console.print(Traceback())
        writeHosts()
    else:
        hostAdres=Prompt.ask("Geef ip-adres van host op")
        valid = checkInputIP(hostAdres)
        if not valid:
            console.print("[bold red]Geen geldig ip[/bold red]")
            time.sleep(1)
        else:
            if hostAdres not in activeHosts:
                activeHosts.append(hostAdres)
            writeHosts()

def checkInputIP(inputIP):
    segments=inputIP.split(".")
    validIp=True
    try:
        if len(segments) != 4:
            return False
        for segment in segments:
            if int(segment) < 0 or int(segment) > 255:
                validIp=False
        return validIp
    except:
        return False

def removeHost(hostAdres=""):
    if hostAdres!="":
        """This function is used to remove a host automatically from the list of active hosts"""
        try:
            activeHosts.remove(hostAdres)
        except:
            console.print(Traceback())
        writeHosts()

    else:
        """This function is used to remove a host from the list of active hosts"""
        os.system("cls||clear")
        if (len(activeHosts)!=0):
            showActiveHosts()
            try:
                numberOfHost=int(input("Geef nummer van host op: "))
            except:
                console.print("[bold red]Verkeerd getal opgegeven.[/bold red]")
                time.sleep(1)
                return()
            try:
                del activeHosts[numberOfHost-1]
                writeHosts()
            except IndexError:
                console.print("[bold blue]Nummer kwam niet voor in lijst.[bold blue]")
                time.sleep(0.5)
            except:
                console.print(Traceback())
        else:
            console.print("[bold blue]Geen hosts in lijst.[/bold blue]")
            time.sleep(0.5)

def showActiveHosts():
    """This function is used to show the active hosts"""
    for i in range(0,len(activeHosts)):
        console.print(f"ip-adres host {i+1}: '{activeHosts[i]}'")

def showHostsInteractive():
    """This function is used to show the active hosts in an interactive way"""
    if len(activeHosts) !=0:
        showActiveHosts()
    else:
        console.print("Geen hosts in lijst.")
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