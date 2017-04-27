from Musikstueck import Musikstueck
from pygame import mixer



class Mock_Song(Musikstueck):

    def meta(self):
        self.title="Mock"
        self.intepret="Mock"
        self.album="Mock"
        self.slength=3

    def abspielen(self):
        print("Titel: {} \nAlbum: {} \nIntepret: {}".format (self.title, self.album, self.intepret))
        song=open(self.path)
        print(song.read())
        song.close()
        print("---")