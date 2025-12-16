import pytest
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


def test_circle_positive():
    c = Circle(3)
    assert c.get_area == 28.274333882308138, 'Площадь круга с радиусом 3'
    assert c.get_perimeter == 18.84955592153876, 'Периметр круга с радиусом 3'


def test_circle_negative():
    c = Circle(3)
    assert c.get_area != 30, 'Площадь круга с радиусом 3 должен равняться 28.274333882308138'
    assert c.get_perimeter != 19, 'Периметр круга с радиусом 3 должен равняться 18.84955592153876'


def test_circle_input_error():
    with pytest.raises(ValueError, match='Радиус круга должны быть больше 0'):
        Circle(-3)


def test_rectangle_positive():
    r = Rectangle(3, 5)
    assert r.get_area == 15, 'Площадь прямоугольника со сторонами 3 и 5'
    assert r.get_perimeter == 16, 'Периметр прямоугольника со сторонами 3 и 5'


def test_rectangle_negative():
    r = Rectangle(3, 5)
    assert r.get_area != 17, 'Площадь прямоугольника со сторонами 3 и 5 должна равняться 15'
    assert r.get_perimeter != 14, 'Периметр прямоугольника со сторонами 3 и 5 должна равняться 16'


def test_rectangle_input_error():
    with pytest.raises(ValueError, match="Стороны прямоугольника должны быть больше 0"):
        Rectangle(3, -3)


def test_square_positive():
    s = Square(3)
    assert s.get_area == 9, 'Площадь квадрата со сторонами 3'
    assert s.get_perimeter == 12,'Периметр квадрата со сторонами 3'


def test_square_negative():
    s = Square(3)
    assert s.get_area != 10, 'Площадь квадрата со сторонами 3 должна равняться 9'
    assert s.get_perimeter != 13, 'Периметр квадрата со сторонами 3 должна равняться 12'


def test_square_input_error():
    with pytest.raises(ValueError, match="Стороны квадрата должны быть больше 0"):
        Square(-3)


def test_triangle_positive():
    s = Triangle(13, 14, 15)
    assert s.get_area == 84, 'Площадь треугольника со сторонами 13, 14 и 15'
    assert s.get_perimeter == 42, 'Периметр треугольника со сторонами 13, 14 и 15'


def test_triangle_negative():
    s = Triangle(13, 14, 15)
    assert s.get_area != 85.0, 'Площадь треугольника со сторонами 13, 14 и 15 должна равняться 84'
    assert s.get_perimeter != 43, 'Периметр треугольника со сторонами 13, 14 и 15 должна равняться 42'


def test_triangle_input_error():
    with pytest.raises(ValueError, match="Стороны треугольника должны быть больше 0"):
        Triangle(-3, 13, 14)


def test_triangle_dont_exist():
    with pytest.raises(
        ValueError,
        match="Сумма двух сторон треугольника должна быть больше третьей стороны"
    ):
        Triangle(3, 4, 11)
