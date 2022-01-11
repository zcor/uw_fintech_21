pragma solidity ^0.5.0;

import "./Husky.sol";
import "OpenZeppelin/openzeppelin-contracts@2.5.0/contracts/token/ERC20/ERC20.sol";
import "OpenZeppelin/openzeppelin-contracts@2.5.0/contracts/crowdsale/Crowdsale.sol";

contract HuskyTokenMinter {
    HuskyToken private husky_token;
    uint256 private stored_last_price;
    address private stored_leader;
    address payable private admin;

    constructor(
        HuskyToken _token,
        address payable _admin
    )
        public
    {
	husky_token = _token;
	admin = _admin;
    }

    event NewLeader(address indexed _from, uint _value);


    function mint() public payable 
    {
	require(msg.value > stored_last_price, "Must pay more");
	husky_token.mint(msg.sender, 1e18);
	stored_last_price = msg.value ;
	if(husky_token.balanceOf(msg.sender) > husky_token.balanceOf(stored_leader)) {
		stored_leader = msg.sender;
                emit NewLeader(msg.sender, husky_token.balanceOf(msg.sender));
	}
    }
    function claim() public {
    	require(msg.sender == admin, "Only admin can claim");
	admin.transfer(address(this).balance);
    }
    function reset() public {
    	require(msg.sender == admin, "Only admin can reset");
	stored_last_price = 0;
	stored_leader = address(0);
    }
    function leader() public view returns (address) {
	return stored_leader;
    }
    function last_price() public view returns (uint256) {
	return stored_last_price;
    }
    function token() public view returns (address) {
	return address(husky_token);
    }
    function() external payable {}
}

contract HuskyTokenDeployer {

    address public minter_address;
    address public token_address;

    constructor(
        string memory name,
        string memory symbol,
        address payable admin // this address will receive all Ether raised by the sale
    )
        public
    {
        // create the ArcadeToken and keep its address handy
        HuskyToken husky_token = new HuskyToken(name, symbol, 0);
        token_address = address(husky_token);

        // create the ArcadeTokenSale and tell it about the token
        HuskyTokenMinter husky_minter = new HuskyTokenMinter(husky_token, admin);
        minter_address = address(husky_minter);

	// Add Minter as husky token minter, then renounce deployer's minter role
        husky_token.addMinter(minter_address);
        husky_token.renounceMinter();
    }
}
