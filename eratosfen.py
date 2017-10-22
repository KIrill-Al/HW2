#!/usr/bin/env python3
'''Поиск простых чисел до заданного числа алгоритмом Эратосфена'''
n = int(input('Введите число: '))
a = list(range(n+1))
a[1] = 0 # 1 - не простое число
prime_numbers = []
i = 2
while i <= n:
    if a[i] != 0:
        prime_numbers.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1
print (prime_numbers)
