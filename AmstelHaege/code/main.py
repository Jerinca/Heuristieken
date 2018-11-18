import csv
import pandas as pd
from random import randint
import matplotlib.pyplot as plt
from class_house import House_types, House, Bungalow, Maison
# import os
# import sys


INPUT_CSV = "https://raw.githubusercontent.com/Jerinca/Heuristieken/master/AmstelHaege/data/Gegevenshuizen.csv"
TOTAL_HOUSES = [20, 40, 60]
WIDTH = 160
HEIGHT = 180

def csv_reader(filename):
    """
    Loads csv file as data frame
    """

    data = pd.read_csv(filename, index_col=0, sep=";", decimal=",")
    return data

def df_to_dict(df):
    """
    Transforms data frame to dictionary
    """

    dict = df.to_dict()
    return dict

def place_houses(TOTAL_HOUSES, percentages):

    # first random generate of coordinates without duplicates
    # n =  bound value coordinates (for x is 160 and y is 180)
    # N =  total points (houses) for us it is [20, 40, 60]
    # also consider a certain distance
    # So retrieve random coordinate, get the corner coordinates of rectangle
    # Calculate distances relative to previous placed rectangles
    # if distance >= 0 for all corner points relative to the others than it is
    # possible to place the rectangle and can be added to list of houses
    list_houses = []

    while len(list_houses) < TOTAL_HOUSES[0]:
         if len(list_houses) < (TOTAL_HOUSES[0] * percentages[0]):
             x = randint(0, WIDTH)
             y = randint(0, HEIGHT)
             new_house = House(x, y, 0)
             house_rect = new_house.rectangle()
             new_house.get_coordinates(house_rect)
             if new_house.in_map():
                 count = 0

                 for house in list_houses:
                     if new_house.intersect(house):
                         count += 1

                 if count == 0:

                     list_houses.append(new_house)

         elif len(list_houses) < ((TOTAL_HOUSES[0] * percentages[0]) + (TOTAL_HOUSES[0] * percentages[1])):
             x = randint(0, WIDTH)
             y = randint(0, HEIGHT)
             new_house = Bungalow(x, y, 0)
             house_rect = new_house.rectangle()
             new_house.get_coordinates(house_rect)
             if new_house.in_map():
                 count = 0

                 for house in list_houses:
                     if new_house.intersect(house):
                         count += 1

                 if count == 0:

                     list_houses.append(new_house)

         else:
             x = randint(0, WIDTH)
             y = randint(0, HEIGHT)
             new_house = Maison(x, y, 0)
             house_rect = new_house.rectangle()
             new_house.get_coordinates(house_rect)
             if new_house.in_map():
                 count = 0

                 for house in list_houses:
                     if new_house.intersect(house):
                         count += 1

                 if count == 0:

                     list_houses.append(new_house)

    return list_houses

def plot_distribution(list_houses):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_facecolor("green")
    plt.axis([0, 160, 0, 180])

    for house in list_houses:
        house_rec = house.rectangle()
        ax.add_patch(house_rec)

    plt.grid()
    plt.show()


if __name__ == "__main__":

    data = csv_reader(INPUT_CSV)
    print(data)
    test = data["Percentage"][0]
    print(type(test))
    dict = df_to_dict(data)
    print(dict)
    print(type(dict["Percentage"]["Eensgezins"]))

    list_houses = place_houses(TOTAL_HOUSES, data["Percentage"])
    print(list_houses)
    print(len(list_houses))
    plot_distribution(list_houses)
