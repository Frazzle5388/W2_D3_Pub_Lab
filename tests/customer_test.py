import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Mr Smith", [], 10.00)

    #@unittest.skip("delete...")
    def test_customer_has_name(self):
        result = self.customer.name
        expected = "Mr Smith"
        self.assertEqual(expected, result)

    #@unittest.skip("delete...")
    def test_customer_has_stomach(self):
        result = self.customer.stomach
        expected = []
        self.assertEqual(expected, result)

    #@unittest.skip("delete...")
    def test_customer_has_wallet(self):
        result = self.customer.wallet
        expected = 10.00
        self.assertEqual(expected, result)

    #@unittest.skip("delete...")
    def test_reduce_wallet(self):
        self.customer.reduce_wallet(3.50)
        result = self.customer.wallet
        expected = 6.50
        self.assertEqual(expected, result)

    
