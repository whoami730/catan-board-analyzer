# Joseph Wang
# 6/18/2021
# Driver program for OOP Catan board analyzer

from Board import Board

from typed_argparse import TypedArgs, Parser, arg

# 1. Argument definition
class Args(TypedArgs):
    board: str = arg("-b", "--board", default='./src/board.csv')
    use_resource_importance: bool = arg("-r", "--use_resource_importance", type=bool)

def analyze(args: Args):
    """
    tile1 = Tile(3, 'brick')
    tile2 = Tile(3, 'brick')
    location1 = Location(tile1, tile2)

    print(tile1.dice_number)
    print(tile2)
    print(location1)
    """
    board1 = Board(args.board)
    board1.analyze_tiles()
    board1.analyze_locations(args.use_resource_importance)
    board1.display_GUI()


if __name__ == '__main__':
    Parser(Args).bind(analyze).run()

