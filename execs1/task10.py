'''
    Да се напише логически израз, който да бъде верен, ако
    поне две от цифрите на трицифрено цяло число са
    равни помежду си.
'''

def are_digits_nonunique(m):
    a = m // 100
    b = m // 10 % 10
    c = m % 10
    return a == b or b == c or a == c

def main():
    m = int(input("Enter a 3-digit number: "))
    print(are_digits_nonunique(m))

main()