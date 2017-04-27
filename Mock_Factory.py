from MusikdatenbankFabrik import MusikdatenbankFabrik
import glob
from Mock_Song import Mock_Song

class Mock_Factory(MusikdatenbankFabrik):

    def lade_musik(self):
        playlistprep=glob.glob("F:/Schule/JG4/SEW/Python/A09/music/mock/*.txt")
        for paths in playlistprep:
            self.playlist.append(Mock_Song(paths))
        self.geladen=True
