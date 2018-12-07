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
import time
from collections import Counter


def random(amstelhaege):

    while len(amstelhaege.houses_placed) < amstelhaege.amount_houses:
       if len(amstelhaege.houses_placed) < (amstelhaege.amount_houses * amstelhaege.portions[0]):
           x = randint(0, amstelhaege.width)
           y = randint(0, amstelhaege.height)
           new_house = House(x, y, 0)
           house_rect = new_house.rectangle()
           new_house.get_coordinates(house_rect)
           if  new_house.in_map():
               count = 0

               for house in amstelhaege.houses_placed:
                   if new_house.intersect(house):
                       count += 1

               if count == 0:

                   amstelhaege.houses_placed.append(new_house)

       elif len(amstelhaege.houses_placed) < ((amstelhaege.amount_houses * amstelhaege.portions[0]) + (amstelhaege.amount_houses * amstelhaege.portions[1])):
           x = randint(0, amstelhaege.width)
           y = randint(0, amstelhaege.height)
           new_house = Bungalow(x, y, 0)
           house_rect = new_house.rectangle()
           new_house.get_coordinates(house_rect)
           if  new_house.in_map():
               count = 0

               for house in amstelhaege.houses_placed:
                   if new_house.intersect(house):
                       count += 1

               if count == 0:

                   amstelhaege.houses_placed.append(new_house)

       else:
           x = randint(0, amstelhaege.width)
           y = randint(0, amstelhaege.height)
           new_house = Maison(x, y, 0)
           house_rect = new_house.rectangle()
           new_house.get_coordinates(house_rect)
           if  new_house.in_map():
               count = 0

               for house in amstelhaege.houses_placed:
                   if new_house.intersect(house):
                       count += 1

               if count == 0:

                   amstelhaege.houses_placed.append(new_house)

    return amstelhaege


if __name__ == '__main__':
    start_time = time.process_time()
    amstelhaege = Area(20)
    areas = []
    values = []

    for i in range(10):
        test_area = random(amstelhaege)
        value = test_area.calculate_totalvalue()
        areas.append(test_area)
        values.append(test_area.value)

    print("--- %s seconds ---" % (time.process_time() - start_time))

    max_index = [i for i, x in enumerate(values) if x == max(values)]
    min_index = [i for i, x in enumerate(values) if x == min(values)]

    for i, index in enumerate(max_index):
        area = areas[index]
        fig = area.plot_distribution()
        fig.savefig("../resultaten/random(20)/best_areas/" + "area" + str(i) + ".png")
        plt.close(fig)

    for i, index in enumerate(min_index):
        area = areas[index]
        fig = area.plot_distribution()
        fig.savefig("../resultaten/random(20)/worst_areas/" + "area" + str(i) + ".png")
        plt.close(fig)

    # count = Counter(values)
    labels, values = zip(*Counter(values).items())
    indexes = np.arange(len(labels))
    width = 1

    fig = plt.bar(indexes, values, width)
    plt.xticks(indexes + width * 0.5, labels)
    plt.title("BarChart Random")
    plt.show()
    # fig.savefig("../resultaten/random(20)/barplot.png")
    # plt.close(fig)
