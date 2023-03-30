import sys
import hostManagement
import checks
def mainLoop():
    match sys.argv[1]:
        case "host":
            match sys.argv[2]:
                case "add":
                    hostManagement.addHost(sys.argv[3])
                case "remove":
                    hostManagement.removeHost(sys.argv[3])
        case "check":
            match sys.argv[2]:
                case "toggle":
                    checks.toggleCheck(sys.argv[3])
                case "perform":
                    checks.performChecks()