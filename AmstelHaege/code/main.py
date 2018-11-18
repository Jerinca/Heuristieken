import csv
import pandas as pd


INPUT_CSV = "https://raw.githubusercontent.com/Jerinca/Heuristieken/master/AmstelHaege/data/Gegevenshuizen.csv"

def csv_reader(filename):
    """
    Loads csv file as data frame
    """

    data = pd.read_csv(filename, index_col=0, sep=";")
    return data

if __name__ == "__main__":

    data = csv_reader(INPUT_CSV)
    print(data)
    print(data["Percentage"][0] * 10)
