import tkinter as tk
import csv

# define tiles and initialize locations

tiles = []

"""
# old tiles, before I got tiles
tiles = [
    [ (6, "lumber"), (2, "wool"), (5, "brick") ],
    [ (3, "lumber"), (9, "grain"), (10, "wool"), (8, "grain") ],
    [ (8, "ore"), (4, "grain"), (11, "brick"), (3, "grain"), (4, "lumber") ],
    [ (0, "desert"), (5, "wool"), (6, "wool"), (11, "ore") ],
    [ (10, "ore"), (9, "lumber"), (12, "brick") ]
]
"""

locations = [
    [],
    [],
    [],
    [],
    [],
    []
]

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

# number of each resource tile on map
resource_amounts = {
    "brick": 3,
    "grain": 4,
    "lumber": 4,
    "ore": 3,
    "wool": 4,
    "desert": 1,
}

# relative chance for each resource to their baseline
resource_rarity_percent = {
    "brick": 0.0,
    "grain": 0.0,
    "lumber": 0.0,
    "ore": 0.0,
    "wool": 0.0,
    "desert": 0.0
}

def main():
    get_tiles('board.csv')

    generate_locations()

    print_locations()

    analyze_tiles()

    locations_by_resources = analyze_locations()

    display_GUI(locations_by_resources)

def get_tiles(board_location):
    with open(board_location) as board:

        # read from file
        reader = csv.reader(board)

        # skip header line
        next(reader)

        # initialize variables
        tiles_row = []
        tile_types = {
            "b": "brick",
            "g": "grain",
            "l": "lumber",
            "o": "ore",
            "w": "wool",
            "d": "desert"
        }

        for tile in reader:

            # for '0' character, start new tiles row
            if tile[1] == '0':
                tiles.append(tiles_row)
                tiles_row = []

            # otherwise add tile as tuple to tiles row
            else:
                tiles_row.append((int(tile[0]), tile_types[tile[1]]))
        
def generate_locations():
    # define the tiles rows to go through to create locations, 
    # always going from one row to the adjacent smaller one, 
    # including the nonexistent rows -1  and 5
    tiles_rows_for_locations = [(0, -1), (1, 0), (2, 1), (2, 3), (3, 4), (4, 5)]


    # initialize locations row
    locations_row = 0

    # go through two tiles rows at a time (in a tuple) to create locations
    for tiles_rows in tiles_rows_for_locations:

        # initalize starting location and tile
        location = 0
        tile = 0

        # save rows 1 and 2
        row1 = tiles_rows[0]
        row2 = tiles_rows[1]

        # while the current tile exists, keep adding locations from that row
        while tile < len(tiles[row1]):

            # for even numbered locations, use two tiles on bottom and one on top
            if location % 2 == 0:
                
                # if second row exists and there is a tile before the current one, create location like normal (3 tiles)
                if row2 in range(0, 5) and (tile - 1) in range(len(tiles[row1])):
                    locations[locations_row].append([tiles[row1][tile], tiles[row1][tile - 1], tiles[row2][tile - 1]])

                # if second row does not exist but there is a tile before the current one, add 2 tiles
                elif row2 not in range(0, 5) and (tile - 1) in range (len(tiles[row1])):
                    locations[locations_row].append([tiles[row1][tile], tiles[row1][tile - 1]]) 
                
                # if there is not a tile before the current one, add 1 tile
                else:
                    locations[locations_row].append([tiles[row1][tile]])

                # increment location
                location = location + 1

            # for odd numbered locations, use one tile on bottom and two on top
            else:

                # if second row exists, there is a tile before the current one, 
                # and there is a tile in row 2 in the upper right corner,
                # create location like normal (3 tiles)
                if row2 in range(0, 5) and (tile - 1) in range(len(tiles[row1])) and tile in range(len(tiles[row2])):
                    locations[locations_row].append([tiles[row1][tile], tiles[row2][tile], tiles[row2][tile - 1]])

                # if second row exists, there is a tile before the current one, 
                # and there is not a tile in row 2 in the upper right corner,
                # add 2 tiles like a backslash \
                elif row2 in range(0, 5) and (tile - 1) in range(len(tiles[row1])) and tile not in range(len(tiles[row2])):
                    locations[locations_row].append([tiles[row1][tile], tiles[row2][tile - 1]])
                
                # if second row exists but there is not a tile before the current one, add 2 tiles like a forward slash /
                elif row2 in range(0, 5) and (tile - 1) not in range(len(tiles[row1])):
                    locations[locations_row].append([tiles[row1][tile], tiles[row2][tile]])

                # if there is no second row, add 1 tile
                else:
                    locations[locations_row].append([tiles[row1][tile]])

                # increment location and tile (advance one tile every two locations)
                location = location + 1
                tile = tile + 1
        
        # add final edge location
        locations[locations_row].append([tiles[row1][tile - 1]])

        # increment locations row
        locations_row = locations_row + 1

def print_locations():
    # loop through each location row
    for i, locations_row in enumerate(locations):
        # print row number
        print("Row " + str(i))

        # loop through each location and output in a seperate line indented by a tab
        for location in locations_row:
            print("\t" + str(location))
        print()
    
    # print unformatted locations nested list
    print(locations)

def analyze_locations():

    # initialize variables
    locations_by_resources = []

    # loop through all locations
    for locations_row in locations:

        for location in locations_row:

            location_chance = 0

            # loop through each tile for each location, adding up the total location chance
            for number, resource in location:
                location_chance = location_chance + dice_chance[number]
            
            # add location with total location chance to new list in format [9, (3, 'grain'), (11, 'ore'), (6, 'wool')]
            locations_by_resources.append([location_chance] + location)
    
    # sort locations by chance in descending order
    locations_by_resources.sort(reverse=True)

    return locations_by_resources

def analyze_tiles():
    # initialize variables

    # average chance for each tile
    average_tile_chance = (2 * 1 + 4 * 2 + 4 * 3 + 4 * 4 + 4 * 5) / 18

    # total chance for each resource
    resource_rarity = {
        "brick": 0,
        "grain": 0,
        "lumber": 0,
        "ore": 0,
        "wool": 0,
        "desert": 0
    }

    # loop through tiles and add up resource chances
    for tiles_row in tiles:
        for number, resource in tiles_row:
            resource_rarity[resource] = resource_rarity[resource] + dice_chance[number]

    # loop through resources and calculate relative resource rarity to baseline
    for resource, chance in resource_rarity.items():
        resource_rarity_percent[resource] = round(chance / (resource_amounts[resource] * average_tile_chance) * 100, 1)

def display_GUI(locations_by_resources):
    # create windows
    window = tk.Tk()
    window.title("Catan Locations by Resource Count")
    
    # initialize card images
    card_images = {
        "brick": tk.PhotoImage(file = "../Icons/card_brick.png"),
        "grain": tk.PhotoImage(file = "../Icons/card_grain.png"),
        "lumber": tk.PhotoImage(file = "../Icons/card_lumber.png"),
        "ore": tk.PhotoImage(file = "../Icons/card_ore.png"),
        "wool": tk.PhotoImage(file = "../Icons/card_wool.png")
    }

    # display each resource and its relative rarity to baseline
    i = 0
    for resource, percent in resource_rarity_percent.items():
        if resource != "desert":
            tk.Label(window, image = card_images[resource]).grid(row=i, column=0)
            tk.Label(window, text = str(percent) + '%', font = "18").grid(row=i, column=1)
            i = i + 1

    # output locations
    print()

    # output top locations by resources
    for i, location in enumerate(locations_by_resources):
        if location[0] >= 10:
            print(location)

            # print resource count
            tk.Label(window, text = location[0], font = "18").grid(row=i, column=3)

            # print relevant tiles for location
            for j, tile in enumerate(location[1:]):
                tk.Label(window, text = tile[0], image = card_images[tile[1]], compound = 'center', font = "18").grid(row=i, column=j+4)
    
    window.mainloop()

if __name__ == '__main__':
    main()