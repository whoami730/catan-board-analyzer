# Joseph Wang
# 6/18/2021
# Constants class for OOP Catan board analyzer

class Constants:
    # dictionary of roll number to dice chance (out of 36), so for 5 the chance is 4/36
    dice_chance: dict[int, int] = {
        0: 0,
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        8: 5,
        9: 4,
        10: 3,
        11: 2,
        12: 1
    }

    # types of tiles
    tile_types: dict[str, str] = {
        "b": "brick",
        "g": "grain",
        "l": "lumber",
        "o": "ore",
        "w": "wool",
        "d": "desert"
    }

    # number of each resource tile on map
    resource_amounts: dict[str, int] = {
        "brick": 3,
        "grain": 4,
        "lumber": 4,
        "ore": 3,
        "wool": 4,
        "desert": 1,
    }

    # average chance for each tile
    average_tile_chance: float = (2 * 1 + 4 * 2 + 4 * 3 + 4 * 4 + 4 * 5) / 18

    # borrowed from https://www.boardgameanalysis.com/what-is-the-strategic-value-of-each-catan-resources/
    resource_importance: dict[str, float] = {
        "brick": 0.781,
        "grain": 1.350,
        "lumber": 0.781,
        "ore": 1.329,
        "wool": 0.760,
        "desert": 0,
    }
