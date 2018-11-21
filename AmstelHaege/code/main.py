# importeer de gebruikte structuur
from datastructuur import DataStructuur

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
