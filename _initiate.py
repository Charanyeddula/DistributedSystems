#---------------------------
# Creating the Node by initializng two threads  
# one for thread acting as a server receiving connections 
# and another always pinging and checking for a successor
#---------------------------

from tabnanny import check
import threading
from ._generatedKey import generatedKey


def initiate(self):
    
    # Receiving and accepting connections from other peer threds
    threading.Thread(target=self.serverLtnThread, args=()).start()

    # Continueously pinging successor to check if it is active
    threading.Thread(target=self.checkForSuccessor, args=()).start()
    
    # Working as a peer in the network and requesting information as a client
    while True:
        print("\nListen for other entering peers")   
        self.cliActionRequest()
