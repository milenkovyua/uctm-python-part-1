'''
Да се напише програма, която изчислява сумата и средната стойност
на числата в интервала от 1 до 100. Да се използват инструкциите
for и while. Да се изведат резултатите с подходящ текст.
'''

def main():
    # 1. Чрез for
    sum_for = 0
    for i in range(1, 101):
        sum_for += i
    print(f"Sum: {sum_for}")

    # 2. Чрез while
    sum_while = 0
    i = 1
    while i <= 100:
        sum_while += i
        i += 1
    print(f"Average: {sum_while / 100}")

main()