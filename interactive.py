import os
import time
import hostManagement
import checks
import sys

from rich.console import Console
from rich.table import Table

console = Console()

checkMode=""

def mainLoop():
    """This function is used to start the main loop"""
    quitProgram=False
    while quitProgram != True:
        os.system("clear|cls")
        console.print("[bold magenta]###### Welkom bij de checkonator ######[/bold magenta]")
        console.print("Kies een van de onderstaande opties:")
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("Optie")
        table.add_column("Beschrijving")
        table.add_row("1", "Target hosts beheren.")
        table.add_row("2", "Checkmodus beheren.")
        table.add_row("3", "Voer checks uit.")
        table.add_row("q", "Het project afsluiten.")
        console.print(table)
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
                console.print("[bold red]Optie niet gevonden[/bold red]")
                time.sleep(0.5)

def manageHosts():
    """This function is used to manage the hosts"""
    quitHosts=False
    while quitHosts != True:
        os.system("clear|cls")
        console.print("[bold magenta]###### Beheer van hosts ######[/bold magenta]")
        console.print("Kies een van de onderstaande opties:")
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("Optie")
        table.add_column("Beschrijving")
        table.add_row("1", "Host toevoegen.")
        table.add_row("2", "Host verwijderen.")
        table.add_row("3", "Hosts weergeven.")
        table.add_row("q", "Terug naar hoofdmenu")
        console.print(table)
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
                console.print("[bold red]Optie niet gevonden[/bold red]")
                time.sleep(0.5)
        

def manageCheckMode():
    """This function is used to manage the checkmode"""
    quitChecks=False
    while quitChecks != True:
        os.system("clear|cls")
        console.print("[bold magenta]###### Beheer van checkmodus ######[/bold magenta]")
        table = Table(show_header=True, header_style="bold blue")
        console.print("Kies een van de onderstaande opties:")
        table.add_column("Actieve modus", justify="right")
        table.add_column(f"{checks.getCheckmode()}")
        table.add_row("1", "ping")
        table.add_row("2", "ping")
        table.add_row("3", "ping <-- beste keuze :)")
        table.add_row("q", "terug naar hoofdmenu")
        console.print(table)
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
                console.print("Optie niet gevonden")
                time.sleep(0.5)