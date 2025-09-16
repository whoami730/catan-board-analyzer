# Joseph Wang
# 6/18/2021
# Board class for OOP Catan board analyzer

import csv
import tkinter as tk
from typing import override

from Tile import Tile
from Location import Location
from Constants import Constants

class Board:
    tiles: list[list[Tile]]
    locations: list[list[Location]]
    locations_by_resources: list[tuple[int, list[Tile]]]
    resource_rarity_percent: dict[str, float]

    def __init__(self, board_location: str):
        # get tiles from csv file
        self.tiles = []

        with open(board_location) as board_file:

            # read from file
            reader = csv.reader(board_file)

            # skip header line
            _ = next(reader)

            # initialize variables
            tiles_row: list[Tile] = []

            for tile in reader:
                # for '0' character, start new tiles row
                if tile[1] == '0':
                    self.tiles.append(tiles_row)
                    tiles_row = []

                # otherwise add Tile to tiles row
                else:
                    tiles_row.append(Tile(int(tile[0]), Constants.tile_types[tile[1]]))
        

        # generate locations based on tiles
        self.locations = [
            [],
            [],
            [],
            [],
            [],
            []
        ]

        # define the tiles rows to go through to create locations, 
        # always going from one row to the adjacent smaller one, 
        # including nonexistent rows -1  and 5
        tiles_rows_for_locations = [(0, -1), (1, 0), (2, 1), (2, 3), (3, 4), (4, 5)]

        # go through two tiles rows at a time (in a tuple) to create locations
        for locations_row, tiles_rows in enumerate(tiles_rows_for_locations):

            # initalize starting location and tile
            location = 0
            tile = 0

            # save rows 1 and 2
            row1 = tiles_rows[0]
            row2 = tiles_rows[1]

            # while the current tile exists, keep adding locations from that row
            while tile < len(self.tiles[row1]):

                # for even numbered locations, use two tiles on bottom and one on top
                if location % 2 == 0:
                    
                    # if second row exists and there is a tile before the current one, create location like normal (3 tiles)
                    if row2 in range(0, 5) and (tile - 1) in range(len(self.tiles[row1])):
                        self.locations[locations_row].append(Location(self.tiles[row1][tile], self.tiles[row1][tile - 1], self.tiles[row2][tile - 1]))

                    # if second row does not exist but there is a tile before the current one, add 2 tiles
                    elif row2 not in range(0, 5) and (tile - 1) in range (len(self.tiles[row1])):
                        self.locations[locations_row].append(Location(self.tiles[row1][tile], self.tiles[row1][tile - 1])) 
                    
                    # if there is not a tile before the current one, add 1 tile
                    else:
                        self.locations[locations_row].append(Location(self.tiles[row1][tile]))

                    # increment location
                    location = location + 1

                # for odd numbered locations, use one tile on bottom and two on top
                else:

                    # if second row exists, there is a tile before the current one, 
                    # and there is a tile in row 2 in the upper right corner,
                    # create location like normal (3 tiles)
                    if row2 in range(0, 5) and (tile - 1) in range(len(self.tiles[row1])) and tile in range(len(self.tiles[row2])):
                        self.locations[locations_row].append(Location(self.tiles[row1][tile], self.tiles[row2][tile], self.tiles[row2][tile - 1]))

                    # if second row exists, there is a tile before the current one, 
                    # and there is not a tile in row 2 in the upper right corner,
                    # add 2 tiles like a backslash \
                    elif row2 in range(0, 5) and (tile - 1) in range(len(self.tiles[row1])) and tile not in range(len(self.tiles[row2])):
                        self.locations[locations_row].append(Location(self.tiles[row1][tile], self.tiles[row2][tile - 1]))
                    
                    # if second row exists but there is not a tile before the current one, add 2 tiles like a forward slash /
                    elif row2 in range(0, 5) and (tile - 1) not in range(len(self.tiles[row1])):
                        self.locations[locations_row].append(Location(self.tiles[row1][tile], self.tiles[row2][tile]))

                    # if there is no second row, add 1 tile
                    else:
                        self.locations[locations_row].append(Location(self.tiles[row1][tile]))

                    # increment location and tile (advance one tile every two locations)
                    location = location + 1
                    tile = tile + 1
            
            # add final edge location
            self.locations[locations_row].append(Location(self.tiles[row1][tile - 1]))

        self.locations_by_resources = []
        self.resource_rarity_percent = {}

    @override
    def __repr__(self):
        repr = ""
        # print tiles
        for row, tiles_row in enumerate(self.tiles):
            # print row number
            repr = repr + f"Row {row}"

            # print each row in a separate line indented by a tab
            repr = repr + f"\t{tiles_row}\n"

        # print locations
        # loop through each location row
        for row, locations_row in enumerate(self.locations):
            # print row number
            repr = repr + f"\nRow {row}"

            # loop through each location and output in a seperate line indented by a tab
            for location in locations_row:
                repr = repr + f"\n\t{location}"

        return repr

    def analyze_tiles(self):
        # total chance for each resource
        resource_rarity = {
            "brick": 0,
            "grain": 0,
            "lumber": 0,
            "ore": 0,
            "wool": 0,
            "desert": 0
        }

        # relative chance for each resource to their baseline
        self.resource_rarity_percent = {
            "brick": 0.0,
            "grain": 0.0,
            "lumber": 0.0,
            "ore": 0.0,
            "wool": 0.0,
            "desert": 0.0
        }

        # loop through tiles and add up resource chances
        for tiles_row in self.tiles:
            for tile in tiles_row:
                resource_rarity[tile.resource_type] = resource_rarity[tile.resource_type] + Constants.dice_chance[tile.dice_number]

        # loop through resources and calculate relative resource rarity to baseline
        for resource, chance in resource_rarity.items():
            self.resource_rarity_percent[resource] = round(chance / (Constants.resource_amounts[resource] * Constants.average_tile_chance), ndigits=2)

    def analyze_locations(self, use_resource_importance: bool = False):
        # initialize variables
        self.locations_by_resources = []

        # loop through all locations
        for locations_row in self.locations:

            for location in locations_row:

                location_value = 0

                # loop through each tile for each location, adding up the total location chance
                for tile in location.location_tiles:
                    location_value = location_value + Constants.dice_chance[tile.dice_number] * (Constants.resource_importance[tile.resource_type] if use_resource_importance else 1)
                
                # add location with total location chance to new list in format [9, (3, 'grain'), (11, 'ore'), (6, 'wool')]
                self.locations_by_resources.append((round(location_value),  location.location_tiles))
        
        # sort locations by chance in descending order
        self.locations_by_resources.sort(reverse=True)

    def display_GUI(self):
        # create windows
        window = tk.Tk()
        window.title("Catan Locations by Resource Count")
        
        # initialize card images
        card_images = {
            "brick": tk.PhotoImage(file = "./resources/card_brick.png"),
            "grain": tk.PhotoImage(file = "./resources/card_grain.png"),
            "lumber": tk.PhotoImage(file = "./resources/card_lumber.png"),
            "ore": tk.PhotoImage(file = "./resources/card_ore.png"),
            "wool": tk.PhotoImage(file = "./resources/card_wool.png")
        }

        # display each resource and its relative rarity to baseline
        i = 0
        for resource, percent in self.resource_rarity_percent.items():
            if resource != "desert":
                tk.Label(window, image = card_images[resource]).grid(row=i, column=0)
                tk.Label(window, text = str(percent), font = "18").grid(row=i, column=1)
                i = i + 1

        # output locations
        print()

        # output top locations by resources
        for i, (score, tiles) in enumerate(self.locations_by_resources):
            if score >= 10:
                # print resource count
                tk.Label(window, text = score, font = "18").grid(row=i, column=3)

                # print relevant tiles for location
                for j, tile in enumerate(tiles):
                    tk.Label(window, text = tile.dice_number, image = card_images[tile.resource_type], compound = 'center', font = "18").grid(row=i, column=j+4)
        
        window.mainloop()
