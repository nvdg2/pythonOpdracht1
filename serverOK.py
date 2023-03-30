import hostManagement
import checks
import sys
import interactive
import automated

if __name__ == "__main__":
    hostManagement.loadHosts()
    checks.loadCheckModes()
    checks.loadResults()
    if(len(sys.argv)>1):
        automated.mainLoop()
    else:
        interactive.mainLoop()