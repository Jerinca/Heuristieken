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
    list_random_climber_values = []
    # rdm_amstelhaege = Area(5)
    # rdm_amstelhaege.place_houses()
<<<<<<< HEAD
    rdm_amstelhaege = greedy_obj_func.main(5)
=======
    rdm_amstelhaege = greedy_obj_func.greedy_obj(5)
>>>>>>> d066d7ab89ecb2dca75276495ce518577db05133
    rdm_amstelhaege.calculate_totalvalue()
    total_value = rdm_amstelhaege.value
    # rdm_amstelhaege.plot_distribution()
    print(total_value)
    # best_plot = rdm_amstelhaege
    # file = open("values_systematic_20_06122018.txt", "w")
    starttime = datetime.datetime.now()
    print(starttime.strftime("%Y-%m-%d %H:%M:%S") +"\n")

    counter_iteration = 0
    list_x_values = []

    for i in range(1000):
        counter_iteration += 1
        index = randint(0, (len(rdm_amstelhaege.houses_placed) - 1))
        y = randint(0, HEIGHT)
        x = randint(0, WIDTH)

        old_x = rdm_amstelhaege.houses_placed[index].x
        old_y = rdm_amstelhaege.houses_placed[index].y


        rdm_amstelhaege.move_house(index,y,x)

        not_possible = 0
        if not rdm_amstelhaege.houses_placed[index].in_map():
            not_possible += 1
            rdm_amstelhaege.move_house(index, old_x, old_y)
            print("bye")

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
                # print(rdm_amstelhaege.value)
                # rdm_amstelhaege.plot_distribution()
                list_x_values.append(counter_iteration)

                list_random_climber_values.append(rdm_amstelhaege.value)
                total_value = rdm_amstelhaege.value
                # best_plot = rdm_amstelhaege
                # counter += 1
                # rdm_amstelhaege.plot_distribution()
                # print("more")
                # file.write(str(total_value)+ "\n")
                # print(total_value)
                # print(rdm_amstelhaege.houses_placed[0].x)
                # print(rdm_amstelhaege.houses_placed[1].x)
            else:
                rdm_amstelhaege.move_house(index, old_x, old_y)
                # print(rdm_amstelhaege.value)

    endtime = datetime.datetime.now()
    print(endtime.strftime("%Y-%m-%d %H:%M:%S")+ "\n")
    # file.write(str(total_value))
    # file.close()
    # print(total_value)
    rdm_amstelhaege.calculate_totalvalue()
    print(rdm_amstelhaege.value)
    # print(best_plot.houses_placed[0].x)
    # print(best_plot.houses_placed[1].x)
    fig = rdm_amstelhaege.plot_distribution()
    fig.savefig('greedy_obj_hillclimber1.png')
    plt.close(fig)
    print(list_random_climber_values)
    # the histogram of the data

    # plt.show()

    plt.plot(list_x_values, list_random_climber_values, color = 'lightseagreen')
    plt.title("Random Hillclimber")
    plt.grid(True)
    plt.show()




if __name__ == "__main__":
    main()
