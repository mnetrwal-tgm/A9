from abc import ABCMeta, abstractmethod
import time
__author__ = 'DD'

class MusikdatenbankFabrik(metaclass=ABCMeta):
    """ Die Basisklasse fuer Fabriken
    """

    def __init__(self):
        self.geladen = False
        self.playlist=[]

    @abstractmethod
    def lade_musik(self):
        pass

    def abspielen(self):
        if not self.geladen:
            self.lade_musik()
        for song in self.playlist:
            song.abspielen()
            time.sleep(song.slength)
            #time.sleep(10)
        print('Wir sind am Ende der Playliste angelangt. Auf Wiedersehen!')
