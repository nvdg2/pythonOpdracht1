import ping3
import traceback
import time
import hostManagement
activeCheckModes=[]

def getCheckmode():
    return activeCheckModes

def toggleCheck(input):
    try:
        index =  activeCheckModes.index(f"{input}")
        del activeCheckModes[index] 
    except ValueError:
        activeCheckModes.append(f"{input}")
    writeChecks()

def performChecks():
    if len(activeCheckModes) !=0:
        for check in activeCheckModes:
            match check:
                case "ping":
                    executePing()
        input("Druk op enter om verder te gaan")
    else:
        print("Geen checkmode aangegeven")
        time.sleep(0.5)

        
def executePing():
    for host in hostManagement.getActiveHosts():
        ping3.verbose_ping(f"{host}")
        

def writeChecks():
    with open("checks.txt","w") as checks:
        temp = open("checks.txt","w")
        temp.close()
        for i in range(0,len(activeCheckModes)):
            if i == 0:
                checks.write(f"{activeCheckModes[i]}")
            else:
                checks.write(f",{activeCheckModes[i]}")

def loadChecks():
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