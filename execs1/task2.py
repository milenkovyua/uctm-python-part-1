'''
 Да се състави програма за преобразуване на галони в литри (1 галон =3.7854 литра).
 Да се изведе резултатът само с 3 знака след десетичната точка. Да се добави въвеждане
 на галоните от командния ред (или конзолата).
'''
import sys

def gallons_to_liters(gallons):
    return round(gallons * 3.7854, 3)

def main():
    if len(sys.argv) > 1:
        try:
            gallons = float(sys.argv[1])
        except ValueError:
            print("Invalid input. Expecting a number.")
            return
    else:
        gallons = float(input("Enter gallons: "))
    
    liters = gallons_to_liters(gallons)
    print(f"{gallons} gallons is {liters} liters")

main()