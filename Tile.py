class Tile:
    # initialize with instance variables dice number and resource type
    def __init__(self, dice_number, resource_type):
        self.dice_number = dice_number
        self.resource_type = resource_type

    def __repr__(self):
        return f"({self.dice_number}, {self.resource_type})"