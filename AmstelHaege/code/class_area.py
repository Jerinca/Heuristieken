import csv
import pandas as pd
from random import randint
import matplotlib.pyplot as plt
from class_house import House_types, House, Bungalow, Maison
# import os
# import sys


INPUT_CSV = "https://raw.githubusercontent.com/Jerinca/Heuristieken/master/AmstelHaege/data/Gegevenshuizen.csv"
TOTAL_HOUSES = [20, 40, 60]
WIDTH = 320
HEIGHT = 360

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

    for amount in TOTAL_HOUSES:
        while len(list_houses) < amount:
             if len(list_houses) < (amount * percentages[0]):
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

             elif len(list_houses) < ((amount * percentages[0]) + (amount * percentages[1])):
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

        plot_distribution(list_houses)

    return list_houses

def plot_distribution(list_houses):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_facecolor("green")
    plt.axis([0, WIDTH, 0, HEIGHT])

    for house in list_houses:
        house_rec = house.rectangle()
        ax.add_patch(house_rec)

    plt.grid()
    plt.show()

def move_house(list, index, new_x, new_y):
    list[index].x = new_x
    list[index].y = new_y

    return (list)
    # move_house(old_list, index, randint(0, WIDTH), randint(0, HEIGHT))
def legit_placement(new_house, list_houses):
    house_rect = new_house.rectangle()
    new_house.get_coordinates(house_rect)
    print(new_house.x)
    print(new_house.y)

    if new_house.in_map():
        count = 0

        for house in list_houses:
            if not house == new_house:
                if new_house.intersect(house):
                    # count += 1
                    print("hoi")
                    return False

            if count == 0:
                print("doei")
                return True

    print("maybe")
    return False

if __name__ == "__main__":

    data = csv_reader(INPUT_CSV)
    # print(data)
    test = data["Percentage"][0]
    # print(type(test))
    dict = df_to_dict(data)
    # print(dict)
    # print(type(dict["Percentage"]["Eensgezins"]))

    list_houses = place_houses(TOTAL_HOUSES, data["Percentage"])
    # list_houses_new = move_house(list_houses, 1, randint(0, WIDTH), randint(0, HEIGHT))
    list_houses_new = move_house(list_houses, 1, list_houses[2].x + 1, list_houses[2].y + 1)
    # plot_distribution(list_houses_new)

    while not legit_placement(list_houses_new[1], list_houses_new):
        list_houses_new = move_house(list_houses_new, 1, randint(0, WIDTH), randint(0, HEIGHT))
        print("here")

    print("not here")

    # print(list_houses)
    # print(len(list_houses))
    # plot_distribution(list_houses)

    # if not house == new_house werkt niet
