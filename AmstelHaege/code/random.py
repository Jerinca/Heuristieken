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

      # list_houses = []
      while len(amstelhaege.houses_placed) < amstelhaege.amount_houses:
           if len(amstelhaege.houses_placed) < (amstelhaege.amount_houses * amstelhaege.portions[0]):
               x = randint(0, amstelhaege.width)
               y = randint(0, amstelhaege.height)
               new_house = House(x, y, 0)
               house_rect = new_house.rectangle()
               new_house.get_coordinates(house_rect)
               if not new_house.in_map():
                   count += 1

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
               if not new_house.in_map():
                   count += 1

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
               if not new_house.in_map():
                   count += 1

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
    count = []
    best_areas = []
    worst_areas = []

    for i in range(10000):
        test_area = random(amstelhaege)
        value = test_area.calculate_totalvalue()
        areas.append(test_area)
        values.append(test_area.value)

    for area in areas:
