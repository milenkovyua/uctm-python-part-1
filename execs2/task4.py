'''
Да се създаде списък, съдържащ информация за резултатите от проведен тест
на група студенти по конкретна дисциплина. Резултатите варират в
интервала от 0 до 100 точки. Да се дефинират функции за:
    * изчисляване средния успех на студентите
    * намиране на най-високия резултат
    * намиране на най-ниския резултат
    * отпечатване резултатите на всички студенти
    * отпечатване резултатите под форма на вертикална хистограма
'''

def average(results):
    return sum(results) / len(results)

def max_result(results):
    return max(results)

def min_result(results):
    return min(results)

def print_results(results):
    for i, result in enumerate(results):
        print(f"Student {i + 1}: {result}")

def print_histogram(results):
    histogram = [0] * 10 # create a list with 10 zeros
    for result in results:
        index = min(result // 10, 9)
        histogram[index] += 1
    for i, count in enumerate(histogram):
        if i == 9:
            print(f"{i * 10:02} - 100: {'*' * count}")
        else:
            print(f"{i * 10:02} - {i * 10 + 9:02}: {'*' * count}")

# test data: 40,85,70,60,90,50,65,55,75,80
def main():
    results = input("Enter results (comma separated values) of students: ").split(',')
    results = [int(item) for item in results] # converting to int
    print(f"Average: {average(results)}")
    print(f"Max: {max_result(results)}")
    print(f"Min: {min_result(results)}")
    print_results(results)
    print_histogram(results)

main()
