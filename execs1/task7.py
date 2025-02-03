'''
    Съставете програма, която изчислява обема на паралелепипед.
    Размерите на страните да се въведат от командния ред
    (от конзолата). Обемът да се изведе на екрана с подходящо
    съобщение.
'''

# Solution:
def volume_of_parallelepiped(a, b, c):
    return a * b * c

def main():
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
    except ValueError:
        print("Invalid input. Expecting a number.")
        return
    
    volume = volume_of_parallelepiped(a, b, c)
    print(f"Volume: {volume}")

main()