from Musikstueck import Musikstueck
from pygame import mixer
from eyed3 import id3
from mutagen.mp3 import MP3


class MP3_Song(Musikstueck):

    def meta(self):
        tag = id3.Tag()
        tag.parse(self.path)
        audio = MP3(self.path)

        self.title=tag.title
        self.intepret=tag.artist
        self.album=tag.album
        self.slength=audio.info.length

    def abspielen(self):
        print("Titel: {} \nAlbum: {} \nIntepret: {}".format (self.title, self.album, self.intepret))
        mixer.init()
        mixer.music.load(self.path)
        mixer.music.play()
        print("---")