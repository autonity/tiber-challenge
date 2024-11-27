import logging
import os
import random

from web3 import HTTPProvider, Web3
from web3.exceptions import ContractLogicError
from web3.middleware.signing import construct_sign_and_send_raw_middleware

from .params import RPC_URL
from .tasks import tasks

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("starter_kit")

w3 = Web3(HTTPProvider(RPC_URL))

sender_account = w3.eth.account.from_key(os.environ["SENDER_PRIVATE_KEY"])
w3.eth.default_account = sender_account.address

# Set `sender_account` as the signer of all transactions
signer_middleware = construct_sign_and_send_raw_middleware(sender_account)
w3.middleware_onion.add(signer_middleware)

for _ in range(10_000):
    task = random.choice(tasks)
    logger.info(task.__name__)
    try:
        task(w3)
    except ContractLogicError as e:
        # Contract execution reverted
        logger.warning(e)
