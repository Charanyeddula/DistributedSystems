from ._generatedKey import generatedKey

#-----------------------------
# This is used for downlaoding the file from 
# current Node or uploading the file to 
# current node and its successor for redundancy
#-----------------------------




def fileTransfer(self, clientConn, address, receiveData):
    # Options for Selection
    # Selection 0 : Download
    # Selection 1 : Upload 

    selection = receiveData[1]
    fName = receiveData[2]
    
    fID = generatedKey(fName)
    
    # Download Request Made
    if selection == 0:
        print("\Download Request --> ", fName)
        try:
            # If file not found in its own directory. Then return file doesnt exist
            if fName not in self.fileList:
                clientConn.send("NotFound".encode('utf-8'))
                print("\nFile Not Found")
            
            # If file is present in the current directory then return found and the file
            else:
                clientConn.send("Found".encode('utf-8'))
                self.fileDataSend(clientConn, fName)
        except ConnectionResetError as error:
            print(error, "\nClient Dis-Connected")

    
    # Upload Request Made
    elif selection == 1 or selection == -1:
        print("\nReceived File --> ", fName)
        fID = generatedKey(fName)
        
        # Adding the file to file list of Current Node
        print("FileID Uploading --> ", fID)
        self.fileList.append(fName)

        # Receiving file Information
        self.fileDataReceive(clientConn, fName)
        
        print("Upload Completed.")
        
        # Replicating file to successor as well
        if selection == 1:
            if self.combineAddr != self.successor:
                self.uFileFunc(fName, self.successor, False)