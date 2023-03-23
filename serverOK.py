from ping3 import verbose_ping
checkMode=""

def mainLoop():
    print("###### Welkom bij de checkonator ######")
    print("Kies een van de onderstaande keuzes:")
    print("1. Voeg een host toe aan de targets. ")
    print("2. Geef de actieve hosts op.")
    print("3. Start een check uit op de targets.")
    print("")

    keuze=int(input("Geef keuze op: "))

    match keuze:
        case 3:
            chooseCheckMode()

def chooseCheckMode():
    print("Welk type check wilt u uitvoeren ?")
    print("- ping. voer een ping check uit.")
    checkMode=input("Geef keuze op: ")


if __name__ == "__main__":
    mainLoop()