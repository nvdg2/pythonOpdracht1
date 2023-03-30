import os
import time
import hostManagement
import checks
import sys


checkMode=""
def mainLoop():
    """This function is used to start the main loop"""
    quitProgram=False
    while quitProgram != True:
        os.system('cls||clear')
        print("###### Welkom bij de checkonator ######")
        print("Kies een van de onderstaande opties:")
        print("1. Target hosts beheren.")
        print("2. Checkmodus beheren.")
        print("3. Voer checks uit.")
        print("q. Het project afsluiten.")
        print("")
        keuze=input("Geef keuze op: ")
        match keuze:
            case "1":
                manageHosts()
            case "2":
                manageCheckMode()
            case "3":
                checks.performChecks()          
            case "q":
                quitProgram= True
            case _:
                print("Optie niet gevonden")
                time.sleep(0.5)

def manageHosts():
    """This function is used to manage the hosts"""
    quitHosts=False
    while quitHosts != True:
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
                quitHosts=True
            case _:
                print("Optie niet gevonden")
                time.sleep(0.5)
        

def manageCheckMode():
    """This function is used to manage the checkmode"""
    
    quitChecks=False
    while quitChecks != True:
        os.system('cls||clear')
        print("###### Beheer van checkmodus ######")
        print(f"Actieve modus: {checks.getCheckmode()}")
        print("Welke check wilt u activeren ?: ")
        print("1. ping")
        print("2. ping.")
        print("3. ping <-- beste keuze :)")
        print("q. terug naar hoofdmenu")
        print("")
        keuze=input("Geef keuze op: ")
        match keuze:
            case "1":
                checks.toggleCheck("ping")
            case "2":
                checks.toggleCheck("ping")
            case "3":
                checks.toggleCheck("ping")
            case "q":
                quitChecks=True
            case _:
                print("Optie niet gevonden")
                time.sleep(0.5)

def automatedMain():
    """This function is used for automated testing"""
    print("lezdgtezdhzeg")

if __name__ == "__main__":
    """This function is used to start the program"""
