'''
Модул Numbers реализира имплементацията на функцийте.
Самите функции се използват във файла task12.py
'''

def get_sum(num):
    return sum(range(1, num + 1))

def get_avg(num):
    return get_sum(num) / num

def is_even(num):
    return num % 2 == 0

def get_even_avg(num):
    return sum([x for x in range(1, num + 1) if x % 2 == 0]) / (num // 2)

def print_text_number(num):
    text = ['нула', 'едно', 'две', 'три', 'четири', 'пет', 'шест', 'седем', 'осем', 'девет']
    return ' '.join([text[int(x)] for x in str(num)])

def get_hundreds_text(n):
    text_numbers = ["", "едно", "две", "три", "четири", "пет", "шест", "седем", "осем", "девет"]
    text_teens = ["десет", "единадесет", "дванадесет", "тринадесет", "четиринадесет", "петнадесет", "шестнадесет", "седемнадесет", "осемнадесет", "деветнадесет"]
    text_tens = ["", "десет", "двадесет", "тридесет", "четиридесет", "петдесет", "шестдесет", "седемдесет", "осемдесет", "деветдесет"]
    text_hundreds = ["", "сто", "двеста", "триста", "четиристотин", "петстотин", "шестстотин", "седемстотин", "осемстотин", "деветстотин"]

    original_n = n
    result = []
    if n >= 100:
        result.append(text_hundreds[n // 100])
        n %= 100
    if n >= 20:
        result.append(text_tens[n // 10])
        n %= 10
    if 10 <= n < 20:
        result.append("и")
        result.append(text_teens[n - 10])
    else:
        if n > 0 and original_n != n:
            result.append('и')
        result.append(text_numbers[n])
    return result

'''
Функцията print_text_from_number поддържа числа до 999 999 999.
'''
def print_text_from_number(num):
    text_thousands = ["", "хиляда", "хиляди"]
    text_millions = ["", "милион", "милиона"]

    result = []
    if num >= 1000000:
        millions = num // 1000000
        result.extend(get_hundreds_text(millions))
        result.append(text_millions[1 if millions == 1 else 2])
        num %= 1000000

    if num >= 1000:
        thousands = num // 1000
        result.extend(get_hundreds_text(thousands))
        result.append(text_thousands[1 if thousands == 1 else 2])
        num %= 1000

    result.extend(get_hundreds_text(num))

    return " ".join(result)

def is_palindrome(num):
    return str(num) == str(num)[::-1]