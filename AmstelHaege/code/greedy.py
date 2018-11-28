# Project: Amstelhaege
# Name: Team Blauw
# Time: 12:48
#
# This program applies the greedy algorithm to
# the optimalization problem AmstelHaege.

TOTAL_HOUSES = [20, 40, 60]
PERCENTAGES = [0.15, 0.35, 0.6]
WIDTH = 320
HEIGHT = 360

def main():

    # We hebben een bepaalde verdeling van het aantal huizen per type dat
    # geplaatst moet worden. Stel we beginnen gewoon met 15% van de duurste
    # huizen (Maison) te plaatsen:

    # Stap 1: zet alle huizen neer, sla allemaal op in lijst en kies diegene met
    #         de meeste vrijstand?
    #         Grootste vrijstand is grootste waarde!?
    #
    #         Dus probeer distance te berekenen van huizen met de lijst van
    #         toegevoegde huizen (bij eerste stap is het een lege lijst)
    #         Wat als die gevonden is? -> voeg object toe aan aparte lijst

    # Stap 2: plaats volgend huis op alle mogelijke plekken
    #         reken afstanden uit -> kies diegene met de grootste afstanden

    # for loop over het aantal rijen: aantal rijen is hoogte wijk / hoogte huis
    #     for loop over het aantal kolommen: breedte wijk / breedte huis
    # probeer huis te plaatsen -> check if is legit placement -> move the same
    # distance further and try to place another house -> at the end move the height
    # of the house further in the row.

    houses_greedy = []

    while len(houses_greedy) < TOTAL_HOUSES[0]:
        if len(houses_greedy) < (TOTAL_HOUSES[0] * PERCENTAGES[0]):
            



if __name__ == "__main__":
    main()
