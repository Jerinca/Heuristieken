import csv
import pandas as pd
from random import randint


INPUT_CSV = "https://raw.githubusercontent.com/Jerinca/Heuristieken/master/AmstelHaege/data/Gegevenshuizen.csv"
TOTAL_HOUSES = [20, 40, 60]

def csv_reader(filename):
    """
    Loads csv file as data frame
    """

    data = pd.read_csv(filename, index_col=0, sep=";")
    return data

def df_to_dict(df):
    """
    Transforms data frame to dictionary
    """

    dict = df.to_dict()
    return dict

def place_houses(list_of_houses):

    # first random generate of coordinates without duplicates
    n = # bound value coordinates (for x is 160 and y is 180)
    N = # total points (houses) for us it is [20, 40, 60]
    # also consider a certain distance
    # So retrieve random coordinate, get the corner coordinates of rectangle
    # Calculate distances relative to previous placed rectangles
    # if distance >= 0 for all corner points relative to the others than it is
    # possible to place the rectangle
    return

if __name__ == "__main__":

    data = csv_reader(INPUT_CSV)
    print(data)
    test = data["Percentage"][0]
    print(test)
    dict = df_to_dict(data)
    print(dict)
    print(dict["Percentage"]["Eensgezins"])
