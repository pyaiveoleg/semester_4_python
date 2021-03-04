from math import acos, degrees, sqrt
from typing import List


class Vector:
    __coordinates: List[float]

    def __init__(self, coordinates: List[float]):
        if not coordinates:
            raise ValueError("The vector must contain at least 1 element")
        self.__coordinates = coordinates

    def length(self) -> float:
        return sqrt(self.scalar_product(self))

    def scalar_product(self, other: "Vector") -> float:
        if len(self.__coordinates) != len(other.__coordinates):
            raise ValueError("Dimensions of vectors aren't equal")
        return sum(x * y for x, y in zip(self.__coordinates, other.__coordinates))

    def angle(self, other: "Vector") -> float:
        return degrees(acos(self.scalar_product(other) / (self.length() * other.length())))
