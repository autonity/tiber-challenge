# Autonity Tiber Challenge

GitHub repository for the Autonity Tiber Challenge.

Example code for the Use-case Testing activity of the Tiber Challange.

Participants can earn points by running the script as-is, but in order to get
awarded with a higher score it is recommended to modify and optimize the code.

The example code has been written in Python using [v6.19.0 of the Web3.py
framework](https://web3py.readthedocs.io/en/v6.19.0/) and [v4.0.0 of the
autonity.py library](https://github.com/autonity/autonity.py/tree/v4.0.0) of Autonity
contract bindings.

The [`starter_kit.bindings`](./starter_kit/bindings/) module contains Python
bindings for the Uniswap V2 Factory and Uniswap V2 Router contracts.

## Getting Started

You need these installed on your system:

- [nix installer](https://zero-to-nix.com/concepts/nix-installer) 
- [devenv](https://devenv.sh/getting-started/) 

1. Fork and clone this repository.
2. Duplicate `.env.template` as `.env` and set the required environment variables.
3. Run the script with `starter-kit`.
4. Run linters with `lint-code`.
