# triangle.py

from point import Point

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        return self.__points_list[0].distance_from_point(self.__points_list[1]) + self.__points_list[0].distance_from_point(self.__points_list[2]) + self.__points_list[1].distance_from_point(self.__points_list[2])

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())