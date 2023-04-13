import ping3
import time
import hostManagement
import json

activeCheckModes=[]
checkResults=[]
possibleChecks=["ping"]

def getCheckmode():
    return activeCheckModes

def toggleCheck(input):
    if input in possibleChecks:
        """This function is used to toggle a checkmode"""
        try:
            index =  activeCheckModes.index(f"{input}")
            del activeCheckModes[index] 
        except ValueError:
            activeCheckModes.append(f"{input}")
        writeCheckModes()
    else:
        print("check nog niet geïmplementeerd")
        time.sleep(0.5)

def performChecks():
    """This function is used to perform the checks"""
    if len(activeCheckModes) != 0:
        print("Checks worden uitgevoerd")
        for check in activeCheckModes:
            match check:
                case "ping":
                    executePing()
        createHTMLResults()
    else:
        print("Geen checkmode aangegeven")
        time.sleep(0.5)

        
def executePing():
    """This function is used to execute the ping check"""
    for host in hostManagement.getActiveHosts():
        succesfulPings=0
        for i in range(0,4):
            delay = ping3.ping(f"{host}")
            if type(delay)!=bool and delay!=None:
                succesfulPings+=1
        checkResults.append({
            "mode": "ping",
            "host": host,
            "pingReceived": succesfulPings,
            "positive": succesfulPings > 2
        })
    writeResults()
        

def writeCheckModes():
    """This function is used to write the active checkmodes to a file"""
    with open("checks.json","w") as checks:
        json.dump(activeCheckModes, checks)

def loadCheckModes():
    """This function is used to load the active checkmodes from a file"""
    global activeCheckModes
    try:
        with open("checks.json","r") as checks:
            activeCheckModes = json.load(checks)
    except FileNotFoundError:
        activeCheckModes = []
    except json.decoder.JSONDecodeError:
        activeCheckModes = []

def loadResults():
    """This function is used to load the results from a file"""
    global checkResults
    try:
        with open("results.json","r") as results:
            checkResults = json.load(results)
    except FileNotFoundError:
        checkResults=[]
    except json.decoder.JSONDecodeError:
        checkResults=[]

def writeResults():
    """This function is used to write the results to a file"""
    with open("results.json", "w") as results:
        json.dump(checkResults, results)

def createHTMLResults():
    """This function is used to create a html file with the results included"""
    try:
        text=[]
        with open("template.html","r") as template:
            while True:
                line = template.readline()
                if len(line)==0:
                    break
                text.append(line)
            target = open("results.html","w")
            target.writelines(text)
            target.close()

        temp = open("results.html","w")
        temp.close()
        with open("results.html","w") as results:
            for i in range(0,len(text)):
                if text[i] == "    </ul>\n":
                    for j in range(len(checkResults)-1,-1,-1):
                        results.writelines(f"<li>{checkResults[j]}</li>\n")
                results.write(text[i])         
    except FileNotFoundError:
        print("Geen template gevonden")