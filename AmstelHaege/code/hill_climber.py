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

def hill_climber(amstelhaege, x, y, index, counter_iteration):
    """
    The basics of the hill climber.
    """

    total_value = amstelhaege.value
    print(total_value)

    old_x = amstelhaege.houses_placed[index].x
    old_y = amstelhaege.houses_placed[index].y

    list_random_climber_values = []
    list_x_values = []

    amstelhaege.move_house(index,y,x)

    not_possible = 0
    if not amstelhaege.houses_placed[index].in_map():
        not_possible += 1
        amstelhaege.move_house(index, old_x, old_y)

    else:
        for object in amstelhaege.houses_placed:
            if not object == amstelhaege.houses_placed[index]:
                if amstelhaege.houses_placed[index].intersect(object):
                    not_possible += 1
                    amstelhaege.move_house(index, old_x, old_y)

    if not_possible == 0:

        amstelhaege.calculate_totalvalue()


        if amstelhaege.value > total_value:

            list_x_values.append(counter_iteration)

            list_random_climber_values.append(amstelhaege.value)
            total_value = amstelhaege.value

        else:
            amstelhaege.move_house(index, old_x, old_y)

    return list_x_values


def hill_climber_random(amstelhaege):
    """
    This hill climber selects random houses and places those on random coordinates.
    """
    counter_iteration = 0

    starttime = datetime.datetime.now()
    print(starttime.strftime("%Y-%m-%d %H:%M:%S") +"\n")


    for i in range(1000):
        counter_iteration += 1
        index = randint(0, (len(amstelhaege.houses_placed) - 1))
        y = randint(0, HEIGHT)
        x = randint(0, WIDTH)

        hill_climber(amstelhaege, x, y, index, counter_iteration)


    endtime = datetime.datetime.now()
    print(endtime.strftime("%Y-%m-%d %H:%M:%S")+ "\n")

    amstelhaege.calculate_totalvalue()
    print(amstelhaege.value)

    fig = amstelhaege.plot_distribution()
    fig.savefig('test10.png')
    plt.close(fig)
    # print(list_random_climber_values)


    # plt.plot(list_x_values, list_random_climber_values, color = 'lightseagreen')
    # plt.title("Random Hillclimber")
    # plt.grid(True)
    # plt.show()

def hill_climber_random_systematic(amstelhaege):
    """
    This hill climber selects houses randomly, but changes the coordinates systematically.
    """

def hil_climber_systematic(amstelhaege):
    """
    This hill climber uses houses in the order it was initially placed and changes the coordinates systematically.
    """



if __name__ == "__main__":
    amstelhaege_random = Area(5)
    amstelhaege_random.place_houses()
    # amstelhaege_greedy = greedy_obj_func.greedy_obj(5)

    hill_climber_random(amstelhaege_random)
    # hill_climber_random_systematic(amstelhaege_random)
