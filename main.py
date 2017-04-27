from MP3_Factory import *
from Mock_Factory import *

__author__ = 'DD'

if __name__ == '__main__':
    fabrik = MP3_Factory()
    fabrik2 = Mock_Factory()
    fabrik.abspielen()
    fabrik2.abspielen()