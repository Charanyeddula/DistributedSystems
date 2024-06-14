#---------------------------------
# The function takes in the IP, PORT of "peer in the network to connect" 
# along with its own ID and iteratively checks for the 
# correct location to insert the incoming node or the current 
# nodes successor and returns its address
#---------------------------------

import socket
import pickle
from ._generatedKey import generatedKey


# Buffer size used for transferring the data
fileBuff = 6144


def getCurrNodeSucc(self, combAddr, nId):

    # Successor request sent to the given address
    dataReceived = [1, combAddr]
    ipPortReceive = dataReceived[1]
    
    while dataReceived[0] == 1:
        pNodeSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            pNodeSock.connect(ipPortReceive)
            
            # Position request for the nId until found one via lookUP
            sendData = [3, nId]
            pNodeSock.sendall(pickle.dumps(sendData))
            
            # Correct possition for nId is received
            dataReceived = pickle.loads(pNodeSock.recv(fileBuff))
            ipPortReceive = dataReceived[1]
            pNodeSock.close()
            
        except socket.error:
            print("\nConnection refuced getting the Successor")
    
    return ipPortReceive
