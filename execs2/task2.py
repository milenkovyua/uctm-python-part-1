'''
Да се състави функция, изчисляваща стойността на квадратно
уравнение от типа: аx2 + bx +c.
Да се реализира възможност за изчисляване на стойността за различни уравнения.
'''

def main():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    x = float(input("Enter x: "))
    result = a * x ** 2 + b * x + c
    print(f"Result: {result}")

main()