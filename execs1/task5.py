'''
  Да се състави програма за преобразуване на сантиметри 
  в метри и сантиметри. Да се добави въвеждане на стойности
  от командния ред. Да се добави въвеждане на няколко сантиметри,
  напр. 122,230,50.
'''

def converter(cm):
    m = cm // 100
    cm = cm % 100
    return m, cm

def main():
    input_cm = input("Enter cm (comma-separated for multiple values): ")
    cm_values = input_cm.split(',')

    for cm in cm_values:
        try:
            cm = int(cm)
            m, cm = converter(cm)
            print(f"{m}m {cm}cm")
        except ValueError:
            print(f"Invalid input: {cm}")

main()