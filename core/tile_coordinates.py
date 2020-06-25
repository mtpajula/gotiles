
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

    def get_tiles(self, point1, point2, zoom_from, zoom_to):
        (z1, z2) = self.fix_order(zoom_from, zoom_to)
        tile_points = []
        for z in range(z1, z2+1):
            tp1 = self.deg2num(point1, z)
            tp2 = self.deg2num(point2, z)
            tile_points.extend(self.get_tiles_between(tp1, tp2))
        return tile_points

    def get_tiles_between(self, tp1, tp2):
        (n1, n2) = self.fix_order(tp1.n, tp2.n)
        (e1, e2) = self.fix_order(tp1.e, tp2.e)

        tile_points = []

        for n in range(n1, n2+1):
            # print("range: " + str(n))
            for e in range(e1, e2+1):
                tp = TilePoint()
                tp.add_coordinates(e, n, tp1.z)
                tile_points.append(tp)
                # print("    " + str(e) + "/" + str(n))

        return tile_points

    def fix_order(self, numa, numb):
        if numa < numb:
            return (numa, numb)
        else:
            return (numb, numa)



