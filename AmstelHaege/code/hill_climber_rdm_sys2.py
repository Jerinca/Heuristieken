import csv
import pandas as pd
import numpy as np
from random import randint
import matplotlib.pyplot as plt
from class_house import House_types, House, Bungalow, Maison
from class_area import Area
import greedy_obj_func
import datetime

TOTAL_HOUSES = [20, 40, 60]
PERCENTAGES = [0.15, 0.35, 0.6]
WIDTH = 320
HEIGHT = 360

def main():

    rdm_amstelhaege = greedy_obj_func.greedy_obj(20)
    rdm_amstelhaege.calculate_totalvalue()
    total_value = rdm_amstelhaege.value
    print(total_value)
    starttime = datetime.datetime.now()
    print(starttime.strftime("%Y-%m-%d %H:%M:%S") +"\n")
    values = []
    x_value = 0
    x_values = []
    values.append(total_value)
    x_values.append(x_value)

    taken_coords = []

    try:
        for i in range(200):
            index = randint(0, (len(rdm_amstelhaege.houses_placed) - 1))
            print(index)

            for y in range(0, rdm_amstelhaege.height - rdm_amstelhaege.houses_placed[index].height, 1):
                for x in range(0, rdm_amstelhaege.width - rdm_amstelhaege.houses_placed[index].width, 1):
                    old_x = rdm_amstelhaege.houses_placed[index].x
                    old_y = rdm_amstelhaege.houses_placed[index].y
                    x_value += 1
                    rdm_amstelhaege.move_house(index, x, y)
                    # print(x,y)

                    # if rdm_amstelhaege.legit_placement(house):
                    not_possible = 0
                    if not rdm_amstelhaege.houses_placed[index].in_map():
                        not_possible += 1
                        rdm_amstelhaege.move_house(index, old_x, old_y)

                    else:
                        for object in rdm_amstelhaege.houses_placed:
                            if not object == rdm_amstelhaege.houses_placed[index]:
                                if rdm_amstelhaege.houses_placed[index].intersect(object):
                                    not_possible += 1
                                    rdm_amstelhaege.move_house(index, old_x, old_y)

                    if not_possible == 0:

                        rdm_amstelhaege.calculate_totalvalue()

                        if rdm_amstelhaege.value > total_value:
                            total_value = rdm_amstelhaege.value
                            values.append(rdm_amstelhaege.value)
                            x_values.append(x_value)
                        else:
                            rdm_amstelhaege.move_house(index, old_x, old_y)

    except KeyboardInterrupt:
        print(values)

    endtime = datetime.datetime.now()
    print(endtime.strftime("%Y-%m-%d %H:%M:%S")+ "\n")
    rdm_amstelhaege.calculate_totalvalue()
    print(values)
    print(rdm_amstelhaege.value)

    fig = rdm_amstelhaege.plot_distribution()
    fig.savefig('hillclimber_rdm_sys_200_20houses.png')
    plt.close(fig)

    plt.plot(x_values, values, color = 'lightseagreen')
    plt.title("Hillclimber combination random and systematic (200 times)")
    plt.xlabel("number of function evaluations")
    plt.ylabel("value amstelhaege(20)")
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()
