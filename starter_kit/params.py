import os
from typing import cast
from eth_typing import ChecksumAddress
from web3 import Web3
from dotenv import load_dotenv  # ✅ Load environment variables

# ✅ Load variables from .env file
load_dotenv()

# ✅ Manually define AUTONITY_CONTRACT_ADDRESS
AUTONITY_CONTRACT_ADDRESS = cast(ChecksumAddress, "0xEf9b191E098Bf009fFe0eAb0E7E1053e1266D236")

# Token and contract addresses
NTN_ADDRESS = AUTONITY_CONTRACT_ADDRESS
USDCX_ADDRESS = cast(ChecksumAddress, "0xB855D5e83363A4494e09f0Bb3152A70d3f161940")
WATN_ADDRESS = cast(ChecksumAddress, "0xcE17e51cE4F0417A1aB31a3c5d6831ff3BbFa1d2")
UNISWAP_ROUTER_ADDRESS = cast(ChecksumAddress, "0x374B9eacA19203ACE83EF549C16890f545A1237b")
UNISWAP_FACTORY_ADDRESS = cast(ChecksumAddress, "0x218F76e357594C82Cc29A88B90dd67b180827c88")

# ✅ Load recipient address from .env
RECIPIENT_ADDRESS = Web3.to_checksum_address(os.environ["RECIPIENT_ADDRESS"])

# Optional: test output
if __name__ == "__main__":
    print("NTN_ADDRESS:", NTN_ADDRESS)
    print("RECIPIENT_ADDRESS:", RECIPIENT_ADDRESS)
