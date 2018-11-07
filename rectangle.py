import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def rectangle(x, y, width, height, angle):

    bottom_left = (x, y)
    rectangle = patches.Rectangle(bottom_left, width, height, angle)
    return rectangle



if __name__ == "__main__":

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.axis([0, 160, 0, 180])
    house = rectangle(1, 1, 10, 10, 0)
    house4 = rectangle(1, 11, 10.5, 10, 0)
    house2 = rectangle(50, 100, 10, 10.5, 20)
    ax.add_patch(house)
    ax.add_patch(house2)
    ax.add_patch(house4)
    plt.show()
