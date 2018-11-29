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
from class_area import plot_distribution

TOTAL_HOUSES = [20, 40, 60]
PERCENTAGES = [0.15, 0.35, 0.6]
WIDTH = 320
HEIGHT = 360
AMOUNT = TOTAL_HOUSES[2]

def main():

    houses_greedy = []
    house = House(0, 0, 0)
    bungalow = Bungalow(0, 0, 0)
    maison = Maison(0, 0, 0)

    while len(houses_greedy) < AMOUNT:

        if len(houses_greedy) < (AMOUNT * PERCENTAGES[0]):

            houses_placed = []

            for y_bottom_left in range(0, HEIGHT, maison.length):
                for x_bottom_left in range(0, WIDTH, maison.width):

                    house_to_place = Maison(x_bottom_left, y_bottom_left, 0)
                    house_to_place_rect = house_to_place.rectangle()
                    house_to_place.get_coordinates(house_to_place_rect)

                    if house_to_place.in_map():
                        count = 0

                    for house in houses_greedy:
                        if house_to_place.intersect(house):
                            count += 1

                    if count == 0:

                        houses_placed.append(house_to_place)

            min_distances_houses = []

            for house in houses_placed:

                distance_min = house.calculate_dist(houses_greedy)
                min_distances_houses.append(distance_min)

            maxpos = min_distances_houses.index(max(min_distances_houses))
            houses_greedy.append(houses_placed[maxpos])


        elif len(houses_greedy) < ((AMOUNT * PERCENTAGES[0]) + (AMOUNT * PERCENTAGES[1])):

            houses_placed = []

            for y_bottom_left in range(0, HEIGHT, bungalow.length):
                for x_bottom_left in range(0, WIDTH, bungalow.width):

                    house_to_place = Bungalow(x_bottom_left, y_bottom_left, 0)
                    house_to_place_rect = house_to_place.rectangle()
                    house_to_place.get_coordinates(house_to_place_rect)

                    if house_to_place.in_map():
                        count = 0

                    for house in houses_greedy:
                        if house_to_place.intersect(house):
                            count += 1

                    if count == 0:

                        houses_placed.append(house_to_place)

            min_distances_houses = []

            for house in houses_placed:
                distance_min = house.calculate_dist(houses_greedy)
                min_distances_houses.append(distance_min)

            maxpos = min_distances_houses.index(max(min_distances_houses))
            houses_greedy.append(houses_placed[maxpos])

        else:

            houses_placed = []

            for y_bottom_left in range(0, HEIGHT, house.length):
                for x_bottom_left in range(0, WIDTH, house.width):

                    house_to_place = House(x_bottom_left, y_bottom_left, 0)
                    house_to_place_rect = house_to_place.rectangle()
                    house_to_place.get_coordinates(house_to_place_rect)

                    if house_to_place.in_map():
                        count = 0

                    for house in houses_greedy:
                        if house_to_place.intersect(house):
                            count += 1

                    if count == 0:

                        houses_placed.append(house_to_place)

            min_distances_houses = []

            for house in houses_placed:
                distance_min = house.calculate_dist(houses_greedy)
                min_distances_houses.append(distance_min)

            maxpos = min_distances_houses.index(max(min_distances_houses))
            houses_greedy.append(houses_placed[maxpos])

    print(houses_greedy)
    plot_distribution(houses_greedy)


if __name__ == "__main__":
    main()
