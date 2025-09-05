from web3 import Web3
from dotenv import load_dotenv
from eth_account import Account
from pathlib import Path
import os

# ✅ Load environment variables from .env file in current folder
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# ✅ Read and validate variables
RPC_URL = os.getenv("RPC_URL", "").strip().rstrip("/")
PRIVATE_KEY = os.getenv("SENDER_PRIVATE_KEY", "").strip()
RECIPIENT = os.getenv("RECIPIENT_ADDRESS", "").strip()

# ✅ Ensure all values are provided
missing = []
if not RPC_URL: missing.append("RPC_URL")
if not PRIVATE_KEY: missing.append("SENDER_PRIVATE_KEY")
if not RECIPIENT: missing.append("RECIPIENT_ADDRESS")
if missing:
    raise ValueError(f"⚠️ Missing variables in .env: {', '.join(missing)}")

# ✅ Setup Web3
w3 = Web3(Web3.HTTPProvider(RPC_URL))
print(f"🔌 Connecting to RPC: {RPC_URL}")
if not w3.is_connected():
    raise ConnectionError("🚫 Failed to connect to the RPC provider.")

# ✅ Addresses and contracts
try:
    sender_address = Account.from_key(PRIVATE_KEY).address
    recipient_address = Web3.to_checksum_address(RECIPIENT)
except Exception as e:
    raise ValueError(f"❌ Invalid private key or address: {e}")

USDCX_ADDRESS = Web3.to_checksum_address("0xB855D5e83363A4494e09f0Bb3152A70d3f161940")  # USDCx on Piccadilly

USDCX_ABI = [
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"}
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function"
    }
]

def transfer_usdcx():
    print("🚀 Preparing transaction to transfer 1 USDCx...")

    contract = w3.eth.contract(address=USDCX_ADDRESS, abi=USDCX_ABI)
    nonce = w3.eth.get_transaction_count(sender_address)
    amount = 1_000_000  # 1 USDCx (6 decimals)

    transaction = contract.functions.transfer(
        recipient_address, amount
    ).build_transaction({
        "chainId": 201804,
        "from": sender_address,
        "nonce": nonce,
        "gas": 200000,
        "gasPrice": w3.to_wei("0.5", "gwei"),
    })

    signed_tx = w3.eth.account.sign_transaction(transaction, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("✅ Transaction sent successfully!")
    print("🔗 Tx Hash:", w3.to_hex(tx_hash))

if __name__ == "__main__":
    transfer_usdcx()
