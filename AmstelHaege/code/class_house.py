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

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def calculate_distance(self, other_house):
        """
        Calculate the distance between another house.
        """
        a = (self.x - other_house.x) ** 2
        b = (self.y - other_house.y) ** 2
        c = math.sqrt(a + b)
        return c

    def calculate_dist(self, list_houses):
        """
        Calculate the distance between houses
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
        self.value *= (1 + (distances * self.perc_increase))
        print(self.value)

        return self.value


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
    list = []
    house1 = House(180, 170, 0)
    house2 = House(205, 290, 0)
    # house3 = House(140, 140, 90)
    # house4 = House(-10, 10, 90)
    # sum_distance = house1.calculate_distance(house2)
    # value = house1.calculate_value(sum_distance)
    # print(sum_distance)
    # print(value)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.axis([0, 320, 0, 360])

    house_rec1 = house1.rectangle()
    coords_house1 = house1.get_coordinates(house_rec1)
    list.append(house1)
    print(list)

    house_rec2 = house2.rectangle()
    coords_house2 = house2.get_coordinates(house_rec2)
    list.append(house2)
    hoi = house1.calculate_dist(list)

    print(hoi)

    # print(house1.coords)
    # print(house1.coords[1])
    ax.add_patch(house_rec1)
    ax.add_patch(house_rec2
    )

    # house_rec2 = house2.rectangle()
    # coords_house2 = house2.get_coordinates(house_rec2)
    # print(house2.coords)
    # print(house2.coords[2])
    # print("test")
    # print(house2.in_map())
    # # print(coords_house2)
    # ax.add_patch(house_rec2)

    # print(house1.intersect(house2))

    # house_rec3 = house3.rectangle()
    # coords_house3 = house3.get_coordinates(house_rec3)
    # # print(coords_house3)
    # ax.add_patch(house_rec3)

    plt.grid()
    plt.show()
