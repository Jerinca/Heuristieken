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

list_x_values = []
list_random_climber_values = []

def basics(amstelhaege):
    blabla 

def hill_climber_random(amstelhaege):

    amstelhaege.calculate_totalvalue()
    total_value = amstelhaege.value

    print(total_value)

    starttime = datetime.datetime.now()
    print(starttime.strftime("%Y-%m-%d %H:%M:%S") +"\n")

    counter_iteration = 0

    for i in range(5):
        counter_iteration += 1
        index = randint(0, (len(amstelhaege.houses_placed) - 1))
        y = randint(0, HEIGHT)
        x = randint(0, WIDTH)

        old_x = amstelhaege.houses_placed[index].x
        old_y = amstelhaege.houses_placed[index].y


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

    endtime = datetime.datetime.now()
    print(endtime.strftime("%Y-%m-%d %H:%M:%S")+ "\n")

    amstelhaege.calculate_totalvalue()
    print(amstelhaege.value)
    print(list_random_climber_values)

    save_distribution(amstelhaege)
    plot_progress(list_x_values, list_random_climber_values)

    return amstelhaege


def plot_progress(list_x_values, list_random_climber_values):
    plt.plot(list_x_values, list_random_climber_values, color = 'lightseagreen')
    plt.title("Random Hillclimber")
    plt.xlabel("number of function evaluations")
    plt.ylabel("value amstelhaege(20)")
    plt.grid(True)
    plt.show()

def save_distribution(amstelhaege):
    fig = amstelhaege.plot_distribution()
    fig.savefig('testtest.png')
    plt.close(fig)

if __name__ == "__main__":
    amstelhaege_random = Area(5)
    amstelhaege_random.place_houses()
    # amstelhaege_greedy = greedy_obj_func.greedy_obj(5)

    hill_climber_random(amstelhaege_random)
