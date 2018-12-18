# Project AmstelHaege
# Team name: Blauw
# Members: Jerinca Vreugdenhil, Yang Yang To en Julien Fer
#
# This program contains serveral applications of a greedy algorithm


import numpy as np
import matplotlib.pyplot as plt
from class_house import House_types, House, Bungalow, Maison
from class_area import Area


def greedy_distance(amstelhaege):
    """
    This function applies a greedy approach, based on distance,
    on placing houses in the area amstelhaege, which is given by the user.
    """

    counter = 0

    while len(amstelhaege.houses_placed) < amstelhaege.amount_houses:

        if (len(amstelhaege.houses_placed) < (amstelhaege.amount_houses *
                                              amstelhaege.portions[2])):

            houses_placed = place_Maison(amstelhaege)
            counter = find_house_min_distance(
                amstelhaege, houses_placed, counter, "distance")

        elif (len(amstelhaege.houses_placed) < ((amstelhaege.amount_houses
                                                 * amstelhaege.portions[2])
                                                + (amstelhaege.amount_houses *
                                                 amstelhaege.portions[1]))):

            houses_placed = place_Bungalow(amstelhaege)
            counter = find_house_min_distance(
                amstelhaege, houses_placed, counter, "distance")

        else:

            houses_placed = place_House(amstelhaege)
            counter = find_house_min_distance(
                amstelhaege, houses_placed, counter, "distance")

    return amstelhaege


def greedy_obj(amstelhaege):
    """
    This function applies a greedy approach, based on the total value of the area,
    on placing houses in the area amstelhaege, which is given by the user.
    """

    counter = 0

    while len(amstelhaege.houses_placed) < amstelhaege.amount_houses:

        if (len(amstelhaege.houses_placed) < (amstelhaege.amount_houses
                                              * amstelhaege.portions[2])):

            houses_placed = place_Maison(amstelhaege)
            counter = find_house_max_value(
                amstelhaege, houses_placed, counter, "obj_func")

        elif (len(amstelhaege.houses_placed) < ((amstelhaege.amount_houses *
                                                amstelhaege.portions[2]) +
                                                (amstelhaege.amount_houses *
                                                   amstelhaege.portions[1]))):

            houses_placed = place_Bungalow(amstelhaege)
            counter = find_house_max_value(
                amstelhaege, houses_placed, counter, "obj_func")

        else:

            houses_placed = place_House(amstelhaege)
            counter = find_house_max_value(
                amstelhaege, houses_placed, counter, "obj_func")

    return amstelhaege


def greedy_heurestics(amstelhaege):
    """
    This function applies a greedy approach, based on the distance of a house
    to be placed to that of houses of type maison. This must be at least twice
    as far as the distance to other type houses
    """

    counter_houses = 0

    while len(amstelhaege.houses_placed) < amstelhaege.amount_houses:

        if len(amstelhaege.houses_placed) < (amstelhaege.amount_houses
                                             * amstelhaege.portions[2]):

            houses_placed = place_Maison(amstelhaege)
            counter_houses = place_with_heurestics(
                amstelhaege, houses_placed, counter_houses)

        elif (len(amstelhaege.houses_placed) < ((amstelhaege.amount_houses *
                                                 amstelhaege.portions[2]) +
                                                (amstelhaege.amount_houses *
                                                   amstelhaege.portions[1]))):

            houses_placed = place_Bungalow(amstelhaege)
            counter_houses = place_with_heurestics(
                amstelhaege, houses_placed, counter_houses)

        else:

            houses_placed = place_House(amstelhaege)
            counter_houses = place_with_heurestics(
                amstelhaege, houses_placed, counter_houses)

    return amstelhaege


def place_Maison(amstelhaege):
    """
    Places houses of type Maison on every possible place in Area
    and saves the houses in a list
    """

    houses_placed = []

    for y_bottom_left in range(0, amstelhaege.height, Maison.height):
        for x_bottom_left in range(0, amstelhaege.width, Maison.width):

            house_to_place = Maison(x_bottom_left, y_bottom_left, 0)
            house_to_place_rect = house_to_place.rectangle()
            house_to_place.get_coordinates(house_to_place_rect)
            place_house(amstelhaege, house_to_place, houses_placed)

    return houses_placed


def place_Bungalow(amstelhaege):
    """
    Places houses of type Bungalow on every possible place in Area
    and saves the houses in a list
    """

    houses_placed = []

    for y_bottom_left in range(0, amstelhaege.height, Bungalow.height):
        for x_bottom_left in range(0, amstelhaege.width, Bungalow.width):

            house_to_place = Bungalow(x_bottom_left, y_bottom_left, 0)
            house_to_place_rect = house_to_place.rectangle()
            house_to_place.get_coordinates(house_to_place_rect)
            place_house(amstelhaege, house_to_place, houses_placed)

    return houses_placed


def place_House(amstelhaege):
    """
    Places houses of type House on every possible place in Area
    and saves the houses in a list
    """

    houses_placed = []

    for y_bottom_left in range(0, amstelhaege.height, House.height):
        for x_bottom_left in range(0, amstelhaege.width, House.width):

            house_to_place = House(x_bottom_left, y_bottom_left, 0)
            house_to_place_rect = house_to_place.rectangle()
            house_to_place.get_coordinates(house_to_place_rect)
            place_house(amstelhaege, house_to_place, houses_placed)

    return houses_placed


def place_house(amstelhaege, new_house, list):
    """
    Function that checks if house to be placed is legit
    If so, append to list
    """

    count = 0

    if not new_house.in_map():
        count += 1

    for house in amstelhaege.houses_placed:
        if new_house.intersect(house):
            count += 1

    if count == 0:
        list.append(new_house)


def save_distribution(amstelhaege, string, counter):
    """
    Save plot of distribution houses at
    specific moment during the greedy algorithm
    """

    amstelhaege.calculate_totalvalue()
    fig = amstelhaege.plot_distribution()
    fig.savefig("../resultaten/greedy_" + string + "(" +
                str(amstelhaege.amount_houses) + ")/" + "house" + str(counter) + ".png")
    plt.close(fig)


def find_house_min_distance(amstelhaege, houses_placed, counter, string):
    """
    This function calculates the distance of each house in houses_placed
    Finds the min distance of each house to other houses in Area and selects
    from this the house with the greatest distance.
    """

    min_distances_houses = []

    for house in houses_placed:

        distance_min = house.calculate_dist(amstelhaege.houses_placed)
        min_distances_houses.append(distance_min)

    maxpos = min_distances_houses.index(max(min_distances_houses))
    amstelhaege.houses_placed.append(houses_placed[maxpos])
    counter += 1
    save_distribution(amstelhaege, string, counter)

    return counter


def find_house_max_value(amstelhaege, houses_placed, counter, string):
    """
    Append every house to amstelhaege, calculate value, store value
    and then remove house (for every possible house)
    """

    values_area = []

    for house in houses_placed:

        amstelhaege.houses_placed.append(house)
        amstelhaege.calculate_totalvalue()
        values_area.append(amstelhaege.value)
        amstelhaege.remove_house(house)

    maxpos = values_area.index(max(values_area))
    amstelhaege.houses_placed.append(houses_placed[maxpos])
    counter += 1
    save_distribution(amstelhaege, string, counter)

    return counter


def find_dist_Maison_Other(amstelhaege, house):
    """
    Calculates the distance of a house to Maison and other type of houses
    in amstelhaege. Returns two lists with the values.
    """

    all_distances_maison = []
    all_distance_to_other_houses = []
    # vind minimale afstand van huis tot maison and de andere types!!!
    for house_area in amstelhaege.houses_placed:
        temp = []
        if house_area.name == "bungalow" or house_area.name == "house":
            temp.append(house_area)
            distance = house.calculate_dist(temp)
            all_distance_to_other_houses.append(distance)

        elif house_area.name == "maison":
            temp.append(house_area)
            distance = house.calculate_dist(temp)
            all_distances_maison.append(distance)

    return all_distances_maison, all_distance_to_other_houses


def calc_temp_value(amstelhaege, house, values_area):
    """
    This function places temporarely a house in the area amstelhaege, calculates
    the value of the area and append this value to a list.
    """

    amstelhaege.houses_placed.append(house)
    amstelhaege.calculate_totalvalue()
    values_area.append(amstelhaege.value)
    amstelhaege.remove_house(house)


def apply_heurestics(list1, list2, houses_placed, values_area):
    """
    Applies heurestic method to find houses with a distance to maison that is
    twice the size of the distance to other type houses.
    """

    counter = 0
    houses_heurestics = []
    values_heurestics = []

    # applies herustic method to the distances found
    for dist_maison, dist_other in zip(list1, list2):
        if dist_maison >= (2 * dist_other):
            houses_heurestics.append(houses_placed[counter])
            values_heurestics.append(values_area[counter])

        counter += 1

    return houses_heurestics, values_heurestics


def check_heurestics(val_heur, houses_heur, values, houses_placed, counter):
    """
    This function checks if there are any houses that suffices the heurestic
    method. If so, append to Area. If not, append house which causes the highest
    values of the area.
    """

    if len(houses_heur) > 0:
        maxpos = val_heur.index(max(val_heur))
        amstelhaege.houses_placed.append(houses_heur[maxpos])
        counter += 1
        save_distribution(amstelhaege, "heurestics", counter)
    else:
        maxpos = values.index(max(values))
        amstelhaege.houses_placed.append(houses_placed[maxpos])
        counter += 1
        save_distribution(amstelhaege, "heurestics", counter)

    return counter


def place_with_heurestics(amstelhaege, houses_placed, counter_houses):
    """
    Place houses of type maison according the heurestic that the house to be
    placed should favor a distance to maison that is twice the distance to other
    houses
    """

    min_distances_to_maison = []
    min_distance_to_other_houses = []
    values_area = []

    for house in houses_placed:

        all_distances_maison, all_distance_to_other_houses = find_dist_Maison_Other(
            amstelhaege, house)

        # vind minimale afstand van te plaatsen huis tot maison and other houses
        if len(all_distances_maison) > 0 and len(all_distance_to_other_houses) > 0:
            min_distances_to_maison.append(min(all_distances_maison))
            min_distance_to_other_houses.append(
                min(all_distance_to_other_houses))

        calc_temp_value(amstelhaege, house, values_area)

    houses_heurestics, values_heurestics = apply_heurestics(
        min_distances_to_maison, min_distance_to_other_houses, houses_placed, values_area)

    counter_houses = check_heurestics(
        values_heurestics, houses_heurestics, values_area, houses_placed, counter_houses)

    return counter_houses
