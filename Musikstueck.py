from abc import ABCMeta, abstractmethod
__author__ = 'DD'

class Musikstueck(metaclass=ABCMeta):
    """ Die basisklasse fuer alle Musikstuecke
    """

    def __init__(self, path):
        self.path=path
        self.meta()

    @abstractmethod
    def meta(self):
        pass

    @abstractmethod
    def abspielen(self):
        pass