#---------------------------------
# This Function takes in option input from the peer 
# for what kind of operation they want to perform and 
# based on that other methods are scheduled
#---------------------------------

from ._generatedKey import generatedKey


# Keeping tab of operations requested as a client
def cliActionRequest(self):
    
    # Displaying options to select from
    self.prntClientOptions()
    
    userInp = input()
    
    # Request to connect to a network
    if userInp == "1":
        ipAddr = input("Enter IP address to connect = ")
        ipPort = input("Enter PORT to connect =  ")
        self.initiateNodeJoin(ipAddr, int(ipPort))

    # Request for current node successor and predecessor
    elif userInp == "2":
        print("Current Node ID = ", self.nodeId)
        print("Predecessor Node ID = ", self.predecessorID)
        print("Successor Node ID = ", self.successorID)

    # Request for current node Finger Table
    elif userInp == "3":
        self.prntFingerT()
    
    # Request to upload file
    elif userInp == "4":
        fName = input("Enter Filename to Upload: ")
        fID = generatedKey(fName)

        # Gettign the node where to store thr file
        ipPortReceived = self.getCurrNodeSucc(self.successor, fID)

        # Store the file in the received IP, PORT node and its successor and hence True
        self.uFileFunc(fName, ipPortReceived, True)
    
    # Request to download file
    elif userInp == "5":
        fName = input("Enter filename: ")
        self.dFileFunc(fName)
    
    # Request to leave the Network
    elif userInp == "6":
        self.exitGrid()
