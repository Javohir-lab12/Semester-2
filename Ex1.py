class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def display_info(self):
        print(f"Title: {self.title}, Artist: {self.artist}, Duration: {self.duration} min")

    def get_duration_seconds(self):
        duration_in_seconds = self.duration * 60
        return duration_in_seconds

first_song = Song("Yesterday", "The Beatles", 2.5)
second_song = Song("Bohemian Rhapsody", "Queen", 6.0)
first_song.display_info()
print(first_song.get_duration_seconds())
second_song.display_info()
print(second_song.get_duration_seconds())