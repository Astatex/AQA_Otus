import pytest
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle

def test_add_aria_positive_rectangle_and_square():
    r = Rectangle(3, 5)
    s = Square(5)
    assert s.add_area(r) == 40, "Сумма площадей прямоугольника и квадрата"

@pytest.mark.parametrize('non_figure',
    [
        -3, 42, 'abc'
    ]
 )

def test_add_area_negative_non_figure(non_figure):
    r = Rectangle(3, 5)
    with pytest.raises(ValueError, match="Должна быть фигура"):
        r.add_area(non_figure)

@pytest.mark.parametrize(
    ('side_a', 'aria', 'perimeter'),
    [
        (3, 28.274333882308138, 18.84955592153876)
    ]
)

def test_circle_positive(side_a, aria, perimeter):
    c = Circle(side_a)
    assert c.get_area() == aria, f"Площадь круга с радиусом {side_a}"
    assert c.get_perimeter() == perimeter, f"Площадь круга с радиусом {side_a}"


def test_circle_negative():
    c = Circle(3)
    assert c.get_area() != 30, (
        "Площадь круга с радиусом 3 должен равняться 28.274333882308138"
    )
    assert c.get_perimeter() != 19, (
        "Периметр круга с радиусом 3 должен равняться 18.84955592153876"
    )

@pytest.mark.parametrize(
"radius",
    [
        0, -3
    ]
)

def test_circle_input_error(radius):
    with pytest.raises(ValueError):
        Circle(radius)


def test_rectangle_positive():
    r = Rectangle(3, 5)
    assert r.get_area() == 15, "Площадь прямоугольника со сторонами 3 и 5"
    assert r.get_perimeter() == 16, "Периметр прямоугольника со сторонами 3 и 5"


def test_rectangle_negative():
    r = Rectangle(3, 5)
    assert r.get_area() != 17, (
        "Площадь прямоугольника со сторонами 3 и 5 должна равняться 15"
    )
    assert r.get_perimeter() != 14, (
        "Периметр прямоугольника со сторонами 3 и 5 должна равняться 16"
    )

@pytest.mark.parametrize(
"side",
    [
        0, -3
    ]
)

def test_rectangle_input_error(side):
    with pytest.raises(ValueError, match="Стороны прямоугольника должны быть больше 0"):
        Rectangle(3, side)


def test_square_positive():
    s = Square(3)
    assert s.get_area() == 9, "Площадь квадрата со сторонами 3"
    assert s.get_perimeter() == 12, "Периметр квадрата со сторонами 3"


def test_square_negative():
    s = Square(3)
    assert s.get_area() != 10, "Площадь квадрата со сторонами 3 должна равняться 9"
    assert s.get_perimeter() != 13, (
        "Периметр квадрата со сторонами 3 должна равняться 12"
    )

@pytest.mark.parametrize(
"side",
    [
        0, -3
    ]
)

def test_square_input_error(side):
    with pytest.raises(ValueError, match="Стороны квадрата должны быть больше 0"):
        Square(side)


@pytest.mark.parametrize(
    ('side_a', 'site_b', 'side_c', 'aria', 'perimeter'),
    [
        (13, 14, 15, 84, 42)
    ]
)

def test_triangle_positive(side_a, site_b, side_c, aria, perimeter):
    s = Triangle(side_a, site_b, side_c)
    assert s.get_area() == aria, f"Площадь треугольника со сторонами {side_a}, {site_b} и {side_c}"
    assert s.get_perimeter() == perimeter, f"Площадь треугольника со сторонами {side_a}, {site_b} и {side_c}"

@pytest.mark.parametrize(
    ('side_a', 'site_b', 'side_c', 'aria', 'perimeter'),
    [
        (13, 14, 15, 84, 42)
    ]
)

def test_triangle_negative(side_a, site_b, side_c, aria, perimeter):
    s = Triangle(side_a, site_b, side_c)
    assert s.get_area() != 85.0, (
        f"Площадь треугольника со сторонами {side_a}, {site_b} и {side_c} должна равняться {aria}"
    )
    assert s.get_perimeter() != 43, (
        f"Площадь треугольника со сторонами {side_a}, {site_b} и {side_c} должна равняться {perimeter}"
    )

@pytest.mark.parametrize(
"side",
    [
        0, -3
    ]
)

def test_triangle_input_error(side):
    with pytest.raises(ValueError, match="Стороны треугольника должны быть больше 0"):
        Triangle(side, 14, 15)


def test_triangle_dont_exist():
    with pytest.raises(
        ValueError,
        match="Сумма двух сторон треугольника должна быть больше третьей стороны",
    ):
        Triangle(3, 4, 11)
