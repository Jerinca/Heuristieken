import csv
import pandas as pd
import numpy as np
from random import randint
import matplotlib.pyplot as plt
from class_house import House_types, House, Bungalow, Maison
from class_area import Area
import greedy_obj_func

TOTAL_HOUSES = [20, 40, 60]
PERCENTAGES = [0.15, 0.35, 0.6]
WIDTH = 320
HEIGHT = 360

def main():

    rdm_amstelhaege = Area(20)
    rdm_amstelhaege.place_houses()
    # rdm_amstelhaege = greedy_obj_func.main()
    rdm_amstelhaege.calculate_totalvalue()
    total_value = rdm_amstelhaege.value
    rdm_amstelhaege.plot_distribution()
    print(total_value)
    best_plot = rdm_amstelhaege

    counter = 1
    while (counter >= 1):
        counter = 0
        index = 0
        for house in rdm_amstelhaege.houses_placed:
            print(index)
            old_x = house.x
            old_y = house.y

            for y in range(0, rdm_amstelhaege.height, 1):
                for x in range(0, rdm_amstelhaege.width, 1):
                    old_x = house.x
                    old_y = house.y

                    rdm_amstelhaege.move_house(index, x, y)
                    # print(x,y)

                    # if rdm_amstelhaege.legit_placement(house):
                    not_possible = 0
                    if not rdm_amstelhaege.houses_placed[index].in_map():
                        not_possible += 1
                        rdm_amstelhaege.move_house(index, old_x, old_y)
                        # print("bye")

                    for object in rdm_amstelhaege.houses_placed:
                        if not object == rdm_amstelhaege.houses_placed[index]:
                            if rdm_amstelhaege.houses_placed[index].intersect(object):
                                not_possible += 1
                                rdm_amstelhaege.move_house(index, old_x, old_y)
                                # print(index)

                    if not_possible == 0:
                        # print("hoi")
                        rdm_amstelhaege.calculate_totalvalue()
                        # print(rdm_amstelhaege.value)
                        # rdm_amstelhaege.plot_distribution()

                        if rdm_amstelhaege.value > total_value:
                            total_value = rdm_amstelhaege.value
                            best_plot = rdm_amstelhaege
                            counter += 1
                            # rdm_amstelhaege.plot_distribution()
                            # print("more")
                            print(total_value)
                            # print(rdm_amstelhaege.houses_placed[0].x)
                            # print(rdm_amstelhaege.houses_placed[1].x)
                        else:
                            rdm_amstelhaege.move_house(index, old_x, old_y)
            index += 1

    print(total_value)
    # print(best_plot.houses_placed[0].x)
    # print(best_plot.houses_placed[1].x)
    rdm_amstelhaege.plot_distribution()

if __name__ == "__main__":
    main()
