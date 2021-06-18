from Tile import Tile
from Location import Location
from Board import Board

def main():
    """
    tile1 = Tile(3, 'brick')
    tile2 = Tile(3, 'brick')
    location1 = Location(tile1, tile2)

    print(tile1.dice_number)
    print(tile2)
    print(location1)
    """

    board1 = Board('board.csv')
    board1.analyze_tiles()
    board1.analyze_locations()
    board1.display_GUI()


if __name__ == '__main__':
    main()