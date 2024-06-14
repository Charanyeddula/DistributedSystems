from platform import node
import socket
import pickle
from ._generatedKey import generatedKey
from math import pow


#------------------------------------
# This file holds two functions
# One to update the finger table of the current Node
# Other to Update the finger Tables of other Nodes
#------------------------------------




# Buffer size used for transferring the data
fileBuff = 6144


# Value of m for Chord Ring Topology
M_VALUE = 8
# Total number of possible nodes for the Chord Topology
TOTAL_NODES_POSSIBLE = int(pow(2, M_VALUE))




# Update Finger Table of Current Node 
def updFingerT(self):

    # 0 to m-1 entries in the finger table
    # Going through each value of bitNumber
    for bitNum in range(M_VALUE):
        fingerID = (self.nodeId + int(pow(2, bitNum))) % TOTAL_NODES_POSSIBLE
        
        # If the network has only one node
        # The node itself is in finger table
        if self.successor == self.combineAddr:
            self.fTable[fingerID] = (self.nodeId, self.combineAddr)
            continue
        
        # If the network has multiple nodes then we get the Successor >= fingerID
        ipPortReceive = self.getCurrNodeSucc(self.successor, fingerID)
        computedId = generatedKey(ipPortReceive[0] + ":" + str(ipPortReceive[1]))
        
        self.fTable[fingerID] = (computedId, ipPortReceive)





# Update the Finger Table of other nodes in the network
def updRemainingFingerTs(self):

    # Go to current Node Successor
    succAddr = self.successor
    
    while True:
        
        # There is only one node in the network and that is current Node
        if succAddr == self.combineAddr:
            break
        
        currSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            # Connect To Successor
            currSock.connect(succAddr)  # Connecting to server
            currSock.sendall(pickle.dumps([5]))

            # Receiving the next successor to update
            succAddr = pickle.loads(currSock.recv(fileBuff))
            
            currSock.close()
            
            # Iterate through successors one after another in the ring until you reach the same successor again
            if succAddr == self.successor:
                break
        except socket.error:
            print("Connection Refused")