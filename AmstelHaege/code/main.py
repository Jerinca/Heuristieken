# importeer de gebruikte structuur
import csv
import pandas as pd
from class_house import House_types, House, Bungalow, Maison
from class_area import Area
import greedy_obj_func
import hill_climber
def main():
    A = DataStructuur("voorbeeld.csv")

    # probeer verschillende algoritmes
    # brute force
    B = randomize(A)

    # iteratief
    C = hill_climber(A)

    # constructief
    D = breadth_first(A)

    # evolutionair
    E = genetic(A)

if __name__ == "__main__":
    main()
