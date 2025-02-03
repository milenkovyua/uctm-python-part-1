'''
Преизползва се максимално кода от task4.py (предходната задача), с леки 
модификаций за да паснат на случая.
'''

def average(results):
    return sum(results) / len(results)

# Приемаме че нямаме студенти с едни и същи резултати
def max_result(students_list, results_list):
    max_grade_index =  results_list.index(max(results_list))
    return students_list[max_grade_index]

# Приемаме че нямаме студенти с едни и същи резултати
def min_result(students_list, results_list):
    min_grade_index =  results_list.index(min(results_list))
    return students_list[min_grade_index]

def print_results(students_list, results_list):
    for i, student in enumerate(students_list):
        print(f"{student}: {results_list[i]}")

# test data: Antonio,50,Georgi,85,Mihail,70,Gergana,60,Ivan,90,Nikolai,50,Nina,65,Katya,55,Yordan,75,Daniela,80
def main():
    results = input("Enter results (comma separated values) of students and their results: ").split(',')
    students_list = [""] * int(len(results) / 2)
    grades_list = [0] * int(len(results) / 2)
    for i, k in enumerate(range(0, len(results), 2)):
        students_list[i] = results[k]
        grades_list[i] = float(results[k + 1])
    print(f"Average: {average(grades_list)}")
    print(f"Greater grade student: {max_result(students_list, grades_list)}")
    print(f"Worst grade student: {min_result(students_list, grades_list)}")
    print_results(students_list, grades_list)

main()