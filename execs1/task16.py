'''
Да се състави програма, която определя числата в диапазона от 50 до 700,
които се делят на 17 без остатък.
'''

def main():
    for i in range(50, 701):
        if i % 17 == 0:
            print(i)

main()