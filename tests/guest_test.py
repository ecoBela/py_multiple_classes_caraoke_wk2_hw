import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Mr Bond", 2000, "Tomorrow Never Dies")
        self.room_1 = Room("Yellow", 15, 200.00)


    def test_guest_has_name(self):
        self.assertEqual("Mr Bond", self.guest_1.name)

    def test_guest_has_cash_amount(self):
        self.assertEqual(2000, self.guest_1.cash_amount)

    def test_guest_has_fav_song(self):
        self.assertEqual("Tomorrow Never Dies", self.guest_1.fav_song)

    # def test_guest_pays_for_room(self):
    #     self.assertEqual(1800, self.guest_1.pay_for_room(room_1))