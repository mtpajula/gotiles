
'''
Holds core

'''
from core.tile_coordinates import TileCoordinates


class Controller:

    def __init__(self):

        self.tilecoord = TileCoordinates()

    def start(self):

        zoom = 10
        (x, y) = self.tilecoord.deg2num(66.49, 25.72, zoom)

        print('tileAddress: ' + str(zoom) + '/' + str(x) + '/' + str(y) + '.png')


