import unittest
from transfer import Transfer

class TestTransfer(unittest.TestCase):
    
    def test_successful_transfer(self):
        # Arrange
        sender = 'Alice'
        receiver = 'Bob'
        amount = 100
        
        # Act
        transfer = Transfer(sender, receiver, amount)
        success = transfer.execute()
        
        # Assert
        self.assertTrue(success)
        self.assertEqual(sender.balance, 100) 
        self.assertEqual(receiver.balance, 100)

    def test_failed_transfer_invalid_amount(self):
        # Arrange
        sender = 'Alice'
        receiver = 'Bob'
        amount = -100
        
        # Act
        transfer = Transfer(sender, receiver, amount)
        success = transfer.execute()
        
        # Assert
        self.assertFalse(success)
        self.assertEqual(sender.balance, 0)
        self.assertEqual(receiver.balance, 0)
        
    def test_failed_transfer_insufficient_funds(self):
        # Arrange
        sender = 'Alice'
        sender.balance = 50
        receiver = 'Bob'
        amount = 100
        
        # Act
        transfer = Transfer(sender, receiver, amount)
        success = transfer.execute()
        
        # Assert
        self.assertFalse(success)
        self.assertEqual(sender.balance, 50)
        self.assertEqual(receiver.balance, 0)
        
if __name__ == '__main__':
    unittest.main()