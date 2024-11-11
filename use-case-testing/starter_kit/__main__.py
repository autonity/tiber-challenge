import logging
import random
import os
import time
from typing import cast

from autonity import networks
from web3 import Web3
from web3.exceptions import ContractLogicError
from web3.middleware import Middleware, SignAndSendRawMiddlewareBuilder

from .tasks import tasks

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("starter_kit")

w3 = Web3(networks.piccadilly.http_provider)

sender_account = w3.eth.account.from_key(os.environ["SENDER_PRIVATE_KEY"])
w3.eth.default_account = sender_account.address
signer_middleware = cast(
    Middleware, SignAndSendRawMiddlewareBuilder.build(sender_account)
)
w3.middleware_onion.add(signer_middleware)

while True:
    task = random.choice(tasks)
    logger.info(task.__name__)
    try:
        task(w3)
    except ContractLogicError as e:
        # Contract execution reverted
        logger.warning(e)
    time.sleep(1)
