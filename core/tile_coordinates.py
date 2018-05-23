
import math
'''
Calculates TMS-koordinates
https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames

'''


class TileCoordinates:

    def __init__(self):
        pass

    def deg2num(self, lat_deg, lon_deg, zoom):
        lat_rad = math.radians(lat_deg)
        n = 2.0 ** zoom
        xtile = int((lon_deg + 180.0) / 360.0 * n)
        ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
        return (xtile, ytile)