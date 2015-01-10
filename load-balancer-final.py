"""
Simulation of Web App Architecture

Service: The Russian Peasant's Algorithm

Architecture Include:

 - App Computer (Modules)
 - Database (--) --> Russian Peasant Algorithm
 - Load Balancer (Algorithm)

+-----+   +-----+   +-----+
| APP |   | APP |   | APP |
|  1  |   |  2  |   |  3  |
+-----+   +-----+   +-----+
"""
## Server names
import computer1
import computer2
import computer3

SERVERS = [computer1, computer2, computer3]

n = -1
def get_server():
    global n
    n += 1
    return SERVERS[n % len(SERVERS)]


## Testing Load which needs balancing
if __name__ == '__main__':
    for i in range(3):
        server = get_server()
        print server.printName
        print server.multiplyHandler
        print server.lastMultipliedHandler
        print " "
        
