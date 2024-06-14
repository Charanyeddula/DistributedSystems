#----------------------------------
# The file contains different file operation functions
# For uploading and downloading files and also two helper 
# functions to transfer file information as bits
#----------------------------------

import socket
import pickle
import time
import os
from ._generatedKey import generatedKey



# Buffer size used for transferring the data
fileBuff = 6144


# Upload File to the appropriate Node
def uFileFunc(self, fName, ipPortReceived, duplicate):
    
    print("Uploading the given file --> ", fName)
    
    sendData = [1]

    # This part is used for letting node know to store file in its Successor node
    if duplicate:
        sendData.append(1)
    else:
        sendData.append(-1)
    try:

        # Checking if the file for upload is present in the current directory or not
        f = open(fName, 'rb')
        f.close()

        sendData = sendData + [fName]

        # Send the file to the Ip and Port Peer received as an argument
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSock.connect(ipPortReceived)
        
        # Sending only the file Name
        clientSock.sendall(pickle.dumps(sendData))
        
        # Sending the File to IP, PORT received --> A helper function
        # Sending File Bits
        self.fileDataSend(clientSock, fName)
        clientSock.close()
        
        print("Uploaded File Successfully")
    except IOError:
        print("Requested file not present in the directory")
    except socket.error:
        print("Error occured while uploading the file")




# Download file from Appropriate Node
def dFileFunc(self, fName):
    print("\nDownloading the requested file --> ", fName)
    
    fID = generatedKey(fName)
    
    # Getting the Node where file is located at
    ipPortReceived = self.getCurrNodeSucc(self.successor, fID)
    sendData = [1, 0, fName]
    
    # Requesting that location for file
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSock.connect(ipPortReceived)
    clientSock.sendall(pickle.dumps(sendData))      
    
    # Received information if file found or not found
    fileData = clientSock.recv(fileBuff)
    
    if fileData == b"NotFound":
        print("FILE NOT FOUND --> ", fName)
    else:
        # Retrieving if File is Found
        print("Retrieving file --> ", fName)
        self.fileDataReceive(clientSock, fName)




# Sending File Information
def fileDataSend(self, clientConn, fName):
    print("\nSending file --> ", fName)
    
    # Opening the file in binary mode
    try:
        with open(fName, 'rb') as f:
            while True:
                
                # Reading all the bits in the file
                fileData = f.read(fileBuff)
                time.sleep(0.001)

                if not fileData:
                    break
                
                #Sending the File data
                clientConn.sendall(fileData)
    except:
        print("\n File not found")
    
    f.close()

    print("\nFile Sent")




# Receiving File content in parts and pieces
def fileDataReceive(self, clientConn, fName):
    
    # To See if File is already in the directory
    fPresentAlready = False
    
    try:
        # Opening file in binary format
        with open(fName, 'rb') as f:
            filData = f.read()

            # Check is file is empty or not
            fileSize = len(filData)

            # If File is Empty request for retransmission
            if fileSize == 0:
                print("\nRequest for Retransmission")
                fPresentAlready = False
            else:
                print("FILE ALREADY PRESENT")
                fPresentAlready = True
            
            return

    except FileNotFoundError:
        pass

    
    # If File has no data it it
    if not fPresentAlready:
        # Creating an Empty binary to append information to it
        completeData = b''
        dataReceiveSize = 0
        
        try:
            # Opening file in write Mode
            with open(fName, 'wb') as f:
                while True:
                    # Receive File binary Data
                    filData = clientConn.recv(fileBuff)
                    dataReceiveSize += len(filData)
                    
                    if not filData:
                        break
                    
                    completeData += filData
                
                # Write data to the file
                f.write(completeData)

        except ConnectionResetError:
            print("\nInformation Transfer Interupted")
            print("Stabilizing the system")
            print("TRYING AGAIN...")
            
            time.sleep(5)
            os.remove(fName)
            
            time.sleep(5)
            self.dFileFunc(fName)
            
