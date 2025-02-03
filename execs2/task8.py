
# Добавени са type hinting във функцийте за по-добър intellisense.
from typing import List, TypedDict

StudentsData = TypedDict('StudentName', {
    "disciplines": List[str],
    "grades": List[int],
    "average": float
})
StudentsType = dict[str, StudentsData]

def average(results: StudentsType) -> float:
    return sum([results[result]["average"] for result in results]) / len(results)

def max_result(results):
    return max(results, key=lambda x: results[x]['average']) # използвае на ламбда функция за сравнение на стойностите

def min_result(results):
    return min(results, key=lambda x: results[x]['average']) # използвае на ламбда функция за сравнение на стойностите

def print_results(results: StudentsType):
    for i, result in enumerate(results):
        print(f"Student {i + 1}: {result} : {results[result]['average']}")

def print_in_discipline(results: StudentsType, discipline: str):
    for student in results:
        if discipline in results[student]['disciplines']:
            print(f"{student}: {results[student]['grades'][results[student]['disciplines'].index(discipline)]}")

def add_student(results: StudentsType, student: str) -> StudentsType:
    results[student] = {
        "disciplines": [],
        "grades": [],
        "average": 0
    }
    return results

def remove_student(results: StudentsType, student: str) -> StudentsType:
    results.pop(student, '') # премахва студента от речника ако съществъва. подава празен стринг за default стойност
    # за да не върне KeyError грешка
    return results

def add_discipline(results: StudentsType, student: str, discipline: str, grade: int) -> StudentsType:
    results[student]["disciplines"].append(discipline)
    results[student]["grades"].append(grade)
    return update_average(results, student)

def remove_discipline(results: StudentsType, student: str, discipline: str) -> StudentsType:
    discipline_index = results[student]['disciplines'].index(discipline)
    results[student]['disciplines'].remove(discipline)
    del results[student]['grades'][discipline_index]
    return update_average(results, student)

def sort_by_name(results: StudentsType):
    return sorted(results)

def sort_by_result(results: StudentsType, ascending: bool = True):
    sorted_students = sorted(results, key= lambda x: results[x]['average'], reverse=ascending)
    for student in sorted_students:
        print(f"{student}: {results[student]['average']}")

def update_average(results: StudentsType, student: str) -> StudentsType:
    results[student]['average'] = sum(results[student]['grades']) / len(results[student]['grades'])
    return results

def main():
    # добавяне на тестови данни за по-лесно тестване на функциите
    results: StudentsType = {
        "Yuliyan": {
            "disciplines": ["KAOS", "Math", "IMMD"],
            "grades": [5, 3, 6],
            "average": 4.67
        },
        "Ivan": {
            "disciplines": ["KAOS", "Math", "IMMD"],
            "grades": [4, 6, 5],
            "average": 5
        },
        "Petar": {
            "disciplines": ["KAOS", "Math", "IMMD"],
            "grades": [6, 6, 6],
            "average": 6
        },
        "Georgi": {
            "disciplines": ["KAOS"],
            "grades": [4],
            "average": 4
        }
    }
    print("Type help to see available commands")
    while True:
        command = input("Enter command: ")
        if command == "average": # V
            print(f"Average: {average(results)}")

        elif command == "max": # V
            print(f"Max: {max_result(results)}")

        elif command == "min": # V
            print(f"Min: {min_result(results)}")

        elif command == "show grades": # V
            student = input("Enter student: ")
            if (student not in results):
                print("Student not found")
            else:
                print(results[student])

        elif command == "print": # V
            print_results(results)

        elif command == "show in discipline": # V
            discipline = input("Enter discipline: ")
            print_in_discipline(results, discipline)

        elif command == "add student": # V
            student = input("Enter student: ")
            if student in results:
                print("Student already exists")
            else:
                results = add_student(results, student)

        elif command == "remove student": # V
            student = input("Enter student: ")
            if student not in results:
                print("Student not found")
            else:
                results = remove_student(results, student)

        elif command == "add discipline":  # V
            student = input("Enter student: ")
            discipline = input("Enter discipline: ")
            grade = int(input("Enter grade: "))
            results = add_discipline(results, student, discipline, grade)

        elif command == "remove discipline":  # V
            student = input("Enter student: ")
            discipline = input("Enter discipline: ")
            results = remove_discipline(results, student, discipline)
        
        elif command == "edit grade": # V
            student = input("Enter student: ")
            if student not in results:
                print("Student not found")
                continue

            discipline = input("Enter discipline: ")
            if discipline not in results[student]['disciplines']:
                print("Discipline not found")
                continue

            grade = int(input("Enter grade: "))
            discipline_index = results[student]['disciplines'].index(discipline)
            results[student]['grades'][discipline_index] = grade
            update_average(results, student)

        elif command == "sort by name": # V
            print(sort_by_name(results))

        elif command == "sort by grades asc": # V
            sort_by_result(results)

        elif command == "sort by grades desc": # V
            sort_by_result(results, False)

        elif command == "help": # V
            print("Commands: average, max, min, print, add student, remove student, add discipline, remove discipline, sort by name, sort by grades asc, sort by grades desc, show in discipline, exit")

        elif command == "exit": # V
            break
        else:
            print("Invalid command")

main()