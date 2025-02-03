'''
Да се състави програма, която определя дали въведена от
командния ред година е високосна. Да се добави възможност
за въвеждане на няколко стойности, напр. 1986,2024,2016
'''

def main():
    input_years = input("Enter years (comma-separated for multiple values): ")
    years = input_years.split(',')

    for year in years:
        try:
            year = int(year)
            if year % 4 == 0:
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
        except ValueError:
            print(f"Invalid input: {year}")

main()