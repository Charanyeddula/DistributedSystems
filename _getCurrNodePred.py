#---------------------------------
# It is a helper function for nodes to join the network
# Updating the predecessor to the newly joined node and
# returning the old predecessor to the joined node
# This also triggers the updation of the finger table of all the peers
#---------------------------------


import pickle
import time
from ._generatedKey import generatedKey


# Join Node Helper Function
def getCurrNodePred(self, peerConn, combineAddr, receivedData):
    if receivedData:
        ipPortPeer = receivedData[1]
        pId = generatedKey(ipPortPeer[0] + ":" + str(ipPortPeer[1]))
        
        # Getting the old predecessor
        oPredecessor = self.predecessor
        
        # Updating the current node predecessor to the new predecessor(newly joined Node)
        self.predecessor = ipPortPeer
        self.predecessorID = pId
        
        # Returning the old Predecessor to the newly joined Node
        sendData = [oPredecessor]
        peerConn.sendall(pickle.dumps(sendData))
    
        time.sleep(0.1)
        
        # Updating the Finger Table of the Current Node
        self.updFingerT()
        
        # Requesting the Other Peers in the network to update their Finger table
        self.updRemainingFingerTs()
