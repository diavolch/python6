# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = 'текст с абв, который удаляет и у абвгд абв'
lst2 = [i for i in text.split() if 'абв' not in i]
print(' '.join(lst2))


# 2. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# day = 6
# day_off = lambda x: 'yes' if (x == 6 or x == 7) else 'not'
# print(day_off(day))


# 3. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# from functools import reduce
# num = list(input('Введите число: ').replace('.',''))
# num = list(map(lambda x: int(x), num))
# sum = reduce((lambda x, y: x + y), num)
# print(sum)


# 4. Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.
# n = int(input('Введите число: '))
# dct = {i: round((1+1/i)**i, 2) for i in range(1,n+1)}
# print(sum(dct.values()))

# 5. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# n = int(input('Введите число: '))
# lst = [i for i in range(-n,n+1)]
# with open('file.txt', 'r') as file:
#     lst2 = file.read().split()
# lst2 = list(map(lambda x: int(x), lst2))
# mult = 1
# for i in range(len(lst2)):
#     mult *= lst[lst2[i]]
# print(mult)