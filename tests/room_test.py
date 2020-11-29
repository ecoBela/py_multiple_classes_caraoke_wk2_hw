import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Pink_room", [])
        self.song_1 = Song("Halo", "Beyonce")

    def test_room_has_name(self):
        self.assertEqual("Pink_room", self.room.name)

    def test_room_has_song_list(self):
        self.assertEqual([], self.room.song_list)

    def test_room_has_guest_list(self):
        self.assertEqual([], self.room.guest_list)

    def test_set_room_capacity(self):
        self.assertEqual(20, self.room.capacity)

    def test_set_room_fee(self):
        self.assertEqual(500, self.room.fee)

    def test_room_has_a_till(self):
        self.assertEqual(150, self.room.till)

    # def test_play_song_if_on_playlist(self):
    #     self.assertEqual("Halo", self.room.play_song(self.song_1))

    