# importeer de gebruikte structuur
import csv
import pandas as pd
from class_house import House_types, House, Bungalow, Maison
from class_area import Area
import greedy
import hill_climber
import add_random

def main():
    amstelhaege = Area(20)

    # # random
    # A = add_random.random(amstelhaege_random)

    # constructive
    B1 = greedy.greedy_distance(amstelhaege)
    B2 = greedy.greedy_obj(amstelhaege)
    B3 = greedy.greedy_heurestics(amstelhaege)

    # iterative
    # C1 = hill_climber.stochastic(A, 5)
    # C2 = hill_climber.steepest_ascent(A)
    # C3 = hill_climber.random_systematic(A, 2)

if __name__ == "__main__":
    main()
