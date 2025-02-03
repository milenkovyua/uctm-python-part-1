'''
1.19	Да се състави програма, която извежда първите 20 члена
от редицата на Фибоначи F(n), както и тяхната средна стойност,
където F(n) = F(n–1) + F(n–2),   F(1) = F(2) = 1.
'''

def main():
    fib = [1, 1]
    for i in range(2, 20):
        fib.append(fib[i - 1] + fib[i - 2])
    print(fib)
    print(sum(fib) / len(fib))

main()