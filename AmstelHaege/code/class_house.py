import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class House_types(object):
    """
    Representation of a house (parent) in Amstelhaege
    """

    def __init__(self, x, y, angle):
        """
        Initialize house as a single coordinate.
        """
        self.x = x
        self.y = y
        self.angle = angle
        self.color = "grey"
        self.value = 0
        self.perc_increase = 0
        self.length = 0
        self.width = 0
        self.portion = 0
        self.coords = []

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

    # def too_many(self, max_houses, amount_houses):
    #     """
    #     Check if there are too many houses already.
    #     """
    #     max_houses *= self.portion
    #     if amount_houses > max_houses:
    #         return True
    #     return False

    def rectangle(self):

        bottom_left = (self.x, self.y)
        rectangle = patches.Rectangle(bottom_left, self.width, self.length, self.angle, color=self.color)
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

    def __eq__(self, other):
        return self.__dict__==other.__dict__


class House(House_types):
    """
    Representation of a house (child) in Amstelhaege
    """

    def __init__(self, x, y, angle):
        House_types.__init__(self, x, y, angle)
        self.color = "yellow"
        self.value = 285000
        self.perc_increase = 0.03
        self.length = 20
        self.width = 20
        self.portion = 0.60 # 60% van de woningen
        self.coords = []

class Bungalow(House_types):
    """
    Representation of a Bungalow (child) in Amstelhaege
    """

    def __init__(self, x, y, angle):
        House_types.__init__(self, x, y, angle)
        self.color = "blue"
        self.value = 399000
        self.perc_increase = 0.04
        self.length = 26
        self.width = 21
        self.portion = 0.25
        self.coords = []

class Maison(House_types):
    """
    Representation of a Maison (child) in Amstelhaege
    """

    def __init__(self, x, y, angle):
        House_types.__init__(self, x, y, angle)
        self.color = "red"
        self.value = 610000
        self.perc_increase = 0.06
        self.length = 34
        self.width = 33
        self.portion = 0.15
        self.coords = []


if __name__ == "__main__":
    house1 = Bungalow(110, 50, 0)
    house2 = Maison(10, -2, 0)
    house3 = House(140, 140, 90)
    house4 = House(-10, 10, 90)
    sum_distance = house1.calculate_distance(house2)
    value = house1.calculate_value(sum_distance)
    print(sum_distance)
    print(value)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.axis([0, 320, 0, 360])

    house_rec1 = house1.rectangle()
    coords_house1 = house1.get_coordinates(house_rec1)
    # print(house1.coords)
    # print(house1.coords[1])
    ax.add_patch(house_rec1)

    house_rec2 = house2.rectangle()
    coords_house2 = house2.get_coordinates(house_rec2)
    print(house2.coords)
    print(house2.coords[2])
    print("test")
    print(house2.in_map())
    # print(coords_house2)
    ax.add_patch(house_rec2)

    # print(house1.intersect(house2))

    house_rec3 = house3.rectangle()
    coords_house3 = house3.get_coordinates(house_rec3)
    # print(coords_house3)
    ax.add_patch(house_rec3)

    plt.grid()
    plt.show()
