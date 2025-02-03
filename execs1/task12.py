'''
Да се напише програма, която определя най-голямото от 3 въведени
от командния ред числа. Изведете резултата на екрана заедно с
поясняващ текст.
'''

def main():
    input_numbers = input("Enter 3 numbers (comma-separated): ")
    numbers = input_numbers.split(',')

    try:
        a, b, c = map(int, numbers)
        max_number = max(a, b, c)
        print(f"The largest number is: {max_number}")
    except ValueError:
        print(f"Invalid input: {numbers}")

main()
