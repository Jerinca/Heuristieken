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

def main():

    rdm_amstelhaege = Area(20)
    rdm_amstelhaege.place_houses()
    rdm_amstelhaege.calculate_totalvalue()
    total_value = rdm_amstelhaege.value
    rdm_amstelhaege.plot_distribution()
    print(total_value)

    for house in rdm_amstelhaege.houses_placed:
        index = 0
        old_x = house.x
        old_y = house.y

        for y in range(0, rdm_amstelhaege.height, 1):
            for x in range(0, rdm_amstelhaege.width, 1):
                old_x = house.x
                old_y = house.y

                rdm_amstelhaege.move_house(index, x, y)

                if rdm_amstelhaege.legit_placement(house):
                    rdm_amstelhaege.calculate_totalvalue()

                    if rdm_amstelhaege.value > total_value:
                        total_value = rdm_amstelhaege.value
                        rdm_amstelhaege.plot_distribution()
                        print(total_value)
                else:
                    rdm_amstelhaege.move_house(index, old_x, old_y)

        # rdm_amstelhaege.plot_distribution()

if __name__ == "__main__":
    main()
