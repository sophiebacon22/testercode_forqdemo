import logging

class Transaction:
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def deposit(self, amount):
        self.logger.info("Depositing %s", amount)
        # existing deposit logic
        
    def withdraw(self, amount):
        self.logger.info("Withdrawing %s", amount) 
        # existing withdraw logic
        
    def transfer(self, amount, account):
        self.logger.info("Transferring %s to account %s", amount, account)
        # existing transfer logic