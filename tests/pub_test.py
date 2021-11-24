import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    
    @unittest.skip("delete...")
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00,)

    @unittest.skip("delete...")
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    @unittest.skip("delete...")
    def test_pub_has_till(self):
        self.assertEqual(0.00, self.pub.till)