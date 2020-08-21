
'''
Holds core

'''
from core.elements.point import Point
from core.tile_coordinates import TileCoordinates
from core.tile_download import TileDownload


class Controller:

    def __init__(self):
        self.tilecoord = TileCoordinates()
        self.downloader = TileDownload('https://tiles.kartat.kapsi.fi/peruskartta/', '.jpg')
        self.corners = []
        self.zoom_from = 1
        self.zoom_to = 16

    def set_corner(self, lat, lon):
        p = Point()
        p.add_coordinates(lon, lat)
        self.corners.append(p)

    def set_zoom(self, zoom_from, zoom_to):
        self.zoom_from = zoom_from
        self.zoom_to = zoom_to

    def download_tiles(self):
        if len(self.corners) == 2:
            tile_points = self.tilecoord.get_tiles(self.corners[0], self.corners[1], self.zoom_from, self.zoom_to)
            if self.downloader.download_tiles(tile_points):
                print('\nTiles downloaded ok!\n')
            else:
                print('\nTiles download failed!\n')
        else:
            print('\nExactly two corner points needed!\n')
