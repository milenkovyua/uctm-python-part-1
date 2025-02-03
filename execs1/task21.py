'''
Да се изчисли коефициентът на дифузия Dg на газове по формулата
Dg = (0,00155 * t^(3/2)) / (P * (Va^(1/3) + Vb^(1/3))^(1/2) ) * ( sqrt( (1/Ma) + (1/Mb) ) )
където Ma и Mb са молни маси, Va и Vb са обеми, p е налягане, t е температура. 
Коефициентът Dg да се изчисли за различни стойности на параметрите t и p,
като t се изменя от зададена начална стойност tn до крайна стойност
tk със стъпка на нарастване dt, а p се изменя от начална стойност pn
до крайна стойност pk със стъпка на нарастване dp.
'''

import math

def main():
    tn = int(input("Enter tn: "))
    tk = int(input("Enter tk: "))
    dt = int(input("Enter dt: "))
    pn = int(input("Enter pn: "))
    pk = int(input("Enter pk: "))
    dp = int(input("Enter dp: "))
    Ma = float(input("Enter Ma: "))
    Mb = float(input("Enter Mb: "))
    Va = float(input("Enter Va: "))
    Vb = float(input("Enter Vb: "))
    print ("t p Dg")
    for t in range(tn, tk + dt, dt):
        for p in range(pn, pk + dp, dp):
            Dg = (0.00155 * (t ** (3 / 2))) / (p * ((Va ** (1 / 3)) + (Vb ** (1 / 3))) ** (1 / 2)) * (math.sqrt((1 / Ma) + (1 / Mb)))
            print(t, p, Dg)

main()
