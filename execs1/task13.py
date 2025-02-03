'''
Да се напише програма, която показва знака (+ или -) от
частното на две реални числа, без да го пресмята.
'''

def main():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    if a * b > 0:
        print("+")
    else:
        print("-")

main()