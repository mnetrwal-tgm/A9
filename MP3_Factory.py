from MusikdatenbankFabrik import MusikdatenbankFabrik
import glob
from MP3_Song import MP3_Song

class MP3_Factory(MusikdatenbankFabrik):

    def lade_musik(self):
        playlistprep=glob.glob("F:/Schule/JG4/SEW/Python/A09/music/real/*.mp3")
        for paths in playlistprep:
            self.playlist.append(MP3_Song(paths))
        self.geladen=True