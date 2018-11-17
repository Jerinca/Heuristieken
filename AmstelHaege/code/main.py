import csv
import pandas as pd


INPUT_CSV = "https://github.com/Jerinca/Heuristieken/blob/master/AmstelHaege/data/Gegevenshuizen.csv"

def csv_reader(filename):
    """
    Loads csv file as data frame
    """

    data = pd.read_csv(filename)
    return data

if __name__ == "__main__":

    data = csv_reader(INPUT_CSV)
    print(data)
