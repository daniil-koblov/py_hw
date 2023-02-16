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