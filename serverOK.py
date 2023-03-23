from ping3 import verbose_ping
import os
import time
import hostManagement
checkMode=""
activeHosts=[]
def mainLoop():
    print(activeHosts)
    stop_Program=False
    while stop_Program == False:
        os.system('cls||clear')
        print("###### Welkom bij de checkonator ######")
        print("Kies een van de onderstaande opties:")
        print("1. Target hosts beheren.")
        print("2. Checkmodus beheren.")
        print("q. Het project afsluiten.")
        print("")
        keuze=input("Geef keuze op: ")

        match keuze:
            case "1":
                manageHosts()
            case "2":
                manageCheckMode()
            case "q":
                stop_Program=True
            case _:
                print("Optie niet gevonden")
                time.sleep(0.5)
                mainLoop()

def manageHosts():
    os.system('cls||clear')
    print("###### Beheer van hosts ######")
    print("Kies een van de onderstaande opties:")
    print("1. Host toevoegen.")
    print("2. Host verwijderen.")
    print("3. Hosts weergeven.")
    print("q. terug naar hoofdmenu")
    print("")
    keuze=input("Geef keuze op: ")

    match keuze:
        case "1":
            hostManagement.addHost()
        case "2":
            hostManagement.removeHost()
        case "3":
            hostManagement.showHostsInteractive()
        case "q":
            mainLoop()
        case _:
            print("Optie niet gevonden")
            time.sleep(0.5)
    manageHosts()

def manageCheckMode():
    os.system('cls||clear')
    print("###### Beheer van checkmodus ######")
    print("Welke check wilt u activeren ?: ")
    print("1. ping")
    print("2. ping.")
    print("3. ping <-- beste keuze :)")
    print("q. terug naar hoofdmenu")
    print("")
    keuze=input("Geef keuze op: ")
    match keuze:
        case "1":
            checkMode="ping"
        case "2":
            checkMode="ping"
        case "3":
            checkMode="ping"
        case "q":
            mainLoop()
        case _:
            print("Optie niet gevonden")
            time.sleep(0.5)
            manageCheckMode()

if __name__ == "__main__":
    mainLoop()