# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# 5
# 1 2 3 4 5
# 6
# -> 5
import random

n = int(input('Введит кол-во чисел в строке: '))
a = []
x = int(input('Введите искомое число: '))

for i in range(n):
    random_num = random.randint(1, 10)
    if random_num != x: a.append(random_num)
    else: i -= 1
print(*a)
find_num = a[0]

for i in range(n-1):
    if abs(a[i]-x) < abs(find_num -x) : find_num= a[i]


print(find_num)