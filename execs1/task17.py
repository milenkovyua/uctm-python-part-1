'''
Да се състави програма, която по дадено цяло число N генерира и
отпечатва 5 цели случайни  числа в интервала от 1 до N.
'''
import random

def main():
    N = int(input("Enter N: "))
    for i in range(5):
        print(random.randint(1, N))

main()