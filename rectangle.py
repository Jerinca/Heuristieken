import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def rectangle(x, y, width, height, angle):

    bottom_left = (x, y)
    rectangle = patches.Rectangle(bottom_left, width, height, angle)
    return rectangle


def get_coordinates(fig):

    coords = np.array([fig.get_xy(), [fig.get_x() + fig.get_width(), fig.get_y()],
                       [fig.get_x() + fig.get_width(), fig.get_y() + fig.get_height()],
                       [fig.get_x(), fig.get_y() + fig.get_height()]])

    return coords


if __name__ == "__main__":

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.axis([0, 160, 0, 180])
    house = rectangle(1, 1, 10, 10, 0)
    coords_house = get_coordinates(house)
    print(coords_house)
    house4 = rectangle(1, 11, 10.5, 10, 0)
    house2 = rectangle(50, 100, 10, 10.5, 20)
    coords_house2 = get_coordinates(house2)
    print(coords_house2)
    ax.add_patch(house)
    ax.add_patch(house2)
    ax.add_patch(house4)
    plt.show()
