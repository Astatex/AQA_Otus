from src.figure import Figure
import math


class Triangle(Figure):
    def __init__(self, side_a: int, side_b: int, side_c: int):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(
                f"Стороны треугольника должны быть больше 0, а у тебя sideA={side_a}, sideB={side_b}, sideC={side_c}"
            )
        elif not (
            side_a + side_b > side_c
            and side_a + side_c > side_b
            and side_b + side_c > side_a
        ):
            raise ValueError(
                "Сумма двух сторон треугольника должна быть больше третьей стороны"
            )
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_area(self):
        semi_p = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(
            (
                semi_p
                * (semi_p - self.side_a)
                * (semi_p - self.side_b)
                * (semi_p - self.side_c)
            )
        )

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
