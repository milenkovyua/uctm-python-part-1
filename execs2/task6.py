'''
Да се състави програма в която да се съхранява информация за името, възрастта, височината и
теглото на служители от дадена организация. За всеки служител да се изчисли индекса на
телесна маса (ИТМ)......
'''

def get_bmi(weight, height):
    return weight / height ** 2

def get_category(bmi):
    if bmi < 18.5:
        return 'Поднормено тегло'
    elif bmi < 25:
        return 'Нормално тегло'
    elif bmi < 30:
        return 'Наднормено тегло'
    elif bmi < 35:
        return 'Затлъстяване I степен'
    elif bmi < 40:
        return 'Затлъстяване II степен'
    else:
        return 'Затлъстяване III степен'
    
def get_correction(weight, height):
    return (24.9 - get_bmi(weight, height)) * height ** 2

def main():
    number_of_employees = int(input('Брой служители: '))
    employees = []
    for i in range(number_of_employees):
        name = input('Име: ')
        age = int(input('Възраст: '))
        height = float(input('Височина: '))
        weight = float(input('Тегло: '))
        bmi = get_bmi(weight, height)
        category = get_category(bmi)
        correction = get_correction(weight, height)
        
        employees.append({
            'name': name,
            'age': age,
            'height': height,
            'weight': weight,
            'bmi': bmi,
            'category': category,
            'correction': correction
        })

    # as we don't have specific requirements for the output, we will just print the employees
    # array for better readability
    for employee in employees:
        print(employee)

main()
