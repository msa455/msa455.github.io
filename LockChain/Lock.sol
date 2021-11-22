pragma solidity ^0.4.10;

contract Lock1 {
    struct User {
        address parent;
        address[] children;
    }

    bool locked = true;

    bool initiated = false;
    
    mapping(address => bool) hasAccess;
    mapping(address => User) users;
    address[] public userAccts;
    
    //function called on first initiation of the smart contract
    //allows the original deploying user to be added to the access list
    function initiateLock() public{
        if(!initiated){
            hasAccess[msg.sender] = true;
            initiated = true;
        }
    }
    
    function removeUser(address _addressToRemove) public{
        hasAccess[_addressToRemove] = false;
    }
    
    function addUser(address _newUser) public returns(bool){
        //User newUser = users[_newUser];
        // newUser.parent = _parent;
        // users[_parent].children.push(_newUser);
        //userAccts.push(_newUser) -1;
        if(hasAccess[msg.sender] == true){
            hasAccess[_newUser] = true;
            return true;
        }
        else{
            return false;
        }
    }
    
    function validateUser(address _addressToValidate) view public returns(bool){
        // for(uint i=0; i<userAccts.length; i++){
        //     if(userAccts[i] == _addressToValidate){
        //         return true;
        //     }
        // return false;
        // }
        return(hasAccess[_addressToValidate]);
    }
    
    function openLock() public returns(bool){
        if(hasAccess[msg.sender]){
            locked = false;
            return true;
        }
        else{
            return false;
        }
    }
    
    function closeLock() public returns(bool){
        if(hasAccess[msg.sender]){
            locked = true;
            return true;
        }
        return false;
    }

    

    
    
    function arrayLength() public constant returns(uint count){
        return userAccts.length;
    }
    
    function getLocPar(uint index) public constant returns(address){
        return userAccts[index];
    }
    
    function checkLock() public constant returns(bool){
        return locked;
    }
}