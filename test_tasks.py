import pytest
from Circle import Circle
from Name import Name

def test_circle_1():
    circle1 = Circle(20)
    assert circle1.get_area() == 1256
    assert circle1.get_perimeter() == 126

def test_circle_2():
    circle2 = Circle(2)
    assert circle2.get_area() == 13
    assert circle2.get_perimeter() ==  13

def test_circle_3():
    circle3 = Circle(4.4)
    assert circle3.get_area() == 61
    assert circle3.get_perimeter() == 28

def test_name_attributes():
    name1 = Name("john", "SMITH")
    assert name1.fname == "John"
    assert name1.lname == "Smith"
    assert name1.fullname == "John Smith"
    assert name1.initials == "J.S"

def test_name_with_lowercase():
    a2 = Name("jane", "doe")
    assert a2.fullname == "Jane Doe"
    assert a2.initials == "J.D"