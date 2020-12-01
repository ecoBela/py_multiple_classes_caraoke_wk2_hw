from src.guest import Guest
from src.song import Song

class Room():
    def __init__(self, room_name, capacity, rate):
        self.room_name = room_name
        self.capacity = capacity
        self.rate = {
            "large": 400,
            "small": 200
        }
        self.till = 150
        self.guest_list = []
        self.song_list = []
        
    def add_song_to_list(self, song):
        self.song_list.append(song)

    def add_to_guestlist(self, guest):
        self.guest_list.append(guest)


    


        



    


        
