class Location:
    # initialize with list of locations
    def __init__(self, *args):
        self.location_tiles = []
        for arg in args:
            self.location_tiles.append(arg)

    def __repr__(self):
        return str(self.location_tiles)