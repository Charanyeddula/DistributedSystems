#------------------------------------
# The function initiates the join request and 
# adds the new Peer to its appropriate Successor and
# Predecessor and into the appropriate position in the network
#------------------------------------

import socket
import pickle
from ._generatedKey import generatedKey


# Buffer size used for transferring the data
fileBuff = 6144



def initiateNodeJoin(self, ipAddr, ipPort):
    try:
        ipPortReceive = self.getCurrNodeSucc((ipAddr, ipPort), self.nodeId)
        
        # Connecting to the successor received
        pSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pSock.connect(ipPortReceive)
        
        sendData = [0, self.combineAddr]
        
        # Sending current peer address to add to the network via successor
        pSock.sendall(pickle.dumps(sendData))

        # Received new Predecessor for the current Node
        receiveData = pickle.loads(pSock.recv(fileBuff))
        
        # Updating the predecessor
        self.predecessor = receiveData[0]
        self.predecessorID = generatedKey(self.predecessor[0] + ":" + str(self.predecessor[1]))
        
        # Updating the Successor
        self.successor = ipPortReceive
        self.successorID = generatedKey(ipPortReceive[0] + ":" + str(ipPortReceive[1]))
        
        # Informing the Predecessor to update its Successor to current node
        sendData = [4, 1, self.combineAddr]
        
        #Connecting to predecessor
        otherPeerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        otherPeerSock.connect(self.predecessor)
        otherPeerSock.sendall(pickle.dumps(sendData))
        
        otherPeerSock.close()
        pSock.close()
    
    except socket.error:
        print("\nSocket Error")
        print("Check IP and PORT")
