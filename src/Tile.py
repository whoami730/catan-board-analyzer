# Joseph Wang
# 6/18/2021
# Tile class for OOP Catan board analyzer

class Tile:
    # initialize with instance variables dice number and resource type
    def __init__(self, dice_number, resource_type):
        self.dice_number = dice_number
        self.resource_type = resource_type

    def __repr__(self):
        return f"({self.dice_number}, {self.resource_type})"

    def __lt__(self, other):
        return self.dice_number < other.dice_number

    def __gt__(self, other):
        return self.dice_number > other.dice_number