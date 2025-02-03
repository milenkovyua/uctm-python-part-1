'''
    Да се състави програма за преобразуване на време от секунди 
    в часове, минути и секунди.
'''

def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return hours, minutes, seconds

def main():
    seconds = int(input("Enter seconds: "))
    hours, minutes, seconds = convert_seconds_to_time(seconds)
    print(f"{hours}h {minutes}m {seconds}s")

main()