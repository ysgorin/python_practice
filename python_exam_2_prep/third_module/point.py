# point.py

# Expected output
# 1.4142135623730951
# 1.4142135623730951

import math

# The class is called 'Point'
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot((x - self.__x),(y - self.__y))

    def distance_from_point(self, point):
        return math.hypot((point.getx() - self.__x),(point.gety() - self.__y))

point1 = Point(0, 0)
point2 = Point(1, 1)

# Added block to avoid execution of print lines when imported.
if __name__ == "__main__":
    print(point1.distance_from_point(point2))
    print(point2.distance_from_xy(2, 0))