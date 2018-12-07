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

    # rdm_amstelhaege = Area(2)
    # rdm_amstelhaege.place_houses()
    rdm_amstelhaege = greedy_obj_func.greedy_obj(2)
    rdm_amstelhaege.calculate_totalvalue()
    total_value = rdm_amstelhaege.value
    # fig1 = rdm_amstelhaege.plot_distribution()

    print(total_value)
    # best_plot = rdm_amstelhaege
    # file = open("values_systematic_20_06122018.txt", "w")
    starttime = datetime.datetime.now()
    print(starttime.strftime("%Y-%m-%d %H:%M:%S") +"\n")
    values = []
    x_values =[]
    values.append(total_value)

    # lijst met mogelijke coordinaten
    x_value = 0
    x_values.append(x_value)
    counter = 1
    try:
        while (counter >= 1):
            counter = 0
            index = 0


            for house in rdm_amstelhaege.houses_placed:
                print(index)
                old_x = house.x
                old_y = house.y

                for y in range(0, rdm_amstelhaege.height - house.height, 1):
                    for x in range(0, rdm_amstelhaege.width - house.width, 1):
                        old_x = house.x
                        old_y = house.y
                        x_value += 1

                        rdm_amstelhaege.move_house(index, x, y)
                        # print(x,y)

                        # if rdm_amstelhaege.legit_placement(house):
                        not_possible = 0
                        if not rdm_amstelhaege.houses_placed[index].in_map():
                            not_possible += 1
                            rdm_amstelhaege.move_house(index, old_x, old_y)
                            # print("bye")

                        else:
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
                                values.append(rdm_amstelhaege.value)
                                x_values.append(x_value)
                                # best_plot = rdm_amstelhaege
                                counter += 1
                                # rdm_amstelhaege.plot_distribution()
                                # print("more")
                                # file.write(str(total_value)+ "\n")
                                # print(total_value)
                                # print(rdm_amstelhaege.houses_placed[0].x)
                                # print(rdm_amstelhaege.houses_placed[1].x)
                            else:
                                rdm_amstelhaege.move_house(index, old_x, old_y)
                index += 1

    except KeyboardInterrupt:
        print(values)

    endtime = datetime.datetime.now()
    print(endtime.strftime("%Y-%m-%d %H:%M:%S")+ "\n")
    print(values)
    rdm_amstelhaege.calculate_totalvalue()
    print(rdm_amstelhaege.value)
    # file.write(str(total_value))
    # file.close()
    # print(total_value)
    # print(best_plot.houses_placed[0].x)
    # print(best_plot.houses_placed[1].x)
    fig = rdm_amstelhaege.plot_distribution()
    fig.savefig('test3.png')
    plt.close(fig)

    plt.plot(x_values, values, color = 'lightseagreen')
    plt.title("Random Hillclimber")
    plt.grid(True)

    # plt.show()

if __name__ == "__main__":
    main()
