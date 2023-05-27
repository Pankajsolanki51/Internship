#q1
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Song 1: Imagine by John Lennon
imagine = Song(["Imagine there's no heaven",
                "It's easy if you try",
                "No hell below us",
                "Above us only sky"])

# Song 2: Bohemian Rhapsody by Queen
bohemian_rhapsody = Song(["Is this the real life?",
                          "Is this just fantasy?",
                          "Caught in a landslide",
                          "No escape from reality"])

# Sing the songs
imagine.sing_me_a_song()
print("-" * 20)
bohemian_rhapsody.sing_me_a_song()


#q2
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Lyrics for the song "Imagine" by John Lennon
imagine_lyrics = ["Imagine there's no heaven",
                  "It's easy if you try",
                  "No hell below us",
                  "Above us only sky"]

# Lyrics for the song "Bohemian Rhapsody" by Queen
bohemian_rhapsody_lyrics = ["Is this the real life?",
                            "Is this just fantasy?",
                            "Caught in a landslide",
                            "No escape from reality"]

# Create song objects using the lyrics variables
imagine = Song(imagine_lyrics)
bohemian_rhapsody = Song(bohemian_rhapsody_lyrics)

# Sing the songs
imagine.sing_me_a_song()
print("-" * 20)
bohemian_rhapsody.sing_me_a_song()
