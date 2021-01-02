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

    def add_to_guestlist_if_capacity(self, guest):
        if len(self.guest_list) <= self.capacity:
            self.guest_list.append(guest)

    def remove_from_guestlist(self, guest):
        self.guest_list.remove(guest)

    def add_to_till(self, guest):
        guest.cash_amount -= self.rate["large"]
        self.till += self.rate["large"]


    

    

    


        



    


        
