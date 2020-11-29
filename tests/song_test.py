import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Senorita", "Cabello_and_Mendes")
    
    def test_song_has_title(self):
        self.assertEqual("Senorita", self.song.title)