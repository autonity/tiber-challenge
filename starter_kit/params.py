import os
from typing import cast

from autonity.constants import AUTONITY_CONTRACT_ADDRESS
from eth_typing import ChecksumAddress

NTN_ADDRESS = AUTONITY_CONTRACT_ADDRESS
USDC_ADDRESS = cast(ChecksumAddress, "0x3a60C03a86eEAe30501ce1af04a6C04Cf0188700")
WATN_ADDRESS = cast(ChecksumAddress, "0xcE17e51cE4F0417A1aB31a3c5d6831ff3BbFa1d2")

UNISWAP_ROUTER_ADDRESS = cast(
    ChecksumAddress, "0x374B9eacA19203ACE83EF549C16890f545A1237b"
)
UNISWAP_NTN_USDC_PAIR_ADDRESS = cast(ChecksumAddress, "0xTBC")

OWN_VALIDATOR_ADDRESS = cast(ChecksumAddress, os.environ["OWN_VALIDATOR_ADDRESS"])
RECIPIENT_ADDRESS = cast(ChecksumAddress, os.environ["RECIPIENT_ADDRESS"])
