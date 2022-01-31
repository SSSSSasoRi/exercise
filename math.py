from math import sqrt


def quadatic(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return x1, x2
    elif d < 0:
        print("no answer")
        return 0, 0


a = 3
b = 6
c = 3
x1, x2 = quadatic(a, b, c)
print(x1, x2)
