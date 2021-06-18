class Constants:
    # dictionary of roll number to dice chance (out of 36), so for 5 the chance is 4/36
    dice_chance = {
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

    tile_types = {
        "b": "brick",
        "g": "grain",
        "l": "lumber",
        "o": "ore",
        "w": "wool",
        "d": "desert"
    }

    # number of each resource tile on map
    resource_amounts = {
        "brick": 3,
        "grain": 4,
        "lumber": 4,
        "ore": 3,
        "wool": 4,
        "desert": 1,
    }

    # average chance for each tile
    average_tile_chance = (2 * 1 + 4 * 2 + 4 * 3 + 4 * 4 + 4 * 5) / 18