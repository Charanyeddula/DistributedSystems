__________                        __           __________                     
\______   \ ____   ___________  _/  |_  ____   \______   \ ____   ___________ 
 |     ___// __ \_/ __ \_  __ \ \   __\/  _ \   |     ___// __ \_/ __ \_  __ \
 |    |   \  ___/\  ___/|  | \/  |  | (  <_> )  |    |   \  ___/\  ___/|  | \/
 |____|    \___  >\___  >__|     |__|  \____/   |____|    \___  >\___  >__|   
               \/     \/                                      \/     \/       
___________.__.__           ___________                              _____             
\_   _____/|__|  |   ____   \__    ___/___________    ____   _______/ ____\___________ 
 |    __)  |  |  | _/ __ \    |    |  \_  __ \__  \  /    \ /  ___/\   __\/ __ \_  __ \
 |     \   |  |  |_\  ___/    |    |   |  | \// __ \|   |  \\___ \  |  | \  ___/|  | \/
 \___  /   |__|____/\___  >   |____|   |__|  (____  /___|  /____  > |__|  \___  >__|   
     \/                 \/                        \/     \/     \/            \/       
 ____ ___      .__                 _________ .__                     .___
|    |   \_____|__| ____    ____   \_   ___ \|  |__   ___________  __| _/
|    |   /  ___/  |/    \  / ___\  /    \  \/|  |  \ /  _ \_  __ \/ __ | 
|    |  /\___ \|  |   |  \/ /_/  > \     \___|   Y  (  <_> )  | \/ /_/ | 
|______//____  >__|___|  /\___  /   \______  /___|  /\____/|__|  \____ | 
             \/        \//_____/           \/     \/                  \/ 



Instructions for execution and Folder Structure

--> Code Folder Structure
* Main/
    Node/
        __init__.py
        _checkForSuccessor.py
        _clientThread.py
        _exitGrid.py
        _fTableUpdates.py
        _fileOperations.py
        _fileTransfer.py
        _generatedKey.py
        _getCurrNodePred.py
        _getCurrNodeSucc.py
        _initiate.py
        _initiateNodeJoin.py
        _keyIdSearch.py
        _printInfo.py
        _threads.py
        _updates.py
    
    main.py 

--> Dependencies
    Install python 3.8.9

--> Code
    The Starter Code is in main
        Execute with --> "python3 main.py IP PORT"
                    E.g. "python3 main.py 167.76.165.2 7687"
                If IP and port are not given then default IP and PORT will be assigned
                    that is IP  : 127.0.0.1
                           PORT : 6000

    Once you execute the command you are given 6 options 
    1 : To Join the Network
        Once you enter option 1
        You should give IP in the network to connect to 
        And then you are requested for port in the network to connect to
    
    2: To get the information of current Node Successor and Predecessor

    3: Get the Finger table of current Node

    4: To upload afile
        To upload a file put the file in Main/ folder the same folder of main.py
        Or the File cannot be uploaded
        Enter the file name to upload

    5: To Download a file
        Enter the file name to Download
        If the File doesn't exit then file not found is displayed

    6: To let the node leave the network
        If the Node leaves the network then it transfers
        All the files present in it to appropriate node



--> For the Execution of this we are Using Multiple AWS EC2 instances

--> You can create multiple nodes via local host aswell but while execution
    Put the Code in various directories and execute
