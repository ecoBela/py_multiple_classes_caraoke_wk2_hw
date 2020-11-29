import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Mr Bond", 2000)

    def test_guest_has_name(self):
        self.assertEqual("Mr Bond", self.guest.name)

    def test_guest_has_cash_amount(self):
        self.assertEqual(2000, self.guest.cash_amount)