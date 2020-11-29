class Room():
    def __init__(self, name, guest_list):
        self.name = name
        self.guest_list = []
        self.song_list = []
        self.capacity = 20
        self.fee = 500
        self.till = 150

    def play_song(self, song):
        if song.title == self.song_list:
            return "Song is ready to play"
        else:
            return "Sorry, song not available"

        
