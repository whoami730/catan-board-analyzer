class Location:
    # initialize with list of locations
    def __init__(self, *args):
        self.locations = []
        for arg in args:
            self.locations.append(arg)

    def __repr__(self):
        return str(self.locations)