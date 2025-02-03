'''
    Да се напише логически израз, който да бъде верен, ако
    поне една от цифрите на трицифрено цяло число е равна на 7.
'''

def main():
    number = int(input("Enter a 3-digit number: "))
    hundreds = number // 100
    tens = number // 10 % 10
    units = number % 10
    print(hundreds == 7 or tens == 7 or units == 7)

main()