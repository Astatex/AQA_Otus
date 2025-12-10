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


class Square(Figure):
    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError(
                f"Стороны квадрата должны быть больше 0, а у тебя sideA={side_a}"
            )
        self.side_a = side_a

    @property
    def get_area(self):
        return self.side_a**2

    @property
    def get_perimeter(self):
        return self.side_a * 4


s = Square(10)
p = Square(10)
print(s.get_area)
print(p.get_perimeter)
