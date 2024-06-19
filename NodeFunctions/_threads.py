import socket
import threading
import pickle
from ._generatedKey import generatedKey


#------------------------------
# Two different threads are defined 
# one for accepting incoming peers connection 
# and other to process request for those peer connections
#------------------------------


# Buffer size used for transferring the data
fileBuff = 6144


# Thread for accepting incoming peer Connection
def serverLtnThread(self):
    
    # Saving the connected peer info to perform requested operations
    while True:
        try:
            clientConn, combAddr = self.sSocket.accept()
            clientConn.settimeout(120)
            
            # Creating thread for peer opertions
            threading.Thread(target=self.clientReqRecvThread, args=(clientConn, combAddr)).start()
        
        except socket.error:
            print("ERROR: CONNECTION NOT ESTABLISHED")
            print("TRY AGAIN")



# Thread for each peer to perform operations
def clientReqRecvThread(self, clientConn, combAddr):
    
    receiveData = pickle.loads(clientConn.recv(fileBuff))
    
    # There are 5 types of connections
    # connection type : 0 --> Peer Network Join Request
    # connection type : 1 --> Peer acting as a client to upload or downoad fileBuff
    # connection type : 2 --> Contineously pinging to check for successor
    # connection type : 3 --> Looking for correct position to insert the keyname
    # connection type : 4 --> Successor or Predecessor update
    # connection type : 5 --> Updating the finger table of the node
    
    connType = receiveData[0]
    
    if connType == 0:
        print("Connected with --> ", combAddr[0], ":", combAddr[1])
        print("Join request made.")
        
        self.getCurrNodePred(clientConn, combAddr, receiveData)
        self.prntClientOptions()

    elif connType == 1:
        print("Connected with --> ", combAddr[0], ":", combAddr[1])
        print("Upload or Download req made")
        
        self.fileTransfer(clientConn, combAddr, receiveData)
        self.prntClientOptions()

    elif connType == 2:
        clientConn.sendall(pickle.dumps(self.predecessor))

    elif connType == 3:
        self.keyIdSearch(clientConn, combAddr, receiveData)

    elif connType == 4:
        if receiveData[1] == 1:
            self.successorUpdate(receiveData)
        else:
            self.predecessorUpdate(receiveData)
    
    elif connType == 5:
        self.updFingerT()

        # Sending the Current node's (Next nodes) Successor
        clientConn.sendall(pickle.dumps(self.successor))
    
    else:
        print("\nConnection type not-matched")