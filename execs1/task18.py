'''
Да се напише програма, при която потребителят трябва да отгатне
случайно генерирано от програмата цяло число в интервала от 1 до 100.
Потребителят въвежда своето предположение, а програмата извежда едно
от следните съобщения "Try higher", "Try lower" , докато не се
отгатне генерираното число. Накрая програмата трябва да изведе
съобщението: "You win! You got it in n trials".
'''
import random

def main():
    number = random.randint(1, 100)
    guess = None
    trials = 0

    while guess != number:
        guess = int(input("Enter your guess: "))
        trials += 1

        if guess < number:
            print("Try higher")
        elif guess > number:
            print("Try lower")

    print(f"You win! You got it in {trials} trials")

main()
