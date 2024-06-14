#-------------------------------
# This function takes in IP address 
# and PORT combined as an input and 
# returns the hashed key for the the Chord Topology
#-------------------------------

import hashlib
from math import pow


# Value of m for Chord Ring Topology
M_VALUE = 8
# Total number of possible nodes for the Chord Topology
TOTAL_NODES_POSSIBLE = pow(2, M_VALUE)


def generatedKey(combAddr):
    # Using SHA-1 hashing algorithm
    shaKey = hashlib.sha1(combAddr.encode())
    hex = int(shaKey.hexdigest(), 16)

    # Outputs 8 bit integer in range (0, 256)
    nId = hex % int(TOTAL_NODES_POSSIBLE)
    return nId
