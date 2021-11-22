# LockChain
A Blockchain Locking System

# How to run:
The easiest way to get this project up and running is through the Ganache test server and the Remix web IDE. Download Ganache from Truffle, and then execute it from command line with the command: 

ganache-cli

Go to remix.ethereum.org
Open the file Lock.sol into the web IDE. In the run tab, find the environment dropdown and select "Injected Web3" and use the server address created by the ganache-cli (the default is localhost:8545).

Now deploy the contract. Copy the address of the smart contract into the file index.html at line 215 into var contractAddress. 
Note: If you change the code in the Lock file you need to get the new AVI from remix to put into the var LockContract.

Once this is all done, simply open index.html. The webpage should be a simple user interface for interacting with the smart contracts.

TODO: Include instructions for deploying with truffle instead. 
