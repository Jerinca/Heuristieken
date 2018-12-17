# Project AmstelHaege
# Team name: Blauw
# Members: Jerinca Vreugdenhil, Yang Yang To en  Julien Fer
#
# This program contains serveral applications of a greedy algorithm

import csv
import pandas as pd
import numpy as np
from random import randint
import matplotlib.pyplot as plt
from class_house import House_types, House, Bungalow, Maison
from class_area import Area
import time


def greedy_distance(amstelhaege):
    """
    This function applies a greedy approach, based on distance,
    on placing houses in the area amstelhaege, which is given by the user.
    """

    counter = 0

    while len(amstelhaege.houses_placed) < amstelhaege.amount_houses:

        if len(amstelhaege.houses_placed) < (amstelhaege.amount_houses * amstelhaege.portions[2]):

            houses_placed = place_Maison(amstelhaege)
            counter = find_house_min_distance(amstelhaege, houses_placed, counter)

        elif len(amstelhaege.houses_placed) < ((amstelhaege.amount_houses * amstelhaege.portions[2]) + (amstelhaege.amount_houses * amstelhaege.portions[1])):

            houses_placed = place_Bungalow(amstelhaege)
            counter = find_house_min_distance(amstelhaege, houses_placed, counter)

        else:

            houses_placed = place_House(amstelhaege)
            counter = find_house_min_distance(amstelhaege, houses_placed, counter)

    return amstelhaege

def greedy_obj(amstelhaege):
    counter = 0

    while len(amstelhaege.houses_placed) < amstelhaege.amount_houses:

        if len(amstelhaege.houses_placed) < (amstelhaege.amount_houses * amstelhaege.portions[2]):

            houses_placed = place_Maison(amstelhaege)
            values_area = calculate_value(amstelhaege, houses_placed)

            # values_area = []
            #
            # for house in houses_placed:
            #
            #     # append every house to amstelhaege, calculate value, store value
            #     # and then remove house (for every possible house)
            #     amstelhaege.houses_placed.append(house)
            #     amstelhaege.calculate_totalvalue()
            #     values_area.append(amstelhaege.value)
            #     amstelhaege.remove_house(house)


            #finds first house with max total value area and its index and then
            # append to area
            maxpos = values_area.index(max(values_area))
            amstelhaege.houses_placed.append(houses_placed[maxpos])
            counter += 1
            amstelhaege.calculate_totalvalue()
            # fig = amstelhaege.plot_distribution()
            # fig.savefig("../resultaten/greedy_obj_func(40)/" + "house" + str(counter) + ".png")
            # plt.close(fig)

        elif len(amstelhaege.houses_placed) < ((amstelhaege.amount_houses * amstelhaege.portions[2]) + (amstelhaege.amount_houses * amstelhaege.portions[1])):

            houses_placed = []

            for y_bottom_left in range(0, amstelhaege.height, Bungalow.height):
                for x_bottom_left in range(0, amstelhaege.width, Bungalow.width):

                    house_to_place = Bungalow(x_bottom_left, y_bottom_left, 0)
                    house_to_place_rect = house_to_place.rectangle()
                    house_to_place.get_coordinates(house_to_place_rect)
                    count = 0

                    if not house_to_place.in_map():
                        count += 1

                    for house in amstelhaege.houses_placed:
                        if house_to_place.intersect(house):
                            count += 1

                    if count == 0:

                        houses_placed.append(house_to_place)

            min_distances_all_houses = []
            min_distances_to_maison = []
            min_distance_to_other_houses = []
            values_area = []

            for house in houses_placed:
                # vind minimale afstand van huis tot maison and de andere types!!!

                # vind minimale afstand van huist t.o.v alle type huizen
                distance_min_all_houses = house.calculate_dist(amstelhaege.houses_placed)
                min_distances_all_houses.append(distance_min_all_houses)

                # append every house to amstelhaege, calculate value, store value
                # and then remove house (for every possible house)
                amstelhaege.houses_placed.append(house)
                amstelhaege.calculate_totalvalue()
                value = amstelhaege.value
                values_area.append(value)
                amstelhaege.remove_house(house)

            # finds first house with maximale lowest distance and its index
            # maxpos = min_distances_houses.index(max(min_distances_houses))

            #finds first house with max total value area and its index and then
            # append to area
            maxpos = values_area.index(max(values_area))
            amstelhaege.houses_placed.append(houses_placed[maxpos])
            counter += 1
            amstelhaege.calculate_totalvalue()
            # fig = amstelhaege.plot_distribution()
            # fig.savefig("../resultaten/greedy_obj_func(40)/" + "house" + str(counter) + ".png")
            # plt.close(fig)
        else:

            houses_placed = []

            for y_bottom_left in range(0, amstelhaege.height, House.height):
                for x_bottom_left in range(0, amstelhaege.width, House.width):

                    house_to_place = House(x_bottom_left, y_bottom_left, 0)
                    house_to_place_rect = house_to_place.rectangle()
                    house_to_place.get_coordinates(house_to_place_rect)
                    count = 0

                    if not house_to_place.in_map():
                        count += 1

                    for house in amstelhaege.houses_placed:
                        if house_to_place.intersect(house):
                            count += 1

                    if count == 0:

                        houses_placed.append(house_to_place)

            min_distances_all_houses = []
            min_distances_to_maison = []
            min_distance_to_other_houses = []
            values_area = []

            for house in houses_placed:
                # vind minimale afstand van huis tot maison and de andere types!!!

                # vind minimale afstand van huist t.o.v alle type huizen
                distance_min_all_houses = house.calculate_dist(amstelhaege.houses_placed)
                min_distances_all_houses.append(distance_min_all_houses)

                # append every house to amstelhaege, calculate value, store value
                # and then remove house (for every possible house)
                amstelhaege.houses_placed.append(house)
                amstelhaege.calculate_totalvalue()
                value = amstelhaege.value
                values_area.append(value)
                amstelhaege.remove_house(house)

            # finds first house with maximale lowest distance and its index
            # maxpos = min_distances_houses.index(max(min_distances_houses))

            #finds first house with max total value area and its index and then
            # append to area
            maxpos = values_area.index(max(values_area))
            amstelhaege.houses_placed.append(houses_placed[maxpos])
            counter += 1
            amstelhaege.calculate_totalvalue()
            # fig = amstelhaege.plot_distribution()
            # fig.savefig("../resultaten/greedy_obj_func(40)/" + "house" + str(counter) + ".png")
            # plt.close(fig)


    print(amstelhaege.houses_placed)
    amstelhaege.calculate_totalvalue()
    print(amstelhaege.value)
    fig = amstelhaege.plot_distribution()
    fig.savefig("../resultaten/greedy_obj_func(60)/" + "amstelhaege" + ".png")
    plt.close(fig)
    print("--- %s seconds ---" % (time.process_time() - start_time))

    return amstelhaege


def place_Maison(amstelhaege):
    """
    Places houses of type Maison on every possible place in Area
    and saves the houses in a list
    """

    houses_placed = []

    for y_bottom_left in range(0, amstelhaege.height, Maison.height):
        for x_bottom_left in range(0, amstelhaege.width, Maison.width):

            house_to_place = Maison(x_bottom_left, y_bottom_left, 0)
            house_to_place_rect = house_to_place.rectangle()
            house_to_place.get_coordinates(house_to_place_rect)
            place_house(amstelhaege, house_to_place, houses_placed)

    return houses_placed

def place_Bungalow(amstelhaege):
    """
    Places houses of type Bungalow on every possible place in Area
    and saves the houses in a list
    """

    houses_placed = []

    for y_bottom_left in range(0, amstelhaege.height, Bungalow.height):
        for x_bottom_left in range(0, amstelhaege.width, Bungalow.width):

            house_to_place = Bungalow(x_bottom_left, y_bottom_left, 0)
            house_to_place_rect = house_to_place.rectangle()
            house_to_place.get_coordinates(house_to_place_rect)
            place_house(amstelhaege, house_to_place, houses_placed)

    return houses_placed

def place_House(amstelhaege):
    """
    Places houses of type House on every possible place in Area
    and saves the houses in a list
    """

    houses_placed = []

    for y_bottom_left in range(0, amstelhaege.height, House.height):
        for x_bottom_left in range(0, amstelhaege.width, House.width):

            house_to_place = House(x_bottom_left, y_bottom_left, 0)
            house_to_place_rect = house_to_place.rectangle()
            house_to_place.get_coordinates(house_to_place_rect)
            place_house(amstelhaege, house_to_place, houses_placed)

    return houses_placed

def place_house(amstelhaege, new_house, list):
    """
    Function that checks if house to be placed is legit
    If so, append to list
    """

    count = 0

    if not new_house.in_map():
        count += 1

    for house in amstelhaege.houses_placed:
        if new_house.intersect(house):
            count += 1

    if count == 0:
        list.append(new_house)

def save_distribution(amstelhaege, string, counter):
    """
    Save plot of distribution houses at
    specific moment during the greedy algorithm
    """

    amstelhaege.calculate_totalvalue()
    fig = amstelhaege.plot_distribution()
    fig.savefig("../resultaten/greedy_" + string + "(" + str(amstelhaege.amount_houses) + ")/" + "house" + str(counter) + ".png")
    plt.close(fig)

def find_house_min_distance(amstelhaege, houses_placed, counter):
    """
    This function calculates the distance of each house in houses_placed
    Finds the min distance of each house to other houses in Area and selects
    from this the house with the greatest distance.
    """

    min_distances_houses = []

    for house in houses_placed:

        distance_min = house.calculate_dist(amstelhaege.houses_placed)
        min_distances_houses.append(distance_min)

    maxpos = min_distances_houses.index(max(min_distances_houses))
    amstelhaege.houses_placed.append(houses_placed[maxpos])
    counter += 1
    save_distribution(amstelhaege, "distance", counter)

    return counter

def calculate_value(amstelhaege, houses_placed):
    """
    Append every house to amstelhaege, calculate value, store value
    and then remove house (for every possible house)
    """

    values_area = []

    for house in houses_placed:

        amstelhaege.houses_placed.append(house)
        amstelhaege.calculate_totalvalue()
        values_area.append(amstelhaege.value)
        amstelhaege.remove_house(house)

    return values_area


if __name__ == "__main__":
    amstelhaege = Area(20)
    amstelhaege = greedy_obj(amstelhaege)
