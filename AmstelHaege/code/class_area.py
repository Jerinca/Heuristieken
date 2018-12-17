import csv
import pandas as pd
from random import randint
import matplotlib.pyplot as plt
from class_house import House_types, House, Bungalow, Maison

# use this file as input
INPUT_CSV = "https://raw.githubusercontent.com/Jerinca/Heuristieken/master/AmstelHaege/data/Gegevenshuizen.csv"

class Area(object):
    """
    Representation of the area Amstelhaege
    Width and Height are taken from csv file
    and set as class attributes.
    """

    # set w, h, and proportion of houses
    height = 360
    width = 320
    portions = [0.6, 0.25, 0.15]

    def __init__(self, amount_houses):
        """
        Initialize area with a list for amount of houses to place
        and the portions of the different types of houses.
        """

        self.value = 0
        self.amount_houses = amount_houses
        self.houses_placed = []

    def __eq__(self, other):
        """
        Makes sure you can compare objects
        """
        return self.__dict__ == other.__dict__

    def __hash__(self):
        """
        Hash function for the houses that need to be placed
        """
        return hash(self.value, self.amount_houses, self.houses_placed)


    def csv_reader(self, filename):
        """
        Loads csv file as data frame
        """
        data = pd.read_csv(filename, index_col=0, sep=";", decimal=",")
        return data

    def df_to_dict(self, df):
        """
        Transforms data frame to dictionary
        """
        dict = df.to_dict()
        return dict

    # def place_house(self, new_house):
    #     """
    #     Function that place house one house in area
    #     """
    #
    #     count = 0
    #
    #     # if new house in the map set counter 0
    #     if not new_house.in_map():
    #         count += 1
    #
    #     # for every house placed
    #     for house in self.houses_placed:
    #         # if new house intersects with existing house counter + 1
    #         if new_house.intersect(house):
    #             count += 1
    #
    #     # if no intersection, append new house
    #     if count == 0:
    #         self.houses_placed.append(new_house)

    def place_houses(self):
        """
        Function that can place houses
        But makes sure they dont overlap
        And stay in the map
        """

        # when not yet the amout of houses needed for map
        while len(self.houses_placed) < self.amount_houses:

             # create coordinates of new House
             if len(self.houses_placed) < (self.amount_houses * self.portions[0]):
                 x = randint(0, self.width)
                 y = randint(0, self.height)
                 new_house = House(x, y, 0)
                 house_rect = new_house.rectangle()

                 # with getting the coordinates make sure there is no overlap
                 new_house.get_coordinates(house_rect)
                 if new_house.in_map():
                     count = 0
                     for house in self.houses_placed:
                         if new_house.intersect(house):
                             count += 1

                     # if no overlap append new house
                     if count == 0:
                         self.houses_placed.append(new_house)

             # create coordinates of new Bungalow
             elif len(self.houses_placed) < ((self.amount_houses * self.portions[0]) + (self.amount_houses * self.portions[1])):
                 x = randint(0, self.width)
                 y = randint(0, self.height)
                 new_house = Bungalow(x, y, 0)
                 house_rect = new_house.rectangle()

                 # with getting the coordinates make sure there is no overlap
                 new_house.get_coordinates(house_rect)
                 if new_house.in_map():
                     count = 0

                     for house in self.houses_placed:
                         if new_house.intersect(house):
                             count += 1

                     # if no overlap append new house
                     if count == 0:
                         self.houses_placed.append(new_house)

            # create coordinates of new Maison
             else:
                 x = randint(0, self.width)
                 y = randint(0, self.height)
                 new_house = Maison(x, y, 0)
                 house_rect = new_house.rectangle()

                 # with getting the coordinates make sure there is no overlap
                 new_house.get_coordinates(house_rect)
                 if new_house.in_map():
                     count = 0

                     for house in self.houses_placed:
                         if new_house.intersect(house):
                             count += 1

                     # if no overlap append new house
                     if count == 0:
                         self.houses_placed.append(new_house)


    def remove_house(self, house):
        """
        A function that makes it possible to remove a house that has been placed
        """
        self.houses_placed.remove(house)


    def calculate_totalvalue(self):
        """
        This function calculates the value of a map
        """

        counter = 0
        all_values = []

        # for every house that is placed
        for house in self.houses_placed:

            # calculate distance
            trigger = house.calculate_dist(self.houses_placed)
            counter += 1

            # calculate value for that house
            house.calculate_value(trigger)

            # append all values
            all_values.append(house.value)

        # sum up
        self.value = sum(all_values)

    def plot_distribution(self):
        """
        This function is going to plot a distribution
        With the values
        """

        # set attributes
        fig = plt.figure(figsize=(6,8))
        ax = fig.add_subplot(111)
        ax.set_facecolor("green")
        plt.axis([0, self.width, 0, self.height])

        for house in self.houses_placed:
            house_rec = house.rectangle()
            ax.add_patch(house_rec)

        plt.title(f'Map AmstelHaege: {round(self.value)}')
        plt.grid()

        return fig

    def move_house(self, index, new_x, new_y):
        """
        This function makes sure you can move a house in the map
        from old x & y coordinates to new ones
        """

        # set new x and new y
        self.houses_placed[index].x = new_x
        self.houses_placed[index].y = new_y
        rect = self.houses_placed[index].rectangle()
        self.houses_placed[index].get_coordinates(rect)
