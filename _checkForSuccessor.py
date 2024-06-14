#-------------------------
# The Function here runs on a different thread and checks continuously, 
# if the successor for that node is present. 
# If The successor is not present then the stabilization of nodes happens
#-------------------------

import socket
import pickle
import time
from ._generatedKey import generatedKey


# Buffer size used for transferring the data
fileBuff = 6144


def checkForSuccessor(self):
    while True:
        
        # Check for Successor every 3 seconds
        time.sleep(3)
        
        # If Network has only one node then no need for pinging
        if self.combineAddr == self.successor:
            continue
        
        # Try Pinging the Successor
        try:
            peerSok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            peerSok.connect(self.successor)
            # Request for Pinging Successor
            peerSok.sendall(pickle.dumps([2]))

            # Response for Ping received  
            recvPred = pickle.loads(peerSok.recv(fileBuff))
            
            peerSok.close()
        except:
            # Node Got Disconnected
            print("\nNode is offline")
            print("Stabilizing the Network....")
            
            # Search for next new Successor for the node
            newSuccessor = False
            val = ()
            
            # Getting the new Successor
            for k, val in self.fTable.items():
                if val[0] != self.successorID:
                    newSuccessor = True
                    break
            
            
            if newSuccessor:
                # Update Current Node Successor to new Successor
                self.successor = val[1]
                self.successorID = generatedKey(self.successor[0] + ":" + str(self.successor[1]))
                
                # Update new Succesor predecessor to current Node
                peerSok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                peerSok.connect(self.successor)
                peerSok.sendall(pickle.dumps([4, 0, self.combineAddr]))
                peerSok.close()

            # If the network is left with only one node
            else:       
                # Update Successor to Current Node
                self.successor = self.combineAddr
                self.successorID = self.nodeId

                #Update Predecessor to Current node
                self.predecessor = self.combineAddr
                self.predecessorID = self.nodeId
                
            
            # Updating finger table of Current Node
            self.updFingerT()

            # Updating the finger table of all the other nodes in the network
            self.updRemainingFingerTs()
            self.prntClientOptions()
