'''
Да се състави функция, изчисляваща корените на квадратно уравнение от типа аx2 + bx +c
'''
import math

def main():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("No real roots.")
    elif d == 0:
        x = -b / (2 * a)
        print(f"Root: {x}")
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"Roots: {x1}, {x2}")

main()