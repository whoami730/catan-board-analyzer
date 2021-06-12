from Tile import Tile
from Location import Location


class Board:
    def __init__(self):
        pass

    def main():
        tile1 = Tile(3, 'brick')
        tile2 = Tile(3, 'brick')
        location1 = Location(tile1, tile2)

        print(tile1.dice_number)
        print(tile2)
        print(location1)
    
    if __name__ == '__main__':
        main()