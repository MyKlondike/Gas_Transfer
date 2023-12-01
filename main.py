import time
import random
from web3 import Web3
from loguru import logger
from config import *

with open("pk_recept.txt", "r") as file:
    lst = file.readlines()


class Wallet:
    def __init__(self, key, recipient):
        self.key = key
        self.recipient = recipient
        self.w3 = Web3(Web3.HTTPProvider(rpc))
        self.gasPrice = self.w3.eth.gas_price
        key_with_prefix = key if key.startswith('0x') else f'0x{key}'
        recipient_with_prefix = recipient if recipient.startswith('0x') else f'0x{recipient}'
        self.account = self.w3.to_checksum_address(self.w3.eth.account.from_key(key_with_prefix).address)
        self.recipient = self.w3.to_checksum_address(recipient_with_prefix)
        self.balance = self.w3.eth.get_balance(self.account)
        self.nonce = self.w3.eth.get_transaction_count(self.account)

    def send_gas(self):
        recipient_with_prefix = self.recipient if self.recipient.startswith('0x') else f'0x{self.recipient}'
        to = recipient_with_prefix
        module = f'Transfer:'
        logger.info(module)
        try:
            gas = self.w3.eth.estimate_gas({'from': self.account, 'to': self.recipient, 'value': self.balance})
            amount = int(self.balance - gas * self.gasPrice * (random.uniform(1.01, 1.02)))

            tx = {
                'from': self.account,
                'to': to,
                'value': amount,
                'chainId': id,
                'gasPrice': self.gasPrice,
                'nonce': self.nonce,
                'gas': gas,
            }

            logger.info(f"From {self.account} to {self.recipient}")
            signed_txn = self.w3.eth.account.sign_transaction(tx, private_key = self.key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            tx_status = Txn(tx_hash)
            if tx_status.check_status() == True:
                logger.info(f"Transaction : {scan}{self.w3.to_hex(tx_hash)}")

            return tx_hash
        except Exception as error:
            logger.error(f'{module} | {error}')


class Txn:
    def __init__(self, tx_hash):
        self.tx_hash = tx_hash
        self.w3 = Web3(Web3.HTTPProvider(rpc))

    def check_status(self):
        start_time_stamp = int(time.time())
        while True:
            try:
                stat = self.w3.eth.get_transaction_receipt(self.tx_hash)
                status = stat["status"]

                if status in [0, 1]:
                    return status

            except Exception as error:
                time_stamp = int(time.time())
                if time_stamp - start_time_stamp > 100:
                    logger.info(f'{error} не получили tx_status за {100} sec, вероятно tx is success')
                    return 1
                time.sleep(1)


def main():
    lines = [line.strip() for line in lst]
    total_wallets = len(lines)
    random.shuffle(lines)

    for number, line in enumerate(lines, start = 1):
        key, recipient = line.strip().split(":")
        print(f"\nОбработка кошелька {number} из {total_wallets}")
        transfer = Wallet(key, recipient)
        transfer.send_gas()

        t = random.randint(delay_from, delay_to)
        if number != total_wallets:
            print(f"\nСледующий кошелек будет обработан через {t} сек.")
            time.sleep(t)
        else:
            print(f"\nВсе кошельки успешно обработаны!")


if __name__ == "__main__":
    main()
