#----------------------------
# The following operations happen if
# user requests to leave the network
#----------------------------

import socket, random
import pickle
from ._generatedKey import generatedKey



# Buffer size used for transferring the data
fileBuff = 6144


# node leaving the network
def exitGrid(self):
    
    # Invoking current node successor to change its predecessor
    peerSok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    peerSok.connect(self.successor)
    peerSok.sendall(pickle.dumps([4, 0, self.predecessor]))
    peerSok.close()
    
    
    # Invoking current node predecessor to change its successor
    peerSok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    peerSok.connect(self.predecessor)
    peerSok.sendall(pickle.dumps([4, 1, self.successor]))
    peerSok.close()
    
    # Listing files if current node has any
    print("\nFiles current node has --> ", self.fileList)
    
    # If Current node has any files then 
    # transfer them to its successor before leaving
    print("\n Transferring files to other nodes before leaving")
    
    #Going throught the files list
    for fName in self.fileList:
        peerSok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        peerSok.connect(self.successor)
        
        sDataList = [1, 1, fName]
        
        # Sending files to its next appropriate node location
        peerSok.sendall(pickle.dumps(sDataList))
        
        # Confirmation if files are received
        with open(fName, 'rb') as file:
            peerSok.recv(fileBuff)
            self.fileDataSend(peerSok, fName)
            peerSok.close()
            
            print("Files Replication Completed.")
        
        peerSok.close()
    
    # Update the finger tables of all the nodes in the network
    self.updRemainingFingerTs()
    
    # Current node values are reverted to defaults
    self.predecessor = (self.ipAddr, self.ipPort)
    self.predecessorID = self.nodeId
    self.successor = (self.ipAddr, self.ipPort)
    self.successorID = self.nodeId
    
    # Clearing the finger Table
    self.fTable.clear()
    
    #Node Left the Network
    print(self.combineAddr, " Left the network")
