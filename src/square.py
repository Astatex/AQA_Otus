from src.figure import Figure


class Square(Figure):
    def __init__(self, side_a: int):
        if side_a <= 0:
            raise ValueError(
                f"Стороны квадрата должны быть больше 0, а у тебя sideA={side_a}"
            )
        self.side_a = side_a

    def get_area(self):
        return self.side_a**2

    def get_perimeter(self):
        return self.side_a * 4
