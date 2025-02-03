'''
  Да се състави програма, която извежда сумата, разликата и
  произведението на две въведени от командния ред числа
  (както и от конзолата).
'''

import sys

def main():
    if len(sys.argv) > 2:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
        except ValueError:
            print("Invalid input. Expecting two numbers.")
            return
    else:
        try:
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
        except ValueError:
            print("Invalid input. Expecting a number.")
            return
    
    print(f"Sum: {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product: {a * b}")

main()