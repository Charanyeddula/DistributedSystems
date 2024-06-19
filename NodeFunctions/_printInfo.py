from ._generatedKey import generatedKey

#---------------------------------
# The functions here perform display operations. 
# One to Display options as a client for the node. 
# Another Displays the Finger table of the requested user.
#---------------------------------


# Peer options as a client
def prntClientOptions(self):
    print("\n1 --> Enter Network")
    print("2 --> Get Node Succ and Pred")
    print("3 --> Get Node Finger Table")
    print("4 --> Upload File")
    print("5 --> Download File")
    print("6 --> Leave Network")
    print("Enter any of the above options")


# Display node's finger table
def prntFingerT(self):
    print("\nFinger Table of the Node")
    
    for k, val in self.fTable.items(): 
        print("NodeID:", k, "Address value", val)