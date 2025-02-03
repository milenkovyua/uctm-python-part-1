'''
ВНИМАНИЕ: При повече от 10-20 милиона се наблюдава увеличаване в натоварването на процесора
и забавяне на изпълнението на програмата. За този случай е
препопръчително е да не се тества с твърде големи числа.
Не е оптимизирана да работи с изключително големи числа.
'''

import Numbers

def main():
    num = int(input("Enter a number: "))
    print(f"Sum: {Numbers.get_sum(num)}")
    print(f"Average: {Numbers.get_avg(num)}")
    print(f"Is even: {Numbers.is_even(num)}")
    print(f"Even average: {Numbers.get_even_avg(num)}")
    print(f"Text number: {Numbers.print_text_number(num)}")
    print(f"Text from number: {Numbers.print_text_from_number(num)}")
    print(f"Is palindrome: {Numbers.is_palindrome(num)}")

main()