# Joseph Wang
# 6/18/2021
# Tile class for OOP Catan board analyzer

from typing import Self, override


class Tile:
    dice_number: int
    resource_type: str

    # initialize with instance variables dice number and resource type
    def __init__(self, dice_number: int, resource_type: str):
        self.dice_number = dice_number
        self.resource_type = resource_type

    def is_desert(self):
        return self.resource_type == "desert"

    @override
    def __repr__(self):
        return f"({self.dice_number}, {self.resource_type})"

    def __lt__(self, other: Self) -> bool:
        return self.dice_number < other.dice_number

    def __gt__(self, other: Self) -> bool:
        return self.dice_number > other.dice_number
