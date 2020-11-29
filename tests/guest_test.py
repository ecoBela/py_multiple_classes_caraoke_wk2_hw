import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Mr Bond", 2000, "Tomorrow Never Dies")

    def test_guest_has_name(self):
        self.assertEqual("Mr Bond", self.guest_1.name)

    def test_guest_has_cash_amount(self):
        self.assertEqual(2000, self.guest_1.cash_amount)

    def test_guest_has_fav_song(self):
        self.assertEqual("Tomorrow Never Dies", self.guest_1.fav_song)