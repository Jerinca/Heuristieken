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
import time

# TOTAL_HOUSES = [20, 40, 60]
# PERCENTAGES = [0.15, 0.35, 0.6]
# WIDTH = 320
# HEIGHT = 360
# AMOUNT = TOTAL_HOUSES[2]

def main():
    start_time = time.process_time()

    amstelhaege = Area(40)
    counter = 0
    name = "house"

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

            min_distances_houses = []

            for house in houses_placed:

                distance_min = house.calculate_dist(amstelhaege.houses_placed)
                min_distances_houses.append(distance_min)

            maxpos = min_distances_houses.index(max(min_distances_houses))
            amstelhaege.houses_placed.append(houses_placed[maxpos])
            counter += 1
            amstelhaege.calculate_totalvalue()
            fig = amstelhaege.plot_distribution()
            fig.savefig("../resultaten/resultaten_greedy(40)/" + "house" + str(counter) + ".png")
            plt.close(fig)

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

            min_distances_houses = []

            for house in houses_placed:
                distance_min = house.calculate_dist(amstelhaege.houses_placed)
                min_distances_houses.append(distance_min)

            maxpos = min_distances_houses.index(max(min_distances_houses))
            amstelhaege.houses_placed.append(houses_placed[maxpos])
            counter += 1
            amstelhaege.calculate_totalvalue()
            fig = amstelhaege.plot_distribution()
            fig.savefig("../resultaten/resultaten_greedy(40)/" + "house" + str(counter) + ".png")
            plt.close(fig)

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

            min_distances_houses = []

            for house in houses_placed:
                distance_min = house.calculate_dist(amstelhaege.houses_placed)
                min_distances_houses.append(distance_min)

            maxpos = min_distances_houses.index(max(min_distances_houses))
            amstelhaege.houses_placed.append(houses_placed[maxpos])
            counter += 1
            amstelhaege.calculate_totalvalue()
            fig = amstelhaege.plot_distribution()
            fig.savefig("../resultaten/resultaten_greedy(40)/" + "house" + str(counter) + ".png")
            plt.close(fig)


    print(amstelhaege.houses_placed)
    amstelhaege.calculate_totalvalue()
    print(amstelhaege.value)
    fig = amstelhaege.plot_distribution()
    fig.savefig("../resultaten/resultaten_greedy(40)/" + "amstelhaege" + ".png")
    plt.close(fig)
    print("--- %s seconds ---" % (time.process_time() - start_time))

    return amstelhaege
if __name__ == "__main__":
    main()
