# Joseph Wang
# 6/18/2021
# Location class for OOP Catan board analyzer

class Location:
    # initialize with list of locations
    def __init__(self, *args):
        self.location_tiles = []
        for arg in args:
            self.location_tiles.append(arg)

    def __repr__(self):
        return str(self.location_tiles)