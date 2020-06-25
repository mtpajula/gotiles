
'''
Holds core

'''
from core.elements.point import Point
from core.tile_coordinates import TileCoordinates
from core.tile_download import TileDownload


class Controller:

    def __init__(self):
        self.tilecoord = TileCoordinates()
        self.download = TileDownload('https://tiles.kartat.kapsi.fi/peruskartta/', '.jpg')

    def test(self):
        p1 = Point()
        p1.add_coordinates(25.7455, 66.511686)
        p2 = Point()
        p2.add_coordinates(25.8015, 66.48094)

        zoom_from = 1
        zoom_to = 16

        tile_points = self.tilecoord.get_tiles(p1, p2, zoom_from, zoom_to)

        if self.download.download_tiles(tile_points):
            print('\nTiles downloaded ok!\n')
        else:
            print('\nTiles download failed!\n')
