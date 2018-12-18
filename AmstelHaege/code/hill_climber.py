from random import randint
import matplotlib.pyplot as plt
from class_house import House_types, House, Bungalow, Maison
from class_area import Area
import greedy

WIDTH = 320
HEIGHT = 360

list_x_values = []
list_random_climber_values = []
dict = {}

def basics(amstelhaege, index, x, y, counter_iteration, total_value, counter):
    """
    This function performs the necessary steps for all the hill climbers. The
    placement with a higher value will be remembered/ used.
    """
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
            counter += 1
        else:
            amstelhaege.move_house(index, old_x, old_y)

    dict['total_value'] = total_value
    dict['counter'] = counter

    return dict

def stochastic(amstelhaege, n):
    """
    This hill climber selects a random house in the area and places it on random x
    and y coordinates.
    """
    del list_x_values[:]
    del list_random_climber_values[:]
    amstelhaege.calculate_totalvalue()
    total_value = amstelhaege.value

    counter_iteration = 0
    counter = 0

    for i in range(n):
        counter_iteration += 1
        index = randint(0, (len(amstelhaege.houses_placed) - 1))
        y = randint(0, HEIGHT)
        x = randint(0, WIDTH)

        dict = basics(amstelhaege, index, x, y, counter_iteration, total_value, counter)
        total_value = dict['total_value']

    amstelhaege.calculate_totalvalue()

    save_distribution(amstelhaege, '../resultaten/hill_climber/stochastic.png')
    plot_progress(list_x_values, list_random_climber_values)

    return amstelhaege

def random_systematic(amstelhaege, n):
    """
    This hill climber selects random houses and changes the placements of those
    systematically.
    """
    del list_x_values[:]
    del list_random_climber_values[:]
    amstelhaege.calculate_totalvalue()
    total_value = amstelhaege.value

    counter_iteration = 0
    counter = 0

    try:
        for i in range(n):
            index = randint(0, (len(amstelhaege.houses_placed) - 1))
            print(index)

            for y in range(0, amstelhaege.height - amstelhaege.houses_placed[index].height, 1):
                for x in range(0, amstelhaege.width - amstelhaege.houses_placed[index].width, 1):
                    counter_iteration += 1
                    dict = basics(amstelhaege, index, x, y, counter_iteration, total_value, counter)
                    total_value = dict['total_value']

    except KeyboardInterrupt:
        print(list_random_climber_values)

    amstelhaege.calculate_totalvalue()

    save_distribution(amstelhaege, '../resultaten/hill_climber/random_systematic.png')
    plot_progress(list_x_values, list_random_climber_values)

def steepest_ascent(amstelhaege):
    """
    This hill climber selects every house in the area and changes the placements
    systematically.
    """
    del list_x_values[:]
    del list_random_climber_values[:]
    amstelhaege.calculate_totalvalue()
    total_value = amstelhaege.value

    counter_iteration= 0
    counter = 1
    try:
        while (counter >= 1):
            counter = 0
            index = 0

            for house in amstelhaege.houses_placed:
                for y in range(0, amstelhaege.height - house.height, 1):
                    for x in range(0, amstelhaege.width - house.width, 1):
                        dict = basics(amstelhaege, index, x, y, counter_iteration, total_value, counter)
                        total_value = dict['total_value']
                        counter = dict['counter']
                index += 1

    except KeyboardInterrupt:
        print(list_random_climber_values)

    amstelhaege.calculate_totalvalue()

    save_distribution(amstelhaege, '../resultaten/hill_climber/steepest_ascent.png')
    plot_progress(list_x_values, list_random_climber_values)

def plot_progress(list_x_values, list_random_climber_values):
    """
    Plots the progress of the algorithm.
    """
    fig = plt.plot(list_x_values, list_random_climber_values, color = 'lightseagreen')
    plt.title("Hillclimber")
    plt.xlabel("number of function evaluations")
    plt.ylabel("value amstelhaege(20)")
    plt.grid(True)
    plt.show()

def save_distribution(amstelhaege, name):
    """
    Save the plot with the distribution of the area.
    """
    fig = amstelhaege.plot_distribution()
    fig.savefig(name)
    plt.close(fig)
