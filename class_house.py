import math

class House_types(object):
    """
    Representation of a house in Amstelhaege
    """

    def __init__(self, x, y):
        """
        Initialize house as a single coordinate.
        """
        self.x = x
        self.y = y
        self.value = 285000
        self.perc_increase = 0.03

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
        max_houses *= 0.60
        if amount_houses > max_houses:
            return True
        return False

if __name__ == "__main__":
    house1 = House(2, 4)
    house2 = House(5, 8)
    sum_distance = house1.calculate_distance(house2)
    value = house1.calculate_value(sum_distance)
    print(sum_distance)
    print(value)
