from math import pi
from math import sqrt


def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def circle_area(r):
    area = pi * r ** 2
    return area


def rectangle_area(a, b):
    area = a * b
    return area
