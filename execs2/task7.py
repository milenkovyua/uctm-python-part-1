'''
Да се дефинира речник, който да съдържа информация за студент: име, факултетен номер,
специалност, изучавани дисциплини и оценките (между 2 и 6), по които студентът е положил
изпити. Да се съставят функции за изчисляване на средния успех на студента и отпечатване
 на оценките му.
'''

def get_average_grade(grades):
    return sum(grades) / len(grades)

def print_grades(grades):
    for grade in grades:
        print(grade)

def main():
    student = {
        'name': 'Юлиян Миленков',
        'faculty_number': 'MC1652',
        'specialty': 'Информационни технологии',
        'disciplines': ['КАОС', 'ЕСПИ', 'ИММД'],
        'grades': [6, 6, 6]
    }

    average_grade = get_average_grade(student['grades'])
    print('Average grade:', average_grade)
    print('Grades:')
    print_grades(student['grades'])

main()