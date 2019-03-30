class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        song = self
        songs_sofar = set() 
        
        while (song.next != None):
            if (song.name in songs_sofar): # found it, so it is repeating
                return True
            else:
                songs_sofar.add(song.name)  # add it to the set
                song = song.next
        
        return False

########### CODE ENDS HERE ########################

####### EXAMPLES ################

first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("Third Eye")

first.next_song(second)
second.next_song(third)
third.next_song(first)


print(first.is_repeating_playlist())
# This should return True
print(second.is_repeating_playlist())
# This should return True
print(third.is_repeating_playlist())
# This should return True

forth = Song("Hello2")
fifth = Song("Eye of the tiger2")
sixth = Song("Third Eye2")
seventh = Song("The last song")

forth.next_song(fifth)
fifth.next_song(sixth)
sixth.next_song(seventh)

# All these will return False
print(forth.is_repeating_playlist())
print(fifth.is_repeating_playlist())
print(sixth.is_repeating_playlist())
print(seventh.is_repeating_playlist())

eighth = Song("Take me to a repeating playlist")
eighth.next_song(third)

# Will also print True
print(eighth.is_repeating_playlist())
