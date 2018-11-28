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

TOTAL_HOUSES = [20, 40, 60]
PERCENTAGES = [0.15, 0.35, 0.6]
WIDTH = 320
HEIGHT = 360

def main():

    # We hebben een bepaalde verdeling van het aantal huizen per type dat
    # geplaatst moet worden. Stel we beginnen gewoon met 15% van de duurste
    # huizen (Maison) te plaatsen:

    # Stap 1: zet alle huizen neer, sla allemaal op in lijst en kies diegene met
    #         de meeste vrijstand?
    #         Grootste vrijstand is grootste waarde!?
    #
    #         Dus probeer distance te berekenen van huizen met de lijst van
    #         toegevoegde huizen (bij eerste stap is het een lege lijst)
    #         Wat als die gevonden is? -> voeg object toe aan aparte lijst

    # Stap 2: plaats volgend huis op alle mogelijke plekken
    #         reken afstanden uit -> kies diegene met de grootste afstanden

    # for loop over het aantal rijen: aantal rijen is hoogte wijk / hoogte huis
    #     for loop over het aantal kolommen: breedte wijk / breedte huis
    # probeer huis te plaatsen -> check if is legit placement -> move the same
    # distance further and try to place another house -> at the end move the height
    # of the house further in the row.

    houses_greedy = []
    house = House(0, 0, 0)
    bungalow = Bungalow(0, 0, 0)
    maison = Maison(0, 0, 0)

    while len(houses_greedy) < TOTAL_HOUSES[0]:

        if len(houses_greedy) < (TOTAL_HOUSES[0] * PERCENTAGES[0]):

            height_steps = np.arange(0, HEIGHT, HEIGHT / maison.length)
            width_steps = np.arange(0, WIDTH, WIDTH / maison.width)
            houses_placed = []
            distances = []

            for y_bottom_left in height_steps:
                for x_bottom_left in width_steps:

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

            max_distances_all_houses = []

            for house in enumerate(houses_placed, i):

                distances = house.calculate_dist(houses_greedy)
                # find shortest distance
                distance = max(distances)
                max_distances_all_houses.append(distance)

            # find highest value in max_distances_all_houses and corresponding
            # house and append this one to houses_greedy




if __name__ == "__main__":
    main()
