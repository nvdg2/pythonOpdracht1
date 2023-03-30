import ping3
import traceback
import time
import hostManagement
activeCheckModes=[]
checkResults=[]
def getCheckmode():
    return activeCheckModes

def toggleCheck(input):
    """This function is used to toggle a checkmode"""
    try:
        index =  activeCheckModes.index(f"{input}")
        del activeCheckModes[index] 
    except ValueError:
        activeCheckModes.append(f"{input}")
    writeCheckModes()

def performChecks():
    """This function is used to perform the checks"""
    if len(activeCheckModes) !=0:
        for check in activeCheckModes:
            match check:
                case "ping":
                    executePing()
        input("Druk op enter om verder te gaan")
        maakHtmlVanResultaten
    else:
        print("Geen checkmode aangegeven")
        time.sleep(0.5)


        
def executePing():
    """This function is used to execute the ping check"""
    for host in hostManagement.getActiveHosts():
        aantalPingsSuccesvol=0
        for i in range(0,4):
            delay = ping3.ping(f"{host}")
            if type(delay)!=bool:
                aantalPingsSuccesvol+=1
        checkResults.append({
            "mode": "ping",
            "pingReceived": aantalPingsSuccesvol,
            "positive": aantalPingsSuccesvol > 2
        })
    writeResults()
    maakHtmlVanResultaten()
        

def writeCheckModes():
    """This function is used to write the active checkmodes to a file"""
    with open("checks.txt","w") as checks:
        temp = open("checks.txt","w")
        temp.close()
        for i in range(0,len(activeCheckModes)):
            if i == 0:
                checks.write(f"{activeCheckModes[i]}")
            else:
                checks.write(f",{activeCheckModes[i]}")

def loadCheckModes():
    """This function is used to load the active checkmodes from a file"""
    global activeCheckModes
    try:
        with open("checks.txt","r") as checks:
            while True:
                line = checks.readline()
                if len(line)==0:
                    break
                else:
                    activeCheckModes =line.split(",")
    except FileNotFoundError:
        hosts = open("checks.txt","w")
        hosts.close()

def loadResults():
    """This function is used to load the results from a file"""
    global checkResults
    try:
        with open("results.txt","r") as results:
            while True:
                line = results.readline()
                if len(line)==0:
                    break
                else:
                    checkResults.append(line.replace("\n",""))

    except FileNotFoundError:
        hosts = open("checks.txt","w")
        hosts.close()

def writeResults():
    """This function is used to write the results to a file"""
    with open("results.txt","w") as results:
        temp = open("results.txt","w")
        temp.close()
        for i in range(0,len(checkResults)):
            if i == 0:
                results.write(f"{checkResults[i]}")
            else:
                results.write(f"\n{checkResults[i]}")

def maakHtmlVanResultaten():
    """This function is used to create a html file with the results included"""
    try:
        tekst=[]
        with open("template.html","r") as template:
            while True:
                line = template.readline()
                if len(line)==0:
                    break
                tekst.append(line)
            target = open("results.html","w")
            target.writelines(tekst)
            target.close()

        temp = open("results.html","w")
        temp.close()
        with open("results.html","w") as results:
            for i in range(0,len(tekst)):
                if tekst[i] == "    </ul>\n":
                    for j in range(len(checkResults)-1,-1,-1):
                        results.writelines(f"<li>{checkResults[j]}</li>\n")
                results.write(tekst[i])         

    except FileNotFoundError:
        print("Geen template gevonden")