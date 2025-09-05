import logging
import os
import random
from typing import cast

from dotenv import load_dotenv
load_dotenv()

import requests
from web3 import Web3, HTTPProvider
from web3.exceptions import ContractLogicError
from web3.middleware import Middleware, SignAndSendRawMiddlewareBuilder

from tasks import tasks

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("starter_kit")

def create_web3_provider(rpc_url: str) -> Web3:
    try:
        w3 = Web3(HTTPProvider(rpc_url))
        if not w3.is_connected():
            raise ConnectionError(f"Web3 failed to connect to {rpc_url}")
        return w3
    except Exception as e:
        raise RuntimeError(f"Could not connect to RPC URL {rpc_url}. Reason: {e}")

primary_rpc = os.getenv("RPC_URL")
fallback_rpc = os.getenv("FALLBACK_RPC_URL")

if not primary_rpc:
    logger.critical("RPC_URL not found in environment (.env file).")
    exit(1)

try:
    w3 = create_web3_provider(primary_rpc)
except Exception as e:
    logger.error(e)
    if fallback_rpc:
        logger.warning("Trying fallback RPC...")
        try:
            w3 = create_web3_provider(fallback_rpc)
        except Exception as e2:
            logger.critical(f"Fallback RPC failed too. {e2}")
            exit(1)
    else:
        exit(1)

private_key = os.getenv("SENDER_PRIVATE_KEY")
if not private_key:
    logger.critical("SENDER_PRIVATE_KEY not found in environment (.env file).")
    exit(1)

sender_account = w3.eth.account.from_key(private_key)
w3.eth.default_account = sender_account.address

signer_middleware = cast(
    Middleware, SignAndSendRawMiddlewareBuilder.build(sender_account)
)
w3.middleware_onion.add(signer_middleware)

logger.info("== Running Tasks ==")

for _ in range(10_000):
    task = random.choice(tasks)
    logger.info(f"Running task: {task.__name__}")
    try:
        task(w3)
    except ContractLogicError as e:
        logger.warning(f"Contract logic error: {e}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error: {e}")
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
