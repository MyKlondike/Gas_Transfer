from time import sleep
from web3 import Web3

from config import CHECK_GWEI, CHAIN_GAS, MAX_GWEI, RETRY_COUNT, rpc
from loguru import logger


def get_gas():
    try:
        w3 =Web3(Web3.HTTPProvider("https://rpc.ankr.com/eth"))

        gas_price = w3.eth.gas_price
        gwei = w3.from_wei(gas_price, 'gwei')

        return gwei
    except Exception as error:
        logger.error(error)


def get_base_gas():
    try:
        w3 =Web3(Web3.HTTPProvider(rpc))
        gas_price = w3.eth.gas_price
        gwei = w3.from_wei(gas_price, 'gwei')

        return gwei
    except Exception as error:
        logger.error(error)


def wait_gas():
    logger.info("Get GWEI")
    while True:
        gas = get_gas()
        base_gas = get_base_gas()

        if gas > MAX_GWEI or base_gas > CHAIN_GAS:
            logger.info(f'Current ETH GWEI: {gas} > {MAX_GWEI} | CHAIN GWEI: {base_gas} > {CHAIN_GAS}')
            sleep(60)
        else:
            logger.success(f"GWEI is normal | current ETH GWEI: {gas} < {MAX_GWEI} | CHAIN GWEI: {base_gas} < {CHAIN_GAS}")
            break


def retry(func):
    def wrapper(*args, **kwargs):
        retries = 0
        while retries <= RETRY_COUNT:
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logger.error(f"Error | {e}")
                sleep(10, 20)
                retries += 1

    return wrapper


def check_gas(func):
    def _wrapper(*args, **kwargs):
        if CHECK_GWEI:
            wait_gas()
            get_base_gas()
        return func(*args, **kwargs)

    return _wrapper
