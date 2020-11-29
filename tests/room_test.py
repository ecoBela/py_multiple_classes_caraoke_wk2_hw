import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("Pink_room")

    def test_room_has_name(self):
        self.assertEqual("Pink_room", self.room.name)

    def test_room_has_song_list(self):
        self.assertEqual([], self.room.song_list)