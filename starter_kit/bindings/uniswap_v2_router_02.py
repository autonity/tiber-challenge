"""UniswapV2Router02 contract binding and data structures."""

### THIS FILE HAS BEEN AUTO-GENERATED, DO NOT MODIFY IT ###

import typing

import eth_typing
import hexbytes
import web3
from web3.contract import contract


class UniswapV2Router02:
    """UniswapV2Router02 contract binding.

    Parameters
    ----------
    w3 : web3.Web3
    """

    _contract: contract.Contract

    def __init__(
        self,
        w3: web3.Web3,
        address: eth_typing.ChecksumAddress,
    ):
        self._contract = w3.eth.contract(address=address, abi=ABI)

    def weth(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `WETH` on the UniswapV2Router02 contract.

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.WETH().call()
        return eth_typing.ChecksumAddress(return_value)

    def add_liquidity(
        self,
        token_a: eth_typing.ChecksumAddress,
        token_b: eth_typing.ChecksumAddress,
        amount_a_desired: int,
        amount_b_desired: int,
        amount_a_min: int,
        amount_b_min: int,
        to: eth_typing.ChecksumAddress,
        deadline: int,
    ) -> contract.ContractFunction:
        """Binding for `addLiquidity` on the UniswapV2Router02 contract.

        Parameters
        ----------
        token_a : eth_typing.ChecksumAddress
        token_b : eth_typing.ChecksumAddress
        amount_a_desired : int
        amount_b_desired : int
        amount_a_min : int
        amount_b_min : int
        to : eth_typing.ChecksumAddress
        deadline : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.addLiquidity(
            token_a,
            token_b,
            amount_a_desired,
            amount_b_desired,
            amount_a_min,
            amount_b_min,
            to,
            deadline,
        )

    def add_liquidity_eth(
        self,
        token: eth_typing.ChecksumAddress,
        amount_token_desired: int,
        amount_token_min: int,
        amount_eth_min: int,
        to: eth_typing.ChecksumAddress,
        deadline: int,
    ) -> contract.ContractFunction:
        """Binding for `addLiquidityETH` on the UniswapV2Router02 contract.

        Parameters
        ----------
        token : eth_typing.ChecksumAddress
        amount_token_desired : int
        amount_token_min : int
        amount_eth_min : int
        to : eth_typing.ChecksumAddress
        deadline : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.addLiquidityETH(
            token,
            amount_token_desired,
            amount_token_min,
            amount_eth_min,
            to,
            deadline,
        )

    def factory(
        self,
    ) -> eth_typing.ChecksumAddress:
        """Binding for `factory` on the UniswapV2Router02 contract.

        Returns
        -------
        eth_typing.ChecksumAddress
        """
        return_value = self._contract.functions.factory().call()
        return eth_typing.ChecksumAddress(return_value)

    def get_amount_in(
        self,
        amount_out: int,
        reserve_in: int,
        reserve_out: int,
    ) -> int:
        """Binding for `getAmountIn` on the UniswapV2Router02 contract.

        Parameters
        ----------
        amount_out : int
        reserve_in : int
        reserve_out : int

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getAmountIn(
            amount_out,
            reserve_in,
            reserve_out,
        ).call()
        return int(return_value)

    def get_amount_out(
        self,
        amount_in: int,
        reserve_in: int,
        reserve_out: int,
    ) -> int:
        """Binding for `getAmountOut` on the UniswapV2Router02 contract.

        Parameters
        ----------
        amount_in : int
        reserve_in : int
        reserve_out : int

        Returns
        -------
        int
        """
        return_value = self._contract.functions.getAmountOut(
            amount_in,
            reserve_in,
            reserve_out,
        ).call()
        return int(return_value)

    def get_amounts_in(
        self,
        amount_out: int,
        path: typing.List[eth_typing.ChecksumAddress],
    ) -> typing.List[int]:
        """Binding for `getAmountsIn` on the UniswapV2Router02 contract.

        Parameters
        ----------
        amount_out : int
        path : typing.List[eth_typing.ChecksumAddress]

        Returns
        -------
        typing.List[int]
        """
        return_value = self._contract.functions.getAmountsIn(
            amount_out,
            path,
        ).call()
        return [int(return_value_elem) for return_value_elem in return_value]

    def get_amounts_out(
        self,
        amount_in: int,
        path: typing.List[eth_typing.ChecksumAddress],
    ) -> typing.List[int]:
        """Binding for `getAmountsOut` on the UniswapV2Router02 contract.

        Parameters
        ----------
        amount_in : int
        path : typing.List[eth_typing.ChecksumAddress]

        Returns
        -------
        typing.List[int]
        """
        return_value = self._contract.functions.getAmountsOut(
            amount_in,
            path,
        ).call()
        return [int(return_value_elem) for return_value_elem in return_value]

    def quote(
        self,
        amount_a: int,
        reserve_a: int,
        reserve_b: int,
    ) -> int:
        """Binding for `quote` on the UniswapV2Router02 contract.

        Parameters
        ----------
        amount_a : int
        reserve_a : int
        reserve_b : int

        Returns
        -------
        int
        """
        return_value = self._contract.functions.quote(
            amount_a,
            reserve_a,
            reserve_b,
        ).call()
        return int(return_value)

    def remove_liquidity(
        self,
        token_a: eth_typing.ChecksumAddress,
        token_b: eth_typing.ChecksumAddress,
        liquidity: int,
        amount_a_min: int,
        amount_b_min: int,
        to: eth_typing.ChecksumAddress,
        deadline: int,
    ) -> contract.ContractFunction:
        """Binding for `removeLiquidity` on the UniswapV2Router02 contract.

        Parameters
        ----------
        token_a : eth_typing.ChecksumAddress
        token_b : eth_typing.ChecksumAddress
        liquidity : int
        amount_a_min : int
        amount_b_min : int
        to : eth_typing.ChecksumAddress
        deadline : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.removeLiquidity(
            token_a,
            token_b,
            liquidity,
            amount_a_min,
            amount_b_min,
            to,
            deadline,
        )

    def remove_liquidity_eth(
        self,
        token: eth_typing.ChecksumAddress,
        liquidity: int,
        amount_token_min: int,
        amount_eth_min: int,
        to: eth_typing.ChecksumAddress,
        deadline: int,
    ) -> contract.ContractFunction:
        """Binding for `removeLiquidityETH` on the UniswapV2Router02 contract.

        Parameters
        ----------
        token : eth_typing.ChecksumAddress
        liquidity : int
        amount_token_min : int
        amount_eth_min : int
        to : eth_typing.ChecksumAddress
        deadline : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.removeLiquidityETH(
            token,
            liquidity,
            amount_token_min,
            amount_eth_min,
            to,
            deadline,
        )

    def remove_liquidity_eth_supporting_fee_on_transfer_tokens(
        self,
        token: eth_typing.ChecksumAddress,
        liquidity: int,
        amount_token_min: int,
        amount_eth_min: int,
        to: eth_typing.ChecksumAddress,
        deadline: int,
    ) -> contract.ContractFunction:
        """Binding for `removeLiquidityETHSupportingFeeOnTransferTokens` on the UniswapV2Router02 contract.

        Parameters
        ----------
        token : eth_typing.ChecksumAddress
        liquidity : int
        amount_token_min : int
        amount_eth_min : int
        to : eth_typing.ChecksumAddress
        deadline : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.removeLiquidityETHSupportingFeeOnTransferTokens(
            token,
            liquidity,
            amount_token_min,
            amount_eth_min,
            to,
            deadline,
        )

    def remove_liquidity_eth_with_permit(
        self,
        token: eth_typing.ChecksumAddress,
        liquidity: int,
        amount_token_min: int,
        amount_eth_min: int,
        to: eth_typing.ChecksumAddress,
        deadline: int,
        approve_max: bool,
        v: int,
        r: hexbytes.HexBytes,
        s: hexbytes.HexBytes,
    ) -> contract.ContractFunction:
        """Binding for `removeLiquidityETHWithPermit` on the UniswapV2Router02 contract.

        Parameters
        ----------
        token : eth_typing.ChecksumAddress
        liquidity : int
        amount_token_min : int
        amount_eth_min : int
        to : eth_typing.ChecksumAddress
        deadline : int
        approve_max : bool
        v : int
        r : hexbytes.HexBytes
        s : hexbytes.HexBytes

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.removeLiquidityETHWithPermit(
            token,
            liquidity,
            amount_token_min,
            amount_eth_min,
            to,
            deadline,
            approve_max,
            v,
            r,
            s,
        )

    def remove_liquidity_eth_with_permit_supporting_fee_on_transfer_tokens(
        self,
        token: eth_typing.ChecksumAddress,
        liquidity: int,
        amount_token_min: int,
        amount_eth_min: int,
        to: eth_typing.ChecksumAddress,
        deadline: int,
        approve_max: bool,
        v: int,
        r: hexbytes.HexBytes,
        s: hexbytes.HexBytes,
    ) -> contract.ContractFunction:
        """Binding for `removeLiquidityETHWithPermitSupportingFeeOnTransferTokens` on the UniswapV2Router02 contract.

        Parameters
        ----------
        token : eth_typing.ChecksumAddress
        liquidity : int
        amount_token_min : int
        amount_eth_min : int
        to : eth_typing.ChecksumAddress
        deadline : int
        approve_max : bool
        v : int
        r : hexbytes.HexBytes
        s : hexbytes.HexBytes

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.removeLiquidityETHWithPermitSupportingFeeOnTransferTokens(
            token,
            liquidity,
            amount_token_min,
            amount_eth_min,
            to,
            deadline,
            approve_max,
            v,
            r,
            s,
        )

    def remove_liquidity_with_permit(
        self,
        token_a: eth_typing.ChecksumAddress,
        token_b: eth_typing.ChecksumAddress,
        liquidity: int,
        amount_a_min: int,
        amount_b_min: int,
        to: eth_typing.ChecksumAddress,
        deadline: int,
        approve_max: bool,
        v: int,
        r: hexbytes.HexBytes,
        s: hexbytes.HexBytes,
    ) -> contract.ContractFunction:
        """Binding for `removeLiquidityWithPermit` on the UniswapV2Router02 contract.

        Parameters
        ----------
        token_a : eth_typing.ChecksumAddress
        token_b : eth_typing.ChecksumAddress
        liquidity : int
        amount_a_min : int
        amount_b_min : int
        to : eth_typing.ChecksumAddress
        deadline : int
        approve_max : bool
        v : int
        r : hexbytes.HexBytes
        s : hexbytes.HexBytes

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.removeLiquidityWithPermit(
            token_a,
            token_b,
            liquidity,
            amount_a_min,
            amount_b_min,
            to,
            deadline,
            approve_max,
            v,
            r,
            s,
        )

    def swap_eth_for_exact_tokens(
        self,
        amount_out: int,
        path: typing.List[eth_typing.ChecksumAddress],
        to: eth_typing.ChecksumAddress,
        deadline: int,
    ) -> contract.ContractFunction:
        """Binding for `swapETHForExactTokens` on the UniswapV2Router02 contract.

        Parameters
        ----------
        amount_out : int
        path : typing.List[eth_typing.ChecksumAddress]
        to : eth_typing.ChecksumAddress
        deadline : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.swapETHForExactTokens(
            amount_out,
            path,
            to,
            deadline,
        )

    def swap_exact_eth_for_tokens(
        self,
        amount_out_min: int,
        path: typing.List[eth_typing.ChecksumAddress],
        to: eth_typing.ChecksumAddress,
        deadline: int,
    ) -> contract.ContractFunction:
        """Binding for `swapExactETHForTokens` on the UniswapV2Router02 contract.

        Parameters
        ----------
        amount_out_min : int
        path : typing.List[eth_typing.ChecksumAddress]
        to : eth_typing.ChecksumAddress
        deadline : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.swapExactETHForTokens(
            amount_out_min,
            path,
            to,
            deadline,
        )

    def swap_exact_eth_for_tokens_supporting_fee_on_transfer_tokens(
        self,
        amount_out_min: int,
        path: typing.List[eth_typing.ChecksumAddress],
        to: eth_typing.ChecksumAddress,
        deadline: int,
    ) -> contract.ContractFunction:
        """Binding for `swapExactETHForTokensSupportingFeeOnTransferTokens` on the UniswapV2Router02 contract.

        Parameters
        ----------
        amount_out_min : int
        path : typing.List[eth_typing.ChecksumAddress]
        to : eth_typing.ChecksumAddress
        deadline : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return (
            self._contract.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(
                amount_out_min,
                path,
                to,
                deadline,
            )
        )

    def swap_exact_tokens_for_eth(
        self,
        amount_in: int,
        amount_out_min: int,
        path: typing.List[eth_typing.ChecksumAddress],
        to: eth_typing.ChecksumAddress,
        deadline: int,
    ) -> contract.ContractFunction:
        """Binding for `swapExactTokensForETH` on the UniswapV2Router02 contract.

        Parameters
        ----------
        amount_in : int
        amount_out_min : int
        path : typing.List[eth_typing.ChecksumAddress]
        to : eth_typing.ChecksumAddress
        deadline : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.swapExactTokensForETH(
            amount_in,
            amount_out_min,
            path,
            to,
            deadline,
        )

    def swap_exact_tokens_for_eth_supporting_fee_on_transfer_tokens(
        self,
        amount_in: int,
        amount_out_min: int,
        path: typing.List[eth_typing.ChecksumAddress],
        to: eth_typing.ChecksumAddress,
        deadline: int,
    ) -> contract.ContractFunction:
        """Binding for `swapExactTokensForETHSupportingFeeOnTransferTokens` on the UniswapV2Router02 contract.

        Parameters
        ----------
        amount_in : int
        amount_out_min : int
        path : typing.List[eth_typing.ChecksumAddress]
        to : eth_typing.ChecksumAddress
        deadline : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return (
            self._contract.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(
                amount_in,
                amount_out_min,
                path,
                to,
                deadline,
            )
        )

    def swap_exact_tokens_for_tokens(
        self,
        amount_in: int,
        amount_out_min: int,
        path: typing.List[eth_typing.ChecksumAddress],
        to: eth_typing.ChecksumAddress,
        deadline: int,
    ) -> contract.ContractFunction:
        """Binding for `swapExactTokensForTokens` on the UniswapV2Router02 contract.

        Parameters
        ----------
        amount_in : int
        amount_out_min : int
        path : typing.List[eth_typing.ChecksumAddress]
        to : eth_typing.ChecksumAddress
        deadline : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.swapExactTokensForTokens(
            amount_in,
            amount_out_min,
            path,
            to,
            deadline,
        )

    def swap_exact_tokens_for_tokens_supporting_fee_on_transfer_tokens(
        self,
        amount_in: int,
        amount_out_min: int,
        path: typing.List[eth_typing.ChecksumAddress],
        to: eth_typing.ChecksumAddress,
        deadline: int,
    ) -> contract.ContractFunction:
        """Binding for `swapExactTokensForTokensSupportingFeeOnTransferTokens` on the UniswapV2Router02 contract.

        Parameters
        ----------
        amount_in : int
        amount_out_min : int
        path : typing.List[eth_typing.ChecksumAddress]
        to : eth_typing.ChecksumAddress
        deadline : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(
            amount_in,
            amount_out_min,
            path,
            to,
            deadline,
        )

    def swap_tokens_for_exact_eth(
        self,
        amount_out: int,
        amount_in_max: int,
        path: typing.List[eth_typing.ChecksumAddress],
        to: eth_typing.ChecksumAddress,
        deadline: int,
    ) -> contract.ContractFunction:
        """Binding for `swapTokensForExactETH` on the UniswapV2Router02 contract.

        Parameters
        ----------
        amount_out : int
        amount_in_max : int
        path : typing.List[eth_typing.ChecksumAddress]
        to : eth_typing.ChecksumAddress
        deadline : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.swapTokensForExactETH(
            amount_out,
            amount_in_max,
            path,
            to,
            deadline,
        )

    def swap_tokens_for_exact_tokens(
        self,
        amount_out: int,
        amount_in_max: int,
        path: typing.List[eth_typing.ChecksumAddress],
        to: eth_typing.ChecksumAddress,
        deadline: int,
    ) -> contract.ContractFunction:
        """Binding for `swapTokensForExactTokens` on the UniswapV2Router02 contract.

        Parameters
        ----------
        amount_out : int
        amount_in_max : int
        path : typing.List[eth_typing.ChecksumAddress]
        to : eth_typing.ChecksumAddress
        deadline : int

        Returns
        -------
        web3.contract.contract.ContractFunction
            A contract function instance to be sent in a transaction.
        """
        return self._contract.functions.swapTokensForExactTokens(
            amount_out,
            amount_in_max,
            path,
            to,
            deadline,
        )


ABI = typing.cast(
    eth_typing.ABI,
    [
        {
            "inputs": [
                {"internalType": "address", "name": "_factory", "type": "address"},
                {"internalType": "address", "name": "_WETH", "type": "address"},
            ],
            "stateMutability": "nonpayable",
            "type": "constructor",
        },
        {
            "inputs": [],
            "name": "WETH",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
                {
                    "internalType": "uint256",
                    "name": "amountADesired",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "amountBDesired",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
                {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "addLiquidity",
            "outputs": [
                {"internalType": "uint256", "name": "amountA", "type": "uint256"},
                {"internalType": "uint256", "name": "amountB", "type": "uint256"},
                {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "token", "type": "address"},
                {
                    "internalType": "uint256",
                    "name": "amountTokenDesired",
                    "type": "uint256",
                },
                {
                    "internalType": "uint256",
                    "name": "amountTokenMin",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "addLiquidityETH",
            "outputs": [
                {"internalType": "uint256", "name": "amountToken", "type": "uint256"},
                {"internalType": "uint256", "name": "amountETH", "type": "uint256"},
                {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "factory",
            "outputs": [{"internalType": "address", "name": "", "type": "address"}],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                {"internalType": "uint256", "name": "reserveIn", "type": "uint256"},
                {"internalType": "uint256", "name": "reserveOut", "type": "uint256"},
            ],
            "name": "getAmountIn",
            "outputs": [
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"}
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                {"internalType": "uint256", "name": "reserveIn", "type": "uint256"},
                {"internalType": "uint256", "name": "reserveOut", "type": "uint256"},
            ],
            "name": "getAmountOut",
            "outputs": [
                {"internalType": "uint256", "name": "amountOut", "type": "uint256"}
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                {"internalType": "address[]", "name": "path", "type": "address[]"},
            ],
            "name": "getAmountsIn",
            "outputs": [
                {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                {"internalType": "address[]", "name": "path", "type": "address[]"},
            ],
            "name": "getAmountsOut",
            "outputs": [
                {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
            ],
            "stateMutability": "view",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountA", "type": "uint256"},
                {"internalType": "uint256", "name": "reserveA", "type": "uint256"},
                {"internalType": "uint256", "name": "reserveB", "type": "uint256"},
            ],
            "name": "quote",
            "outputs": [
                {"internalType": "uint256", "name": "amountB", "type": "uint256"}
            ],
            "stateMutability": "pure",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
                {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
                {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "removeLiquidity",
            "outputs": [
                {"internalType": "uint256", "name": "amountA", "type": "uint256"},
                {"internalType": "uint256", "name": "amountB", "type": "uint256"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "token", "type": "address"},
                {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "amountTokenMin",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "removeLiquidityETH",
            "outputs": [
                {"internalType": "uint256", "name": "amountToken", "type": "uint256"},
                {"internalType": "uint256", "name": "amountETH", "type": "uint256"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "token", "type": "address"},
                {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "amountTokenMin",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "removeLiquidityETHSupportingFeeOnTransferTokens",
            "outputs": [
                {"internalType": "uint256", "name": "amountETH", "type": "uint256"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "token", "type": "address"},
                {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "amountTokenMin",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                {"internalType": "bool", "name": "approveMax", "type": "bool"},
                {"internalType": "uint8", "name": "v", "type": "uint8"},
                {"internalType": "bytes32", "name": "r", "type": "bytes32"},
                {"internalType": "bytes32", "name": "s", "type": "bytes32"},
            ],
            "name": "removeLiquidityETHWithPermit",
            "outputs": [
                {"internalType": "uint256", "name": "amountToken", "type": "uint256"},
                {"internalType": "uint256", "name": "amountETH", "type": "uint256"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "token", "type": "address"},
                {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                {
                    "internalType": "uint256",
                    "name": "amountTokenMin",
                    "type": "uint256",
                },
                {"internalType": "uint256", "name": "amountETHMin", "type": "uint256"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                {"internalType": "bool", "name": "approveMax", "type": "bool"},
                {"internalType": "uint8", "name": "v", "type": "uint8"},
                {"internalType": "bytes32", "name": "r", "type": "bytes32"},
                {"internalType": "bytes32", "name": "s", "type": "bytes32"},
            ],
            "name": "removeLiquidityETHWithPermitSupportingFeeOnTransferTokens",
            "outputs": [
                {"internalType": "uint256", "name": "amountETH", "type": "uint256"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "address", "name": "tokenA", "type": "address"},
                {"internalType": "address", "name": "tokenB", "type": "address"},
                {"internalType": "uint256", "name": "liquidity", "type": "uint256"},
                {"internalType": "uint256", "name": "amountAMin", "type": "uint256"},
                {"internalType": "uint256", "name": "amountBMin", "type": "uint256"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
                {"internalType": "bool", "name": "approveMax", "type": "bool"},
                {"internalType": "uint8", "name": "v", "type": "uint8"},
                {"internalType": "bytes32", "name": "r", "type": "bytes32"},
                {"internalType": "bytes32", "name": "s", "type": "bytes32"},
            ],
            "name": "removeLiquidityWithPermit",
            "outputs": [
                {"internalType": "uint256", "name": "amountA", "type": "uint256"},
                {"internalType": "uint256", "name": "amountB", "type": "uint256"},
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                {"internalType": "address[]", "name": "path", "type": "address[]"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "swapETHForExactTokens",
            "outputs": [
                {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                {"internalType": "address[]", "name": "path", "type": "address[]"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "swapExactETHForTokens",
            "outputs": [
                {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
            ],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                {"internalType": "address[]", "name": "path", "type": "address[]"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "swapExactETHForTokensSupportingFeeOnTransferTokens",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                {"internalType": "address[]", "name": "path", "type": "address[]"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "swapExactTokensForETH",
            "outputs": [
                {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                {"internalType": "address[]", "name": "path", "type": "address[]"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "swapExactTokensForETHSupportingFeeOnTransferTokens",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                {"internalType": "address[]", "name": "path", "type": "address[]"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "swapExactTokensForTokens",
            "outputs": [
                {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountIn", "type": "uint256"},
                {"internalType": "uint256", "name": "amountOutMin", "type": "uint256"},
                {"internalType": "address[]", "name": "path", "type": "address[]"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "swapExactTokensForTokensSupportingFeeOnTransferTokens",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                {"internalType": "uint256", "name": "amountInMax", "type": "uint256"},
                {"internalType": "address[]", "name": "path", "type": "address[]"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "swapTokensForExactETH",
            "outputs": [
                {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [
                {"internalType": "uint256", "name": "amountOut", "type": "uint256"},
                {"internalType": "uint256", "name": "amountInMax", "type": "uint256"},
                {"internalType": "address[]", "name": "path", "type": "address[]"},
                {"internalType": "address", "name": "to", "type": "address"},
                {"internalType": "uint256", "name": "deadline", "type": "uint256"},
            ],
            "name": "swapTokensForExactTokens",
            "outputs": [
                {"internalType": "uint256[]", "name": "amounts", "type": "uint256[]"}
            ],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {"stateMutability": "payable", "type": "receive"},
    ],
)
