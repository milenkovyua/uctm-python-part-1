'''
Документационната част е изпълнена с кратки коментари
на ключовите места в програмата. Не е необходимо от документиране
на всяка функция, предвид че е спазено правилото да се използват
имена на променливи и функции, които да са достатъчно описателни

За по-лесно разбиране на кода и по-добър intellisense са
добавени и type hints на някои места
'''

import math
import random
import itertools
from typing import List, Tuple

def area(p1: int, p2: int, p3: int) -> float:
    a = math.dist(p1, p2)
    b = math.dist(p2, p3)
    c = math.dist(p3, p1)
    p = (a + b + c) / 2
    # формулата на Херон за лице на триъгълник
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def triangle_type(p1: int, p2: int, p3: int) -> str:
    a = math.dist(p1, p2)
    b = math.dist(p2, p3)
    c = math.dist(p3, p1)
    if a == b == c:
        return 'равностранен'
    elif a == b or b == c or c == a:
        return 'равнобедрен'
    else:
        return 'разностранен'

# използваме генератор на псевдослучайни числа в конкретен интервал
def generate_points(n: int) -> List[Tuple[int, int]]:
    return [(random.randint(i,  i + 50), random.randint(i, i + 50)) for i in range(1, n + 1)]

def main():
    points = generate_points(5)
    triangles = []
    # използваме itertools за да генерираме отделни комбинации
    # от 3 точки и да итерираме през тях
    for triangle in itertools.combinations(points, 3):
        if (triangle[0][0] - triangle[1][0]) * (triangle[1][1] - triangle[2][1]) != (triangle[1][0] - triangle[2][0]) * (triangle[0][1] - triangle[1][1]):
            triangles.append(triangle)
    print('Брой на възможните триъгълници:', len(triangles))

    if len(triangles) == 0:
        return

    max_area = 0 # най-голямата площ която сме намерили до момента
    max_area_triangle = None # най-голямата площ измежду всички
    # итерираме през всички триъгълници, като заедно с това записваме
    # техните данни във файл
    with open('./triangles.txt', 'w', encoding='utf-8') as file:
        for triangle in triangles:
            p1, p2, p3 = triangle
            # a, b, c са страните на триъгълника
            a = math.dist(p1, p2)
            b = math.dist(p2, p3)
            c = math.dist(p3, p1)
            # p е периметъра на триъгълника
            p = a + b + c
            # s е лицето на триъгълника
            s = area(p1, p2, p3)
            if s > max_area:
                max_area = s
                max_area_triangle = (a, b, c, p, s, p1, p2, p3)
            file.write(f'Страни: {a:.2f}, {b:.2f}, {c:.2f}\n')
            file.write(f'Координати: {p1}, {p2}, {p3}\n')
            file.write(f'Тип: {triangle_type(p1, p2, p3)}\n')
            file.write(f'Периметър: {p:.2f}\n')
            file.write(f'Лице: {s:.2f}\n')
            file.write('======================\n')
    
    # добавяме всичко в един списък за по-лесно извеждане
    # както на конзолата, така и във файл
    biggest_triangle_data = [
        'Триъгълник с най-голяма площ:',
        f'\tСтрани: {max_area_triangle[0]:.2f}, {max_area_triangle[1]:.2f}, {max_area_triangle[2]:.2f}',
        f'\tКоординати: {max_area_triangle[5]} {max_area_triangle[6]} {max_area_triangle[7]}',
        f'\tТип: {triangle_type(max_area_triangle[5], max_area_triangle[6], max_area_triangle[7])}',
        f'\tПериметър:, {max_area_triangle[3]:.2f}',
        f'\tЛице:, {max_area_triangle[4]:.2f}',
    ]
    
    biggest_triangle_str = '\n'.join(biggest_triangle_data)
    print(biggest_triangle_str)

    # отново отваряме файла, но този път за добавяне
    with open('./triangles.txt', 'a', encoding='utf-8') as file:
        file.write(biggest_triangle_str)

main()
