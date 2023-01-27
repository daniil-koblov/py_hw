# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input('Введите трехзначное число: '))

if (num < 100 or num > 999):
    num = int(input('Введенное число не соответствует требованию. Повторите ввод снова: '))
    num1 = num // 100
    print(num1)
    num2 = (num // 10) % 10
    print(num2)
    num3 = (num % 100) % 10
    print(num3)
    print(f"Сумма цифр трехзначного числа равна {num1 + num2 + num3}.")
else:  
    num1 = num // 100
    print(num1)
    num2 = (num // 10) % 10
    print(num2)
    num3 = (num % 100) % 10
    print(num3)
    print(f"Сумма цифр трехзначного числа равна {num1 + num2 + num3}.")