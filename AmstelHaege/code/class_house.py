import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# set borders
WIDTH = 320
HEIGHT = 360
MIN = 0

class House_types(object):
    """
    Representation of a house (parent) in Amstelhaege
    """
    name = "house_types"
    width = 0
    height = 0
    color = "grey"
    value_const = 0
    perc_increase = 0

    def __init__(self, x, y, angle):
        """
        Initialize house as a single coordinate.
        """
        self.x = x
        self.y = y
        self.angle = angle
        self.name = "house_types"
        self.value_const = 0
        self.width = 0
        self.height = 0
        self.color = "grey"
        self.value = 0
        self.perc_increase = 0
        self.coords = []

    def calculate_dist(self, list_houses):
        """
        Calculate the distance between house(self)
        and a list of other houses
        """

        x_left = self.coords[0][0]
        x_right = self.coords[2][0]
        y_bottom = self.coords[0][1]
        y_top = self.coords[3][1]

        distances = HEIGHT

        # boundry map left, right, top and bottom (in this specific order)
        distances = self.new_distance(x_left, MIN, distances)
        distances = self.new_distance(WIDTH, x_right, distances)
        distances = self.new_distance(HEIGHT, y_top, distances)
        distances = self.new_distance(y_bottom, MIN, distances)

        if len(list_houses) != 0:
            for house in list_houses:
                # rectangle bottomleft
                x_right_differenthouse = house.coords[2][0]
                y_top_differenthouse = house.coords[3][1]
                y_bottom_differenthouse = house.coords[0][1]
                x_left_differenthouse = house.coords[0][0]

                if (x_right_differenthouse < x_left and y_top_differenthouse < y_bottom):
                    a = (x_left - x_right_differenthouse) ** 2
                    b = (y_bottom - y_top_differenthouse) ** 2
                    distances = house.pythagorean(a, b, distances)

                elif x_right_differenthouse < x_left and y_bottom_differenthouse > y_top:
                    a = (x_left - x_right_differenthouse) ** 2
                    b = (y_top - y_bottom_differenthouse) ** 2
                    distances = house.pythagorean(a, b, distances)

                elif x_left_differenthouse > x_right and y_bottom_differenthouse > y_top:
                    a = (x_right - x_left_differenthouse) ** 2
                    b = (y_top - y_bottom_differenthouse) ** 2
                    distances = house.pythagorean(a, b, distances)

                elif x_left_differenthouse > x_right and y_top_differenthouse < y_bottom:
                    a = (x_right - x_left_differenthouse) ** 2
                    b = (y_bottom - y_top_differenthouse) ** 2
                    distances = house.pythagorean(a, b, distances)

                elif x_right_differenthouse <= x_left:
                    distances = house.new_distance(x_left, x_right_differenthouse, distances)

                elif y_bottom_differenthouse >= y_top:
                    distances = house.new_distance(y_bottom_differenthouse, y_top, distances)

                elif x_left_differenthouse >= x_right:
                    distances = house.new_distance(x_left_differenthouse, x_right, distances)

                elif y_top_differenthouse <= y_bottom:
                    distances = house.new_distance(y_bottom, y_top_differenthouse, distances)

        return distances

    def pythagorean(self, a, b, distances):
        """
        Calculate distance using Pythagorean theorem and return this distance
        if it is smaller than var distances.
        """
        pyth_distance = math.sqrt(a + b)

        if pyth_distance < distances:
            distances = pyth_distance

        return distances

    def new_distance(self, coord1, coord2, distances):
        """
        Calculate distance and return this distance if it is smaller than
        var distances.
        """
        new_distance = coord1 - coord2

        if new_distance < distances:
            distances = new_distance

        return distances

    def calculate_value(self, distances):
        """
        Calculate the value of a house.
        """
        self.value = self.value_const + self.value_const * (distances / 2 * self.perc_increase)


    def rectangle(self):
        """
        Creates a rectangle as representation of a house
        """

        bottom_left = (self.x, self.y)
        rectangle = patches.Rectangle(bottom_left, self.width, self.height, self.angle, color=self.color)
        return rectangle


    def get_coordinates(self, fig):
        """
        Get coordinates from a house
        """

        self.coords = np.array([fig.get_xy(), [fig.get_x() + fig.get_width(), fig.get_y()],
                           [fig.get_x() + fig.get_width(), fig.get_y() + fig.get_height()],
                           [fig.get_x(), fig.get_y() + fig.get_height()]])

        return

    def intersect(self, other):
        """
        Checks weather coordinates overlap or not
        """
        br_self = self.coords[1]
        tl_self = self.coords[3]
        br_other = other.coords[1]
        tl_other = other.coords[3]

        return not (tl_self[0] > br_other[0] or tl_other[0] > br_self[0] or tl_self[1] < br_other[1] or tl_other[1] < br_self[1])


    def in_map(self):
        """
        Checks if house is been placed between borders
        """
        bottom_right_x = self.coords[1][0]
        bottom_right_y = self.coords[1][1]
        top_left_x = self.coords[3][0]
        top_left_y = self.coords[3][1]

        return not (bottom_right_x > 320 or bottom_right_y < 0 or top_left_x < 0 or top_left_y > 360)


class House(House_types):
    """
    Representation of a house (child) in Amstelhaege
    """

    name = "house"
    width = 20
    height = 20
    color = "yellow"
    value = 0
    value_const = 285000
    perc_increase = 0.03

    def __init__(self, x, y, angle):
        House_types.__init__(self, x, y, angle)
        self.name = "house"
        self.width = 20
        self.height = 20
        self.color = "yellow"
        self.value = 0
        self.value_const = 285000
        self.perc_increase = 0.03
        self.coords = []

class Bungalow(House_types):
    """
    Representation of a Bungalow (child) in Amstelhaege
    """

    name = "bungalow"
    width = 21
    height = 26
    color = "blue"
    value = 0
    value_const = 399000
    perc_increase = 0.04

    def __init__(self, x, y, angle):
        House_types.__init__(self, x, y, angle)
        self.name = "bungalow"
        self.width = 21
        self.height = 26
        self.color = "blue"
        self.value = 0
        self.value_const = 399000
        self.perc_increase = 0.04
        self.coords = []

class Maison(House_types):
    """
    Representation of a Maison (child) in Amstelhaege
    """

    name = "maison"
    width = 33
    height = 34
    color = "red"
    value = 0
    value_const = 610000
    perc_increase = 0.06

    def __init__(self, x, y, angle):
        House_types.__init__(self, x, y, angle)
        self.name = "maison"
        self.width = 33
        self.height = 34
        self.color = "red"
        self.value = 0
        self.value_const = 610000
        self.perc_increase = 0.06
        self.coords = []
