import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches


INPUT_CSV = "Gegevenshuizen.csv"

# # set borders
# WIDTH = 320
# HEIGHT = 360
# MIN = 0


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

    def __init__(self, input_file, x, y, angle):
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

        self.load_data(input_file)

    def load_data(self, input_file):
        """
        Load data for the objects from csv file
        """

        data = pd.read_csv(input_file)
        print(data)

    def calculate_distance(self, house):
        """
        Calculate the distance between another house.
        """
        x_bottom_and_top_left = self.coords[0][0]
        y_bottom_left_and_bottom_right = self.coords[0][1]
        y_top_left_and_top_right = self.coords[3][1]
        x_top_and_bottom_right = self.coords[2][0]

        distances = HEIGHT
        # rectangle bottomleft
        x_coord_top_right_differenthouse = house.coords[2][0]
        y_coord_top_right_differenthouse = house.coords[2][1]

        # rectangle toplelft
        x_coord_bottom_right_differenthouse = house.coords[1][0]
        y_coord_bottom_right_differenthouse = house.coords[1][1]

        # rectangle topright
        x_coord_bottom_left_differenthouse = house.coords[0][0]
        y_coord_bottom_left_differenthouse = house.coords[0][1]

        # rectangle bottom right
        x_coord_top_left_differenthouse = house.coords[3][0]
        y_coord_top_left_differenthouse = house.coords[3][1]

        # A
        if (x_coord_top_right_differenthouse < x_bottom_and_top_left and y_coord_top_right_differenthouse < y_bottom_left_and_bottom_right):
            a = (x_bottom_and_top_left - x_coord_top_right_differenthouse) ** 2
            b = (y_bottom_left_and_bottom_right - y_coord_top_right_differenthouse) ** 2
            diagonal_distance = math.sqrt(a + b)
            if diagonal_distance < distances:
                # print("a")
                distances = diagonal_distance

        # B
        elif x_coord_bottom_right_differenthouse < x_bottom_and_top_left and y_coord_bottom_right_differenthouse > y_top_left_and_top_right:
            a = (x_bottom_and_top_left - x_coord_bottom_right_differenthouse) ** 2
            b = (y_top_left_and_top_right - y_coord_bottom_right_differenthouse) ** 2
            diagonal_distance = math.sqrt(a + b)
            # print("left corner")
            if diagonal_distance < distances:
                # print("b")
                distances = diagonal_distance

        # C
        elif x_coord_bottom_left_differenthouse > x_top_and_bottom_right and y_coord_bottom_left_differenthouse > y_top_left_and_top_right:
            a = (x_top_and_bottom_right - x_coord_bottom_left_differenthouse) ** 2
            # print(a)
            b = (y_top_left_and_top_right - y_coord_bottom_left_differenthouse) ** 2
            # print(b)
            diagonal_distance = math.sqrt(a + b)
            # print("right corner")
            # print(math.sqrt(1300))
            if diagonal_distance < distances:
                # print('here')
                distances = diagonal_distance

        # D
        elif x_coord_top_left_differenthouse > x_top_and_bottom_right and y_coord_top_left_differenthouse < y_bottom_left_and_bottom_right:
            a = (x_top_and_bottom_right - x_coord_top_left_differenthouse) ** 2
            b = (y_bottom_left_and_bottom_right - y_coord_top_left_differenthouse) ** 2
            diagonal_distance = math.sqrt(a + b)
            if diagonal_distance < distances:
                # print("d")
                distances = diagonal_distance

        # E
        elif x_coord_bottom_right_differenthouse <= x_bottom_and_top_left:
            horizontal_distance = x_bottom_and_top_left - x_coord_bottom_right_differenthouse
            if horizontal_distance < distances:
                # print("e")
                distances = horizontal_distance

        # F
        elif y_coord_bottom_left_differenthouse >= y_top_left_and_top_right:
            vertical_distance = y_coord_bottom_left_differenthouse - y_top_left_and_top_right
            if vertical_distance < distances:
                # print("f")
                distances = vertical_distance

        # G
        elif x_coord_bottom_left_differenthouse >= x_top_and_bottom_right:
            horizontal_distance = x_coord_bottom_left_differenthouse - x_top_and_bottom_right
            if horizontal_distance < distances:
                # print("g")
                distances = horizontal_distance
        # H
        elif y_coord_top_left_differenthouse <= y_bottom_left_and_bottom_right:
            vertical_distance = y_bottom_left_and_bottom_right - y_coord_top_left_differenthouse
            if vertical_distance < distances:
                # print("h")
                distances = vertical_distance

        # boundry map left
        distance_left_border = x_bottom_and_top_left - MIN
        if distance_left_border < distances:
            # print("border")
            distances = distance_left_border

        # boundry map right
        distance_right_border = WIDTH - x_top_and_bottom_right
        if distance_right_border < distances:
            # print("border")
            distances = distance_right_border

        # boundry map top
        distance_top_border = HEIGHT - y_top_left_and_top_right
        if distance_top_border < distances:
            # print("border")
            distances = distance_top_border

        # boudry map bottom
        distance_bottom_border = y_bottom_left_and_bottom_right - MIN
        if distance_bottom_border < distances:
            # print("border")
            distances = distance_bottom_border

        return distances

    def calculate_dist(self, list_houses):
        """
        Calculate the distance between house(self)
        and a list of other houses
        """

        x_bottom_and_top_left = self.coords[0][0]
        y_bottom_left_and_bottom_right = self.coords[0][1]
        y_top_left_and_top_right = self.coords[3][1]
        x_top_and_bottom_right = self.coords[2][0]

        distances = HEIGHT

        if len(list_houses) == 0:
            # boundry map left
            distance_left_border = x_bottom_and_top_left - MIN
            if distance_left_border < distances:
                distances = distance_left_border

            # boundry map right
            distance_right_border = WIDTH - x_top_and_bottom_right
            if distance_right_border < distances:
                distances = distance_right_border

            # boundry map top
            distance_top_border = HEIGHT - y_top_left_and_top_right
            if distance_top_border < distances:
                distances = distance_top_border

            # boudry map bottom
            distance_bottom_border = y_bottom_left_and_bottom_right - MIN
            if distance_bottom_border < distances:
                distances = distance_bottom_border


        for house in list_houses:
            # rectangle bottomleft
            x_coord_top_right_differenthouse = house.coords[2][0]
            y_coord_top_right_differenthouse = house.coords[2][1]

            # rectangle toplelft
            x_coord_bottom_right_differenthouse = house.coords[1][0]
            y_coord_bottom_right_differenthouse = house.coords[1][1]

            # rectangle topright
            x_coord_bottom_left_differenthouse = house.coords[0][0]
            y_coord_bottom_left_differenthouse = house.coords[0][1]

            # rectangle bottom right
            x_coord_top_left_differenthouse = house.coords[3][0]
            y_coord_top_left_differenthouse = house.coords[3][1]

            # A
            if (x_coord_top_right_differenthouse < x_bottom_and_top_left and y_coord_top_right_differenthouse < y_bottom_left_and_bottom_right):
                a = (x_bottom_and_top_left - x_coord_top_right_differenthouse) ** 2
                b = (y_bottom_left_and_bottom_right - y_coord_top_right_differenthouse) ** 2
                diagonal_distance = math.sqrt(a + b)
                if diagonal_distance < distances:
                    # print("a")
                    distances = diagonal_distance

            # B
            elif x_coord_bottom_right_differenthouse < x_bottom_and_top_left and y_coord_bottom_right_differenthouse > y_top_left_and_top_right:
                a = (x_bottom_and_top_left - x_coord_bottom_right_differenthouse) ** 2
                b = (y_top_left_and_top_right - y_coord_bottom_right_differenthouse) ** 2
                diagonal_distance = math.sqrt(a + b)
                # print("left corner")
                if diagonal_distance < distances:
                    # print("b")
                    distances = diagonal_distance

            # C
            elif x_coord_bottom_left_differenthouse > x_top_and_bottom_right and y_coord_bottom_left_differenthouse > y_top_left_and_top_right:
                a = (x_top_and_bottom_right - x_coord_bottom_left_differenthouse) ** 2
                # print(a)
                b = (y_top_left_and_top_right - y_coord_bottom_left_differenthouse) ** 2
                # print(b)
                diagonal_distance = math.sqrt(a + b)
                # print("right corner")
                # print(math.sqrt(1300))
                if diagonal_distance < distances:
                    # print('here')
                    distances = diagonal_distance

            # D
            elif x_coord_top_left_differenthouse > x_top_and_bottom_right and y_coord_top_left_differenthouse < y_bottom_left_and_bottom_right:
                a = (x_top_and_bottom_right - x_coord_top_left_differenthouse) ** 2
                b = (y_bottom_left_and_bottom_right - y_coord_top_left_differenthouse) ** 2
                diagonal_distance = math.sqrt(a + b)
                if diagonal_distance < distances:
                    # print("d")
                    distances = diagonal_distance

            # E
            elif x_coord_bottom_right_differenthouse <= x_bottom_and_top_left:
                horizontal_distance = x_bottom_and_top_left - x_coord_bottom_right_differenthouse
                if horizontal_distance < distances:
                    # print("e")
                    distances = horizontal_distance

            # F
            elif y_coord_bottom_left_differenthouse >= y_top_left_and_top_right:
                vertical_distance = y_coord_bottom_left_differenthouse - y_top_left_and_top_right
                if vertical_distance < distances:
                    # print("f")
                    distances = vertical_distance

            # G
            elif x_coord_bottom_left_differenthouse >= x_top_and_bottom_right:
                horizontal_distance = x_coord_bottom_left_differenthouse - x_top_and_bottom_right
                if horizontal_distance < distances:
                    # print("g")
                    distances = horizontal_distance
            # H
            elif y_coord_top_left_differenthouse <= y_bottom_left_and_bottom_right:
                vertical_distance = y_bottom_left_and_bottom_right - y_coord_top_left_differenthouse
                if vertical_distance < distances:
                    # print("h")
                    distances = vertical_distance

            # boundry map left
            distance_left_border = x_bottom_and_top_left - MIN
            if distance_left_border < distances:
                # print("border")
                distances = distance_left_border

            # boundry map right
            distance_right_border = WIDTH - x_top_and_bottom_right
            if distance_right_border < distances:
                # print("border")
                distances = distance_right_border

            # boundry map top
            distance_top_border = HEIGHT - y_top_left_and_top_right
            if distance_top_border < distances:
                # print("border")
                distances = distance_top_border

            # boudry map bottom
            distance_bottom_border = y_bottom_left_and_bottom_right - MIN
            if distance_bottom_border < distances:
                # print("border")
                distances = distance_bottom_border

        # print(distances)
        return distances

    def calculate_value(self, distances):
        """
        Calculate the value of a house.
        """
        # self.value *= (1 + (distances * self.perc_increase))
        self.value = self.value_const + self.value_const * (distances / 2 * self.perc_increase)
        # print(self.value)



    def rectangle(self):

        bottom_left = (self.x, self.y)
        rectangle = patches.Rectangle(bottom_left, self.width, self.height, self.angle, color=self.color)
        return rectangle


    def get_coordinates(self, fig):

        self.coords = np.array([fig.get_xy(), [fig.get_x() + fig.get_width(), fig.get_y()],
                           [fig.get_x() + fig.get_width(), fig.get_y() + fig.get_height()],
                           [fig.get_x(), fig.get_y() + fig.get_height()]])

        return

    def intersect(self, other):

        br_self = self.coords[1]
        tl_self = self.coords[3]
        br_other = other.coords[1]
        tl_other = other.coords[3]

        return not (tl_self[0] > br_other[0] or tl_other[0] > br_self[0] or tl_self[1] < br_other[1] or tl_other[1] < br_self[1])


    def in_map(self):

        bottom_right_x = self.coords[1][0]
        bottom_right_y = self.coords[1][1]
        top_left_x = self.coords[3][0]
        top_left_y = self.coords[3][1]

        # if bottom_left_x < 0 or bottom_left_y < 0:
        #     return False
        # if top_right_x > 160 or top_right_y > 180
        #  return False
        return not (bottom_right_x > 320 or bottom_right_y < 0 or top_left_x < 0 or top_left_y > 360)


class House(House_types):
    """
    Representation of a house (child) in Amstelhaege
    """

    name = "house"
    width = 0
    height = 0
    color = "yellow"
    value = 0
    value_const = 0
    perc_increase = 0

    def __init__(self, x, y, angle):
        House_types.__init__(self, x, y, angle)
        self.name = "house"
        self.width = width
        self.height = height
        self.color = "yellow"
        self.value = 0
        self.value_const = value_const
        self.perc_increase = perc_increase
        self.coords = []

class Bungalow(House_types):
    """
    Representation of a Bungalow (child) in Amstelhaege
    """

    name = "bungalow"
    width = 0
    height = 0
    color = "blue"
    value = 0
    value_const = 0
    perc_increase = 0

    def __init__(self, x, y, angle):
        House_types.__init__(self, x, y, angle)
        self.name = "bungalow"
        self.width = width
        self.height = height
        self.color = "blue"
        self.value = 0
        self.value_const = value_const
        self.perc_increase = perc_increase
        self.coords = []

class Maison(House_types):
    """
    Representation of a Maison (child) in Amstelhaege
    """

    name = "maison"
    width = 0
    height = 0
    color = "red"
    value = 0
    value_const = 0
    perc_increase = 0

    def __init__(self, x, y, angle):
        House_types.__init__(self, x, y, angle)
        self.name = "maison"
        self.width = width
        self.height = height
        self.color = "red"
        self.value = 0
        self.value_const = value_const
        self.perc_increase = perc_increase
        self.coords = []


if __name__ == "__main__":
    house = House(INPUT_CSV,0 ,0)
