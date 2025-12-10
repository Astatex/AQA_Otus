from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Должна быть фигура")
        return self.get_area() + other_figure.get_area()


class Circle(Figure):
    def __init__(self, side_r: int):
        if side_r <= 0:
            raise ValueError(
                f"Радиус круга должны быть больше 0, а у тебя радиус = {side_r}"
            )
        self.side_r = side_r

    @property
    def get_area(self):
        return math.pi * (self.side_r**2)

    @property
    def get_perimeter(self):
        return 2 * math.pi * self.side_r


s = Circle(5)
p = Circle(5)
print(round(s.get_area, 2))
print(round(p.get_perimeter, 2))
