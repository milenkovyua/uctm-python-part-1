'''
Да се състави програма, която задава равнина, описана чрез две точки:
begin(x,y) и end(x,y).
В равнината се задават точки, описващи местоположението на даден обект във времето.
Позициите на обекта във времето се съхраняват в списък (броят на точките не е
предварително известен).
Дефинирайте функции за:
◦ Добавяне на точка в равнината
◦ Изтриване на точка от равнината
◦ Определяне на изминатия път на обекта в равнината
◦ Отпечатване координатите на точките, които се намирад в указана подравнина (s).
В главната програма създайте меню, чрез което потребителят да изпълнява определена
функционалност от разработената програмата.
'''

import math
from typing import List, Tuple

main_square_coords = [(-50, -50), (50, 50)] # основната равнина [(x1, y1), (x2, y2)] дефинирана като глобална за по-лесна работа с нея

# is_in_square и  is_subssquare са помощни функции за по-лесна проверка
def is_in_square(point: Tuple[int, int], s: List[Tuple[int, int]]): # проверка дали точката се съдържа в равнината s
    return point[0] >= s[0][0] and point[1] >= s[0][1] and point[0] <= s[1][0] and point[1] <= s[1][1]

def is_subssquare(s1: List[Tuple[int, int]], s2: List[Tuple[int, int]]): # проверка дали s1 е подравнина на s2
    return s1[0][0] >= s2[0][0] and s1[0][1] >= s2[0][1] and s1[1][0] <= s2[1][0] and s1[1][1] <= s2[1][1]

def add_point(points, x, y):
    if (is_in_square((x, y), main_square_coords)):
        points.append((x, y))
    else:
        print('Point out of bounds')

def remove_point(points, x, y):
    for i in range(len(points)):
        if points[i] == (x, y):
            points.pop(i)
            break

def path(points):
    path = 0
    if (len(points) <= 1): # ако няма точки или има само една, няма път
        return path

    for i in range(1, len(points)):
        path += math.dist(points[i-1], points[i])
    return path

def print_points(points: List[Tuple[int, int]], s: List[Tuple[int, int]]):
    if not is_subssquare(s, main_square_coords):
        print('Invalid sub square')
        return

    for i in range(len(points)):
        if is_in_square(points[i], s):
            print(points[i])

def main():
    points = []
    while True:
        print('1. Add point')
        print('2. Remove point')
        print('3. Path')
        print('4. Print points')
        print('5. Exit')
        choice = int(input('Enter choice: '))
        if choice == 1:
            x = int(input('Enter x: '))
            y = int(input('Enter y: '))
            add_point(points, x, y)
        elif choice == 2:
            x = int(input('Enter x: '))
            y = int(input('Enter y: '))
            remove_point(points, x, y)
        elif choice == 3:
            print(path(points))
        elif choice == 4:
            s_x1 = int(input('Enter s begin x: '))
            s_y1 = int(input('Enter s begin y: '))
            s_x2 = int(input('Enter s end x: '))
            s_y2 = int(input('Enter s end y: '))
            print_points(points, [(s_x1, s_y1), (s_x2, s_y2)])
        elif choice == 5:
            break

main()