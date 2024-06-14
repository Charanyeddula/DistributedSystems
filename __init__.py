from http.client import NETWORK_AUTHENTICATION_REQUIRED
import socket
from collections import OrderedDict
from ._generatedKey import generatedKey
from math import pow


#-----------------------------------------
# It is an initialization file for any Peer 
# that wants to enter the Network with 
# all the methods and attributes that a peer node can have.
#-----------------------------------------



# Buffer size used for transferring the data
fileBuff = 6144

# Value of m for Chord Ring Topology
M_VALUE = 8
# Total number of possible nodes for the Chord Topology
TOTAL_NODES_POSSIBLE = pow(2, M_VALUE)



class Node:
    def __init__(self, ipAddr, ipPort):
        self.fileList = []
        self.ipAddr = ipAddr
        self.ipPort = ipPort
        self.combineAddr = (ipAddr, ipPort)

        #Current Node ID
        self.nodeId = generatedKey(ipAddr + ":" + str(ipPort))
        
        #Current Node Predecessor
        self.predecessor = (ipAddr, ipPort)
        self.predecessorID = self.nodeId
        
        # Current Node Successor
        self.successor = (ipAddr, ipPort)
        self.successorID = self.nodeId
        
        # Stores finger table entries 
        # key is ID 
        # value tuple(IP Address, PORT)
        self.fTable = OrderedDict()
        
        try:
            # Creating Sockets for current node for it to 
            # act as server and accept any incoming request
            self.sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sSocket.bind(self.combineAddr)
            self.sSocket.listen()
        except socket.error:
            print("\nSocket not opened")


    # Importing all the methods from various files
    from ._threads import serverLtnThread, clientReqRecvThread
    from ._getCurrNodePred import getCurrNodePred
    from ._fileTransfer import fileTransfer
    from ._keyIdSearch import keyIdSearch
    from ._updates import successorUpdate, predecessorUpdate
    from ._initiate import initiate
    from ._checkForSuccessor import checkForSuccessor
    from ._clientThread import cliActionRequest
    from ._initiateNodeJoin import initiateNodeJoin
    from ._exitGrid import exitGrid
    from ._fileOperations import uFileFunc, dFileFunc
    from ._getCurrNodeSucc import getCurrNodeSucc
    from ._fTableUpdates import updFingerT, updRemainingFingerTs
    from ._fileOperations import fileDataSend, fileDataReceive
    from ._printInfo import prntClientOptions, prntFingerT
