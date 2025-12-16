from src.figure import Figure
import math


class Circle(Figure):
    def __init__(self, side_r: int | float):
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
