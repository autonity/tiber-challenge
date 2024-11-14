import random
from typing import Callable, List, Tuple, TypeAlias, cast

from autonity import Autonity, ERC20
from eth_typing import ChecksumAddress
from web3 import Web3

from . import params
from .bindings.uniswap_v2_router_02 import UniswapV2Router02

Task: TypeAlias = Callable[[Web3], None]

tasks: List[Task] = []

stakes: List[Tuple[ChecksumAddress, int]] = []


def task(f: Task) -> Task:
    """Decorator that registers 'task' functions."""
    tasks.append(f)
    return f


@task
def transfer(w3: Web3) -> None:
    """Transfers 0.1 NTN to a recipient specified in .env."""
    autonity = Autonity(w3)
    amount = int(0.1 * 10 ** autonity.decimals())
    tx = autonity.transfer(params.RECIPIENT_ADDRESS, amount).transact()
    w3.eth.wait_for_transaction_receipt(tx)


@task
def bond(w3: Web3) -> None:
    """Bonds 0.1 NTN to a random validator."""
    autonity = Autonity(w3)
    validator_address = random.choice(autonity.get_validators())
    amount = int(0.1 * 10 ** autonity.decimals())
    tx = autonity.bond(validator_address, amount).transact()
    w3.eth.wait_for_transaction_receipt(tx)
    stakes.append((validator_address, amount))


@task
def unbond(w3: Web3) -> None:
    """Unbonds some of the stake previously bonded."""
    if stakes:
        autonity = Autonity(w3)
        validator_address, amount = random.choice(stakes)
        tx = autonity.unbond(validator_address, amount).transact()
        w3.eth.wait_for_transaction_receipt(tx)


@task
def approve(w3: Web3) -> None:
    """Approves the transfer of 0.1 NTN by a recipient specified in .env."""
    autonity = Autonity(w3)
    amount = int(0.1 * 10 ** autonity.decimals())
    tx = autonity.approve(params.RECIPIENT_ADDRESS, amount).transact()
    w3.eth.wait_for_transaction_receipt(tx)


@task
def change_comission_rate(w3: Web3) -> None:
    """Changes commission rate to a random value betwen 0% and 100%."""
    autonity = Autonity(w3)
    rate = random.randint(0, 10000)
    tx = autonity.change_commission_rate(params.OWN_VALIDATOR_ADDRESS, rate).transact()
    w3.eth.wait_for_transaction_receipt(tx)


@task
def pause_validator(w3: Web3) -> None:
    """Pauses the sender's validator."""
    autonity = Autonity(w3)
    tx = autonity.pause_validator(params.OWN_VALIDATOR_ADDRESS).transact()
    w3.eth.wait_for_transaction_receipt(tx)


@task
def activate_validator(w3: Web3) -> None:
    """Activates the sender's validator."""
    autonity = Autonity(w3)
    tx = autonity.activate_validator(params.OWN_VALIDATOR_ADDRESS).transact()
    w3.eth.wait_for_transaction_receipt(tx)


@task
def swap_exact_tokens_for_tokens(w3: Web3) -> None:
    """Swaps 0.1 USDC for NTN."""
    usdc = ERC20(w3, params.USDC_ADDRESS)
    usdc_amount = int(0.1 * 10 ** usdc.decimals())
    approve_tx = usdc.approve(params.UNISWAP_ROUTER_ADDRESS, usdc_amount).transact()
    w3.eth.wait_for_transaction_receipt(approve_tx)

    uniswap_router = UniswapV2Router02(w3, params.UNISWAP_ROUTER_ADDRESS)
    sender_address = cast(ChecksumAddress, w3.eth.default_account)
    deadline = w3.eth.get_block("latest").timestamp + 10  # type: ignore
    swap_tx = uniswap_router.swap_exact_tokens_for_tokens(
        amount_in=usdc_amount,
        amount_out_min=0,
        path=[params.USDC_ADDRESS, params.NTN_ADDRESS],
        to=sender_address,
        deadline=deadline,
    ).transact()
    w3.eth.wait_for_transaction_receipt(swap_tx)


@task
def add_liquidity(w3: Web3) -> None:
    """Adds 1 NTN and 0.1 USDC to the Uniswap liquidity pool."""
    ntn = ERC20(w3, params.NTN_ADDRESS)
    ntn_amount = int(1 * 10 ** ntn.decimals())
    approve_tx_2 = ntn.approve(params.UNISWAP_ROUTER_ADDRESS, ntn_amount).transact()
    w3.eth.wait_for_transaction_receipt(approve_tx_2)

    usdc = ERC20(w3, params.USDC_ADDRESS)
    usdc_amount = int(0.1 * 10 ** usdc.decimals())
    approve_tx_1 = usdc.approve(params.UNISWAP_ROUTER_ADDRESS, usdc_amount).transact()
    w3.eth.wait_for_transaction_receipt(approve_tx_1)

    uniswap_router = UniswapV2Router02(w3, params.UNISWAP_ROUTER_ADDRESS)
    sender_address = cast(ChecksumAddress, w3.eth.default_account)
    deadline = w3.eth.get_block("latest").timestamp + 10  # type: ignore
    add_liquidity_tx = uniswap_router.add_liquidity(
        token_a=params.NTN_ADDRESS,
        token_b=params.USDC_ADDRESS,
        amount_a_desired=ntn_amount,
        amount_b_desired=usdc_amount,
        amount_a_min=0,
        amount_b_min=0,
        to=sender_address,
        deadline=deadline,
    ).transact()
    w3.eth.wait_for_transaction_receipt(add_liquidity_tx)


@task
def remove_liquidity(w3: Web3) -> None:
    """Removes all funds from the Uniswap liquidity pool."""
    uniswap_ntn_usdc_pair = ERC20(w3, params.UNISWAP_NTN_USDC_PAIR_ADDRESS)
    sender_address = cast(ChecksumAddress, w3.eth.default_account)
    liquidity_amount = uniswap_ntn_usdc_pair.balance_of(sender_address)

    if liquidity_amount > 0:
        approve_tx = uniswap_ntn_usdc_pair.approve(
            params.UNISWAP_ROUTER_ADDRESS, liquidity_amount
        ).transact()
        w3.eth.wait_for_transaction_receipt(approve_tx)

        uniswap_router = UniswapV2Router02(w3, params.UNISWAP_ROUTER_ADDRESS)
        deadline = w3.eth.get_block("latest").timestamp + 10  # type: ignore
        remove_liquidity_tx = uniswap_router.remove_liquidity(
            token_a=params.NTN_ADDRESS,
            token_b=params.USDC_ADDRESS,
            liquidity=liquidity_amount,
            amount_a_min=0,
            amount_b_min=0,
            to=sender_address,
            deadline=deadline,
        ).transact()
        w3.eth.wait_for_transaction_receipt(remove_liquidity_tx)
