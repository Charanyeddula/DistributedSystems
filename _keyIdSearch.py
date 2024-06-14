#------------------------------
# The function looks up for the 
# apt position of the nId successor to insert before
#------------------------------


import pickle
from ._generatedKey import generatedKey



def keyIdSearch(self, clientConn, address, receiveData):
    nID = receiveData[1]
    sendData = []
    
    # If nId is itself
    if self.nodeId == nID:
        sendData = [0, self.combineAddr]

    # If there is only one node in network
    elif self.successorID == self.nodeId:
        sendData = [0, self.combineAddr]
    
    # If current node is greater than given nId and nId is 
    # greater than current node predecessor then required answer is current node 
    elif self.nodeId > nID:
        if self.predecessorID < nID:   # If pred is higher than key, then self is the node
            sendData = [0, self.combineAddr]
        
        # If predecessor is greter than current node then its the 
        # cycle join point and hence current node the required answer
        elif self.predecessorID > self.nodeId:
            sendData = [0, self.combineAddr]
        
        #Return Predecessor
        else:   
            sendData = [1, self.predecessor]
    
    # If current nodeId is less than nID then we would 
    # use the chord ring algorithm to find the apt position
    else:

        # Node before cycle join point
        if self.nodeId > self.successorID:
            sendData = [0, self.successor]
        
        # Chord Algo lookup
        else:
            val = ()
            
            for key, val in self.fTable.items():
                if key >= nID:
                    break
            val = self.successor
            
            sendData = [1, val]
    
    clientConn.sendall(pickle.dumps(sendData))
    
