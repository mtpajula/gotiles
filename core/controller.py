
'''
Holds core

'''
from core.elements.point import Point
from core.tile_coordinates import TileCoordinates
from core.tools import *


class Controller:

    def __init__(self):
        self.tilecoord = TileCoordinates()

    def start(self):
        zoom = 10
        p = Point()
        p.add_coordinates(25.72, 66.49)

        tp1 = self.tilecoord.deg2num(p, zoom)

        print('tileAddress: ' + str(zoom) + '/' + str(tp1.e) + '/' + str(tp1.n) + '.png')
        #print('tileAddress: ' + add_leading_zeros(zoom, 4) + '/' + add_leading_zeros(tp.e, 4) + '/' + add_leading_zeros(tp.n, 4) + '.png')

        p.add_coordinates(24.72, 65.49)

        tp2 = self.tilecoord.deg2num(p, zoom)

        print('tileAddress: ' + str(zoom) + '/' + str(tp2.e) + '/' + str(tp2.n) + '.png')
        #print('tileAddress: ' + add_leading_zeros(zoom, 4) + '/' + add_leading_zeros(tp.e, 4) + '/' + add_leading_zeros(
        #    tp.n, 4) + '.png')

        self.tilecoord.get_tiles_between(tp1, tp2)
