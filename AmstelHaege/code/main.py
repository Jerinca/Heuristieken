# importeer de gebruikte structuur
import csv
import pandas as pd
from class_house import House_types, House, Bungalow, Maison
from class_area import Area
import greedy
import hill_climber
import random_distribution

def main(n):
    amstelhaege = Area(n)

    # random
    A = random_distribution.random(amstelhaege)

    # constructive
    B1 = greedy.greedy_distance(amstelhaege)
    B2 = greedy.greedy_obj(amstelhaege)
    B3 = greedy.greedy_heurestics(amstelhaege)

    # iterative starting with random solution
    C1 = hill_climber.stochastic(A, 100)
    C2 = hill_climber.steepest_ascent(A)
    C3 = hill_climber.random_systematic(A, 100)

    # iterative starting with amstelhaege from greedy_obj 
    C4 = hill_climber.stochastic(B2, 100)
    C5 = hill_climber.steepest_ascent(B2)
    C6 = hill_climber.random_systematic(B2, 100)

if __name__ == "__main__":
    main(20)
