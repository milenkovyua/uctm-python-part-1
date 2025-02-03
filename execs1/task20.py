'''
Да се напише програма, която определя дали дадено цяло положително
число е Палиндром. Да се добави възможност за въвеждане на няколко
числа, напр. 122,232,50.
'''

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def main():
    input_n = input("Enter n (comma-separated for multiple values): ")
    n_values = input_n.split(',')

    for n in n_values:
        try:
            n = int(n)
            print(f"{n} is {'palindrome' if is_palindrome(n) else 'not palindrome'}")
        except ValueError:
            print(f"Invalid input: {n}")

main()
