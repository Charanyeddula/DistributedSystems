from ._generatedKey import generatedKey

#--------------------------
# These functions update the successor and predecessor 
# respectively based on the received information
#--------------------------


def successorUpdate(self, receiveData):
    # Received new successor
    nSuccessor = receiveData[2]
    
    # Updating the Successor
    self.successor = nSuccessor
    self.successorID = generatedKey(nSuccessor[0] + ":" + str(nSuccessor[1]))
    

def predecessorUpdate(self, receiveData):
    # Received new Predecessor
    nPredecessor = receiveData[2]

    # Updating the Predecessor
    self.predecessor = nPredecessor
    self.predecessorID = generatedKey(nPredecessor[0] + ":" + str(nPredecessor[1]))