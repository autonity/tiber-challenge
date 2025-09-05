from typing import Callable, List, TypeAlias, cast
from eth_typing import ChecksumAddress
from web3 import Web3
from web3.types import TxParams
from hexbytes import HexBytes
import time
from unittest.mock import MagicMock

# =================== Mocked Contracts ===================
class Autonity:
    def __init__(self, w3):
        print("[Mock] Autonity class loaded.")
        self.w3 = w3

    def decimals(self):
        return 18

    def transfer(self, to, amount):
        print(f"[Mock] Transfer {amount} tokens to {to}")
        return self

    def bond(self, validator, amount):
        print(f"[Mock] Bond {amount} tokens to validator {validator}")
        return self

    def unbond(self, validator, amount):
        print(f"[Mock] Unbond {amount} tokens from validator {validator}")
        return self

    def approve(self, spender, amount):
        print(f"[Mock] Approve {amount} tokens for {spender}")
        return self

    def get_validators(self):
        return ["0x0000000000000000000000000000000000000001"]

    def transact(self):
        tx_hash = HexBytes("0x000000000000000000000000000000000000000000000000000000000000beef")
        print(f"[Mock] Transaction sent: {tx_hash.hex()}")
        return tx_hash

class ERC20:
    def __init__(self, w3, address):
        self.w3 = w3
        self.address = address

    def decimals(self):
        return 18

    def approve(self, spender, amount):
        print(f"[Mock ERC20] Approving {amount} tokens to {spender}")
        return self

    def balance_of(self, address):
        return 1000000000000000000

    def transact(self, *args, **kwargs):
        return HexBytes("0x000000000000000000000000000000000000000000000000000000000000beef")

class UniswapV2Router02:
    def __init__(self, w3, address):
        self.w3 = w3
        self.address = address

    def swap_exact_tokens_for_tokens(self, amount_in, amount_out_min, path, to, deadline):
        print(f"[Mock Router] Swapping {amount_in} tokens for {path}")
        return self

    def swap_exact_eth_for_tokens(self, amount_out_min, path, to, deadline):
        print(f"[Mock Router] Swapping ETH for tokens {path}")
        return self

    def add_liquidity(self, token_a, token_b, amount_a_desired, amount_b_desired, amount_a_min, amount_b_min, to, deadline):
        print(f"[Mock Router] Adding liquidity")
        return self

    def remove_liquidity(self, token_a, token_b, liquidity, amount_a_min, amount_b_min, to, deadline):
        print(f"[Mock Router] Removing liquidity")
        return self

    def transact(self, *args, **kwargs):
        return HexBytes("0x000000000000000000000000000000000000000000000000000000000000beef")

class UniswapV2Factory:
    def __init__(self, w3, address):
        self.w3 = w3
        self.address = address

    def get_pair(self, token_a, token_b):
        return "0x000000000000000000000000000000000000dead"

# =================== Dummy Parameters ===================
class params:
    RECIPIENT_ADDRESS = "0x0000000000000000000000000000000000000002"
    NTN_ADDRESS = "0x0000000000000000000000000000000000000003"
    USDCX_ADDRESS = "0x0000000000000000000000000000000000000004"
    WATN_ADDRESS = "0x0000000000000000000000000000000000000005"
    UNISWAP_ROUTER_ADDRESS = "0x0000000000000000000000000000000000000006"
    UNISWAP_FACTORY_ADDRESS = "0x0000000000000000000000000000000000000007"

# =================== Task Definitions ===================
Task: TypeAlias = Callable[[Web3], None]
tasks: List[Task] = []

def transfer(w3: Web3) -> None:
    autonity = Autonity(w3)
    amount = int(0.01 * 10 ** autonity.decimals())
    tx = autonity.transfer(params.RECIPIENT_ADDRESS, amount).transact()
    w3.eth.wait_for_transaction_receipt(tx)

tasks.append(transfer)

def bond(w3: Web3) -> None:
    autonity = Autonity(w3)
    validator = autonity.get_validators()[0]
    amount = int(0.01 * 10 ** autonity.decimals())
    tx = autonity.bond(validator, amount).transact()
    w3.eth.wait_for_transaction_receipt(tx)

tasks.append(bond)

def unbond(w3: Web3) -> None:
    autonity = Autonity(w3)
    validator = autonity.get_validators()[0]
    amount = int(0.01 * 10 ** autonity.decimals())
    tx = autonity.unbond(validator, amount).transact()
    w3.eth.wait_for_transaction_receipt(tx)

tasks.append(unbond)

def approve(w3: Web3) -> None:
    autonity = Autonity(w3)
    amount = int(0.01 * 10 ** autonity.decimals())
    tx = autonity.approve(params.RECIPIENT_ADDRESS, amount).transact()
    w3.eth.wait_for_transaction_receipt(tx)

tasks.append(approve)

def swap_exact_tokens_for_tokens(w3: Web3) -> None:
    ntn = ERC20(w3, params.NTN_ADDRESS)
    amount = int(0.01 * 10 ** ntn.decimals())
    approve_tx = ntn.approve(params.UNISWAP_ROUTER_ADDRESS, amount).transact()
    w3.eth.wait_for_transaction_receipt(approve_tx)

    router = UniswapV2Router02(w3, params.UNISWAP_ROUTER_ADDRESS)
    sender = cast(ChecksumAddress, w3.eth.default_account)
    deadline = int(time.time()) + 10
    tx = router.swap_exact_tokens_for_tokens(amount, 0, [params.NTN_ADDRESS, params.USDCX_ADDRESS], sender, deadline).transact()
    w3.eth.wait_for_transaction_receipt(tx)

tasks.append(swap_exact_tokens_for_tokens)

def swap_exact_atn_for_ntn(w3: Web3) -> None:
    watn = ERC20(w3, params.WATN_ADDRESS)
    amount = int(0.01 * 10 ** watn.decimals())
    approve_tx = watn.approve(params.UNISWAP_ROUTER_ADDRESS, amount).transact()
    w3.eth.wait_for_transaction_receipt(approve_tx)

    router = UniswapV2Router02(w3, params.UNISWAP_ROUTER_ADDRESS)
    sender = cast(ChecksumAddress, w3.eth.default_account)
    deadline = int(time.time()) + 10
    tx = router.swap_exact_eth_for_tokens(0, [params.WATN_ADDRESS, params.NTN_ADDRESS], sender, deadline).transact({"value": amount})
    w3.eth.wait_for_transaction_receipt(tx)

tasks.append(swap_exact_atn_for_ntn)

def add_liquidity(w3: Web3) -> None:
    ntn = ERC20(w3, params.NTN_ADDRESS)
    usdc = ERC20(w3, params.USDCX_ADDRESS)

    amount_a = int(0.1 * 10 ** ntn.decimals())
    amount_b = int(0.01 * 10 ** usdc.decimals())

    w3.eth.wait_for_transaction_receipt(ntn.approve(params.UNISWAP_ROUTER_ADDRESS, amount_a).transact())
    w3.eth.wait_for_transaction_receipt(usdc.approve(params.UNISWAP_ROUTER_ADDRESS, amount_b).transact())

    router = UniswapV2Router02(w3, params.UNISWAP_ROUTER_ADDRESS)
    sender = cast(ChecksumAddress, w3.eth.default_account)
    deadline = int(time.time()) + 10
    tx = router.add_liquidity(params.NTN_ADDRESS, params.USDCX_ADDRESS, amount_a, amount_b, 0, 0, sender, deadline).transact()
    w3.eth.wait_for_transaction_receipt(tx)

tasks.append(add_liquidity)

def remove_liquidity(w3: Web3) -> None:
    factory = UniswapV2Factory(w3, params.UNISWAP_FACTORY_ADDRESS)
    pair_address = factory.get_pair(params.NTN_ADDRESS, params.USDCX_ADDRESS)

    pair = ERC20(w3, pair_address)
    sender = cast(ChecksumAddress, w3.eth.default_account)
    liquidity = pair.balance_of(sender)

    if liquidity > 0:
        w3.eth.wait_for_transaction_receipt(pair.approve(params.UNISWAP_ROUTER_ADDRESS, liquidity).transact())

        router = UniswapV2Router02(w3, params.UNISWAP_ROUTER_ADDRESS)
        deadline = int(time.time()) + 10
        tx = router.remove_liquidity(params.NTN_ADDRESS, params.USDCX_ADDRESS, liquidity, 0, 0, sender, deadline).transact()
        w3.eth.wait_for_transaction_receipt(tx)

tasks.append(remove_liquidity)

# =================== Main Mock Runner ===================
if __name__ == "__main__":
    w3 = MagicMock(spec=Web3)
    w3.eth = MagicMock()
    w3.eth.default_account = "0x000000000000000000000000000000000000abcd"
    w3.eth.accounts = [w3.eth.default_account]
    w3.eth.wait_for_transaction_receipt = lambda tx: print(f"[Mock] Tx receipt for {tx.hex()}")
    w3.eth.get_block = lambda _: {"timestamp": int(time.time())}

    print("=== Running All Tasks ===")
    for task in tasks:
        task(w3)
    print("=== All Tasks Completed ===")
