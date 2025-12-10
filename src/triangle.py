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


class Triangle(Figure):
    def __init__(self, side_a: int, side_b: int, side_c: int):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(
                f"Стороны треугольника должны быть больше 0, а у тебя sideA={side_a}, sideB={side_b}, sideC={side_c}"
            )
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_area(self):
        p = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(
            (p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))
        )

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c


s = Triangle(13, 14, 15)
p = Triangle(13, 14, 15)
print(s.get_area)
print(p.get_perimeter)
