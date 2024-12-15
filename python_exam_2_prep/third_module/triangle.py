# triangle.py

from point import Point

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        sum = 0
        for i in range(3):
            sum += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
        return sum

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())