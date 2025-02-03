'''
    Да се напише логически израз, който да бъде верен,
    ако цифрите на трицифрено цяло число m са различни
'''

def are_digits_unique(m):
    a = m // 100
    b = m // 10 % 10
    c = m % 10
    return a != b and b != c and a != c

def main():
    m = int(input("Enter a 3-digit number: "))
    print(are_digits_unique(m))

main()