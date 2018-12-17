import csv
import pandas as pd
from random import randint
import matplotlib.pyplot as plt
from class_house_test import House_types, House, Bungalow, Maison
# import os
# import sys


INPUT_CSV = "https://raw.githubusercontent.com/Jerinca/Heuristieken/master/AmstelHaege/data/Gegevenshuizen.csv"
# TOTAL_HOUSES = [20, 40, 60]
# WIDTH = 320
# HEIGHT = 360

class Area(object):
    """
    Representation of the area Amstelhaege
    Width and Height are taken from csv file
    and set as class attributes.
    """

    height = 0
    width = 0
    portions = []

    def __init__(self, input_file ,amount_houses):
        """
        Initialize area with a list for amount of houses to place
        and the portions of the different types of houses.
        """

        self.value = 0
        self.amount_houses = amount_houses
        self.houses_placed = []

        self.load_data(input_file)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(self.value, self.amount_houses, self.houses_placed)

    def load_data(self, input_file):
        """
        Load data from csv file
        """

        data = pd.read_csv(input_file, index_col=0, sep=";", decimal=",")
        data = data.to_dict(orient="index")
        type_houses = list(data.keys())
        for type in type_houses:
            keys = list(data[type].keys())
            self.portions.append(data[type][])
            print(keys)
            for key in keys:
                self.portions.append(data[type][key])
        print(data)
        print(type_houses)


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

    def place_house(self, new_house):
        """
        Allen handig voor random plaatsen of iedergeval voor
        als er geen  verder vergelijkingen nodig zijn dan die al in de functie
        worden beschreven en de huizen direct geplaatst kunnen worden.
        """
        if new_house.in_map():
            count == 0

        for house in self.houses_placed:
            if new_house.intersect(house):
                count += 1

        if count == 0:
            self.houses_placed.append(new_house)

    def place_houses(self):

        # list_houses = []

        while len(self.houses_placed) < self.amount_houses:
             if len(self.houses_placed) < (self.amount_houses * self.portions[0]):
                 x = randint(0, self.width)
                 y = randint(0, self.height)
                 new_house = House(x, y, 0)
                 house_rect = new_house.rectangle()
                 new_house.get_coordinates(house_rect)
                 if new_house.in_map():
                     count = 0

                     for house in self.houses_placed:
                         if new_house.intersect(house):
                             count += 1

                     if count == 0:

                         self.houses_placed.append(new_house)

             elif len(self.houses_placed) < ((self.amount_houses * self.portions[0]) + (self.amount_houses * self.portions[1])):
                 x = randint(0, self.width)
                 y = randint(0, self.height)
                 new_house = Bungalow(x, y, 0)
                 house_rect = new_house.rectangle()
                 new_house.get_coordinates(house_rect)
                 if new_house.in_map():
                     count = 0

                     for house in self.houses_placed:
                         if new_house.intersect(house):
                             count += 1

                     if count == 0:

                         self.houses_placed.append(new_house)

             else:
                 x = randint(0, self.width)
                 y = randint(0, self.height)
                 new_house = Maison(x, y, 0)
                 house_rect = new_house.rectangle()
                 new_house.get_coordinates(house_rect)
                 if new_house.in_map():
                     count = 0

                     for house in self.houses_placed:
                         if new_house.intersect(house):
                             count += 1

                     if count == 0:

                         self.houses_placed.append(new_house)

        # self.houses_placed[7].calculate_dist(self.houses_placed)
    # return list_houses

    def remove_house(self, house):
        self.houses_placed.remove(house)


    def calculate_totalvalue(self):

        counter = 0
        all_values = []

        for house in self.houses_placed:
            trigger = house.calculate_dist(self.houses_placed)
            # print(trigger)
            counter += 1
            house.calculate_value(trigger)
            # value_house = house.value
            all_values.append(house.value)

        self.value = sum(all_values)
        # print(sum_values, "TOTALE DOEKOES!!!--------")
        # return sum_values

    def plot_distribution(self):

        fig = plt.figure(figsize=(6,8))
        ax = fig.add_subplot(111)
        ax.set_facecolor("green")
        plt.axis([0, self.width, 0, self.height])

        for house in self.houses_placed:
            house_rec = house.rectangle()
            ax.add_patch(house_rec)

        plt.title(f'Map AmstelHaege: {round(self.value)}')
        # plt.axis('scaled')
        # plt.yscale("linear")
        # plt.xscale("linear")

        plt.grid()
        # plt.show()

        return fig

    def move_house(self, index, new_x, new_y):
        self.houses_placed[index].x = new_x
        self.houses_placed[index].y = new_y
        rect = self.houses_placed[index].rectangle()
        self.houses_placed[index].get_coordinates(rect)

        # move_house(old_list, index, randint(0, WIDTH), randint(0, HEIGHT))

    def legit_placement(self, new_house):
        house_rect = new_house.rectangle()
        new_house.get_coordinates(house_rect)
        # print(new_house.x)
        # print(new_house.y)

        if not new_house.in_map():
            count += 1

            for house in self.houses_placed:
                if not house == new_house:
                    if new_house.intersect(house):
                        return False

            if count == 0:
                return True

        return False

if __name__ == "__main__":

    amstelhaege = Area(INPUT_CSV, 20)
    print(amstelhaege.portions)
