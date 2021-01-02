import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Pink_room", 30, 400.00)
        self.room_2 = Room("Blue_room", 15, 200.00)
        self.song_1 = Song("Halo", "Beyonce")
        self.song_2 = Song("Living la vida loca", "Ricky Martin")
        self.guest = Guest("Superman", 600, "Bootilicious")
        self.guest2 = Guest("Mariah", 750, "All I want for Christmas")

    def test_room_has_name(self):
        self.assertEqual("Pink_room", self.room_1.room_name)

    def test_check_room_capacity(self):
        self.assertEqual(30, self.room_1.capacity)

    def test_set_room_rate(self):
        self.assertEqual(400, self.room_1.rate["large"])
        self.assertEqual(200, self.room_2.rate["small"])

    def test_room_has_a_till(self):
        self.assertEqual(150, self.room_1.till)

    def test_room_has_song_list(self):
        self.assertEqual([], self.room_1.song_list)

    def test_room_has_guest_list(self):
        self.assertEqual([], self.room_1.guest_list)

    def test_room_can_add_to_song_list(self):
        self.room_1.add_song_to_list(self.song_1)
        self.assertEqual(1, len(self.room_1.song_list))

    def test_room_can_add_to_guestlist(self):
        self.room_1.add_to_guestlist(self.guest)
        self.assertEqual(1, len(self.room_1.guest_list))

    def test_room_can_add_to_guestlist_if_capacity(self):
        self.room_1.add_to_guestlist_if_capacity(self.guest)
        self.room_1.add_to_guestlist_if_capacity(self.guest2)
        self.assertEqual(2, len(self.room_1.guest_list))

    def test_room_can_remove_from_guestlist(self):
        self.room_1.add_to_guestlist(self.guest)
        self.room_1.remove_from_guestlist(self.guest)
        self.assertEqual(0, len(self.room_1.guest_list))