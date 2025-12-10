from abc import ABC, abstractmethod


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


class Rectangle(Figure):
    def __init__(self, side_a: int, side_b: int):
        if side_a <= 0 or side_b <= 0:
            raise ValueError(
                f"Стороны прямоугольника должны быть больше 0, а у тебя sideA={side_a}, sideB={side_b}"
            )
        self.side_a = side_a
        self.side_b = side_b

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2


s = Rectangle(15, 16)
p = Rectangle(15, 16)
print(s.get_area)
print(p.get_perimeter)
