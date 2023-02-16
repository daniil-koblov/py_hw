# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума).
from random import randint

strn = [randint(1, 30) for i in range(randint(5, 15))]
stri = []
print(strn)
min = int(input('Введите минимальное число: '))
max = int(input('Введите максимальное число: '))

for i in range(len(strn)):
    if strn[i] >= min and strn[i] <= max: stri.append(i)

print(*stri)

# ЭТАЛОННОЕ РЕШЕНИЕ:
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)