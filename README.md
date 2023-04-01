# Gebruik van de commandline om acties uit te voeren met het Python-script

Dit Python-script biedt de mogelijkheid om acties uit te voeren voor hostbeheer en controles. Hieronder vindt u informatie over het gebruik van de command line om deze acties uit te voeren.

## Voorbereiding

1. Zorg ervoor dat Python is geïnstalleerd op uw computer. Als dat niet het geval is, kunt u het downloaden van de [officiële Python-website](https://www.python.org/downloads/).

2. Zorg ervoor dat de vereiste modules zijn geïnstalleerd. U kunt deze installeren met behulp van pip. Open de terminal en typ het volgende commando: `pip install -r requirements.txt`

## Hostbeheer

Om hostbeheeracties uit te voeren, gebruikt u de volgende opdrachten:

1. `python serverOK.py host add [hostname]` - Voegt een nieuwe host toe met de opgegeven naam.

2. `python serverOK.py host remove [hostname]` - Verwijdert de host met de opgegeven naam.

## Controles

Om controles uit te voeren, gebruikt u de volgende opdrachten:

1. `python serverOK.py check toggle [checkname]` - Schakelt de controle met de opgegeven naam in of uit.

2. `python serverOK.py check perform` - Voert alle controles uit die zijn ingesteld.

Opmerking: vervang `[hostname]` en `[checkname]` door de juiste naam van de host of controle die u wilt toevoegen, verwijderen, inschakelen of uitschakelen.

Als u hulp nodig heeft bij het gebruik van deze opdrachten, typt u gewoon `python serverOK.py -h` voor een lijst van beschikbare opdrachten en opties.

Veel succes met het gebruik van dit script!

## Interactieve sessie

Wanneer je graag het beheer van de hosts en de controles interactief instelt, voer dan het volgende commando uit: `python serverOK.py`