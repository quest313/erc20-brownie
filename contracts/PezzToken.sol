// contracts/PezzToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract PezzToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("Pezz", "PZZ") {
        _mint(msg.sender, initialSupply);

        address funder = 0x6ab887aa077455c44794b9cC73B0C3eD9B4FFacf;
        transfer(funder, 1000);
    }
}
