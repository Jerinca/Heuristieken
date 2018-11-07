import math

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
    house1 = Bungalow(2, 4)
    house2 = Bungalow(5, 8)
    sum_distance = house1.calculate_distance(house2)
    value = house1.calculate_value(sum_distance)
    print(sum_distance)
    print(value)