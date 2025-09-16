# Joseph Wang
# 6/18/2021
# Location class for OOP Catan board analyzer

from typing import override

from Tile import Tile


class Location:
    location_tiles: list[Tile]

    # initialize with list of locations
    def __init__(self, *args: Tile):
        self.location_tiles = []
        for arg in args:
            self.location_tiles.append(arg)

    @override
    def __repr__(self):
        return str(self.location_tiles)
