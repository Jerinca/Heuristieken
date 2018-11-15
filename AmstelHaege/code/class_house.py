import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class House_types(object):
    """
    Representation of a house (parent) in Amstelhaege
    """

    def __init__(self, x, y):
        """
        Initialize house as a single coordinate.
        """
        self.x = x
        self.y = y
        self.value = 0
        self.perc_increase = 0
        self.length = 0
        self.width = 0
        self.portion = 0

    def calculate_distance(self, other_house):
        """
        Calculate the distance between another house.
        """
        a = (self.x - other_house.x) ** 2
        b = (self.y - other_house.y) ** 2
        c = math.sqrt(a + b)
        return c

    def calculate_value(self, sum_distance):
        """
        Calculate the value of a house.
        """
        self.value *= (1 + (sum_distance * self.perc_increase))
        return self.value

    def too_many(self, max_houses, amount_houses):
        """
        Check if there are too many houses already.
        """
        max_houses *= self.portion
        if amount_houses > max_houses:
            return True
        return False

    def rectangle(self, angle):

        bottom_left = (self.x, self.y)
        rectangle = patches.Rectangle(bottom_left, self.width, self.length, angle)
        return rectangle


    def get_coordinates(self, fig):

        coords = np.array([fig.get_xy(), [fig.get_x() + fig.get_width(), fig.get_y()],
                           [fig.get_x() + fig.get_width(), fig.get_y() + fig.get_height()],
                           [fig.get_x(), fig.get_y() + fig.get_height()]])

        return coords

class House(House_types):
    """
    Representation of a house (child) in Amstelhaege
    """

    def __init__(self, x, y):
        House_types.__init__(self, x, y)
        self.value = 285000
        self.perc_increase = 0.03
        self.length = 10
        self.width = 10
        self.portion = 0.60 # 60% van de woningen

class Bungalow(House_types):
    """
    Representation of a Bungalow (child) in Amstelhaege
    """

    def __init__(self, x, y):
        House_types.__init__(self, x, y)
        self.value = 399000
        self.perc_increase = 0.04
        self.length = 13
        self.width = 10.5
        self.portion = 0.25

class Maison(House_types):
    """
    Representation of a Maison (child) in Amstelhaege
    """

    def __init__(self, x, y):
        House_types.__init__(self, x, y)
        self.value = 610000
        self.perc_increase = 0.06
        self.length = 17
        self.width = 16.5
        self.portion = 0.15


if __name__ == "__main__":
    house1 = Bungalow(110, 50)
    house2 = Maison(20, 100)
    house3 = House(140, 140)
    sum_distance = house1.calculate_distance(house2)
    value = house1.calculate_value(sum_distance)
    print(sum_distance)
    print(value)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.axis([0, 160, 0, 180])

    house_rec1 = house1.rectangle(90)
    coords_house1 = house1.get_coordinates(house_rec1)
    print(coords_house1)
    ax.add_patch(house_rec1)

    house_rec2 = house2.rectangle(90)
    coords_house2 = house2.get_coordinates(house_rec2)
    print(coords_house2)
    ax.add_patch(house_rec2)

    house_rec3 = house3.rectangle(90)
    coords_house3 = house3.get_coordinates(house_rec3)
    print(coords_house3)
    ax.add_patch(house_rec3)

    plt.grid()
    plt.show()
