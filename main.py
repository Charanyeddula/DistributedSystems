import sys
from Node import Node

#---------------------------
# This is the started file where the 
# instance of node of a network is 
# created and execution gets started
#---------------------------


# Default values of IpAddress and port if command line arguments are not given
ipAddr = "127.0.0.1"
ipPort = 6000

# Checking for commandline arguments
if len(sys.argv) <= 2:
    print("Ip and Port are not passed --> default values are used")
else:
    ipAddr = sys.argv[1]
    ipPort = int(sys.argv[2])

# Initialing the node instance to connect to the network
currNode = Node(ipAddr, ipPort)
print("Current Node ID = ", currNode.nodeId)
currNode.initiate()
currNode.sSocket.close()