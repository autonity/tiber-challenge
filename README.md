# tibernet-challenge

GitHub repository for the Autonity Tibernet Challenge.

## Use-case Testing Starter Kit

Example code for the Use-case Testing activity of the Tiber Challange
can be found in the [`starter_kit`](./starter_kit/) directory.

Participants can earn points by running the script as-is, but in order to get
awarded with a higher score it is recommended to modify and optimize the code.

The example code has been written in Python using the
[Web3.py](https://web3py.readthedocs.io/en/stable/) framework and the
[autonity.py](https://github.com/autonity/autonity.py) library of Autonity
contract bindings.

The [`starter_kit.bindings`](./starter_kit/bindings/) module contains Python
bindings for the Uniswap V2 Router contract and ERC20 token contracts.

## Getting Started

1. Fork and clone this repository.
2. Install [Pipenv](https://pipenv.pypa.io/en/latest/) with `pip install --user pipenv`.
3. Install dependencies with `pipenv install`.
4. Duplicate `.env.template` as `.env` and set the required environment variables.
5. Run the script with `pipenv run starter_kit`.
