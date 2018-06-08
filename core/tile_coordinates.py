
import math

from core.elements.point import Point
from core.elements.tilepoint import TilePoint

'''
Calculates TMS-koordinates
https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames

'''


class TileCoordinates:

    def __init__(self):
        pass

    def deg2num(self, point, zoom):
        tp = TilePoint()

        lat_rad = math.radians(point.n)
        n = 2.0 ** zoom
        xtile = int((point.e + 180.0) / 360.0 * n)
        ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)

        tp.add_coordinates(xtile, ytile, zoom)

        return tp

    def get_tiles_between(self, tp1, tp2):
        (n1, n2) = self.fix_order(tp1.n, tp2.n)
        (e1, e2) = self.fix_order(tp1.e, tp2.e)

        for n in range(n1, n2+1):
            print("range: " + str(n))
            for e in range(e1, e2+1):
                print("    " + str(e) + "/" + str(n))

    def fix_order(self, numa, numb):
        if numa < numb:
            return (numa, numb)
        else:
            return (numb, numa)



