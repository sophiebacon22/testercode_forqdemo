import logging

logger = logging.getLogger(__name__)

class Wallet:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        logger.info("Deposited %d, balance is now %d", amount, self.balance)

    def withdraw(self, amount):
        if self.balance < amount:
            logger.warning("Insufficient funds, balance is %d but tried to withdraw %d", self.balance, amount)
            return 
        self.balance -= amount
        logger.info("Withdrew %d, balance is now %d", amount, self.balance)

    def transfer(self, recipient, amount):
        if self.balance < amount:
            logger.warning("Insufficient funds, balance is %d but tried to transfer %d", self.balance, amount)
            return
        self.balance -= amount
        recipient.deposit(amount)
        logger.info("Transferred %d to %s, balance is now %d", amount, recipient, self.balance)