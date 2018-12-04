# Hoi, hier moet nog een greedy komen die niet selecteerd op grootste afstand
# maar op de hoogste score op moment van beslissing
# Project: Amstelhaege
# Name: Team Blauw
# Time: 12:48
#
# This program applies the greedy algorithm to
# the optimalization problem AmstelHaege.

import csv
import pandas as pd
import numpy as np
from random import randint
import matplotlib.pyplot as plt
from class_house import House_types, House, Bungalow, Maison
from class_area import Area

TOTAL_HOUSES = [20, 40, 60]
PERCENTAGES = [0.15, 0.35, 0.6]
WIDTH = 320
HEIGHT = 360
AMOUNT = TOTAL_HOUSES[2]

def main():

    amstelhaege = Area(60)
    # house = House(0, 0, 0)
    # bungalow = Bungalow(0, 0, 0)
    # maison = Maison(0, 0, 0)

    while len(amstelhaege.houses_placed) < amstelhaege.amount_houses:

        if len(amstelhaege.houses_placed) < (amstelhaege.amount_houses * amstelhaege.portions[2]):

            houses_placed = []

            for y_bottom_left in range(0, amstelhaege.height, Maison.height):
                for x_bottom_left in range(0, amstelhaege.width, Maison.width):

                    house_to_place = Maison(x_bottom_left, y_bottom_left, 0)
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
                all_distances_maison = []
                all_distance_to_other_houses = []
                # vind minimale afstand van huis tot maison and de andere types!!!

                    # als huis vergeleken wordt met maison wil je de afstand ook afzonderlijk opslaan
                    # en de afstanden tot andere type huizen apart van maison

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


    print(amstelhaege.houses_placed)
    amstelhaege.calculate_totalvalue()
    print(amstelhaege.value)
    amstelhaege.plot_distribution()


if __name__ == "__main__":
    main()
