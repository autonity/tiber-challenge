"""UniswapV2Factory contract binding and data structures."""

### THIS FILE HAS BEEN AUTO-GENERATED, DO NOT MODIFY IT ###

import typing

import eth_typing
import hexbytes
import web3
from web3.contract import base_contract, contract


class UniswapV2Factory:
    """UniswapV2Factory contract binding.

    Parameters
    ----------
    w3 : web3.Web3
    address : eth_typing.ChecksumAddress
        The address of a deployed UniswapV2Factory contract.
    """

    _contract: contract.Contract

    def __init__(
        self,
        w3: web3.Web3,
        address: eth_typing.ChecksumAddress,
    ):
        self._contract = w3.eth.contract(
            address=address,
            abi=ABI,
        )

    @property
    def PairCreated(self) -> typing.Type[base_contract.BaseContractEvent]:
        """Binding for `event PairCreated` on the UniswapV2Factory contract."""
        return self._contract.events.PairCreated

    def init_code_hash(
        self,
    ) -> hexbytes.HexBytes:
        """Binding for `INIT_CODE_HASH` on the UniswapV2Factory contract.

        Returns
        -------
        hexbytes.HexBytes
        """
        return_value = self._contract.functions.INIT_CODE_HASH().call()
        return hexbytes.HexBytes(return_value)

    def all_pairs(
        self,
        key0: int,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `allPairs` on the UniswapV2Factory contract.

        Parameters
        ----------
        key0 : int

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.allPairs(
            key0,
        ).call()
        return eth_typing.ChecksumAddress(return_value)

    def all_pairs_length(
        self,
    ) -> int:
        """Binding for `allPairsLength` on the UniswapV2Factory contract.

        Returns
        -------
        int
        """
        return_value = self._contract.functions.allPairsLength().call()
        return int(return_value)

    def create_pair(
        self,
        token_a: eth_typing.ChecksumAddress,
        token_b: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `createPair` on the UniswapV2Factory contract.

        Parameters
        ----------
        token_a : eth_typing.ChecksumAddress
        token_b : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.createPair(
            token_a,
            token_b,
        )

    def fee_to(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `feeTo` on the UniswapV2Factory contract.

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.feeTo().call()
        return eth_typing.ChecksumAddress(return_value)

    def fee_to_setter(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `feeToSetter` on the UniswapV2Factory contract.

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.feeToSetter().call()
        return eth_typing.ChecksumAddress(return_value)

    def get_pair(
        self,
        key0: eth_typing.ChecksumAddress,
        key1: eth_typing.ChecksumAddress,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `getPair` on the UniswapV2Factory contract.

        Parameters
        ----------
        key0 : eth_typing.ChecksumAddress
        key1 : eth_typing.ChecksumAddress

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.getPair(
            key0,
            key1,
        ).call()
        return eth_typing.ChecksumAddress(return_value)

    def set_fee_to(
        self,
        _fee_to: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setFeeTo` on the UniswapV2Factory contract.

        Parameters
        ----------
        _fee_to : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setFeeTo(
            _fee_to,
        )

    def set_fee_to_setter(
        self,
        _fee_to_setter: eth_typing.ChecksumAddress,
    ) -> contract.ContractFunction:
        """Binding for `setFeeToSetter` on the UniswapV2Factory contract.

        Parameters
        ----------
        _fee_to_setter : eth_typing.ChecksumAddress

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.setFeeToSetter(
            _fee_to_setter,
        )


ABI = typing.cast(
    eth_typing.ABI,
    [
        {
            "inputs": [
                {"internalType": "address", "name": "_feeToSetter", "type": "address"}
            ],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "token0",
                    "type": "address",
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "token1",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "address",
                    "name": "pair",
                    "type": "address",
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256",
                },
            ],
            "name": "PairCreated",
            "type": "event",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "INIT_CODE_HASH",
            "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "name": "allPairs",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "allPairsLength",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": False,
            "inputs": [
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
            ],
            "name": "createPair",
            "outputs": [{"internalType": "address", "name": "pair", "type": "address"}],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "feeTo",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [],
            "name": "feeToSetter",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": True,
            "inputs": [
                {"internalType": "address", "name": "", "type": "address"},
                {"internalType": "address", "name": "", "type": "address"},
            ],
            "name": "getPair",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function",
        },
        {
            "constant": False,
            "inputs": [
                {"internalType": "address", "name": "_feeTo", "type": "address"}
            ],
            "name": "setFeeTo",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "constant": False,
            "inputs": [
                {"internalType": "address", "name": "_feeToSetter", "type": "address"}
            ],
            "name": "setFeeToSetter",
            "outputs": [],
            "payable": False,
            "stateMutability": "nonpayable",
            "type": "function",
        },
    ],
)
