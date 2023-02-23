# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def add():
    with open('file.txt', 'a', encoding = 'utf-8') as data:
        for i in range(int(input('Введите кол-во строк: '))):
            data.write(input('Введите ФИО полностью и номер телефона: ').title() + '\n')
    
def output():
    path = 'file.txt'
    data = open('file.txt', 'r', encoding = 'utf-8')
    for line in data:
        print(line)
    data.close()

def search(info):
    path = 'file.txt'
    data = open('file.txt', 'r', encoding = 'utf-8')

    for line in data.readlines():
        if info in line: print(line)
    data.close()

def mod(info):
    with open('file.txt') as data:
        list_mod = []
        for line in data:
            if info in line.split(): list_mod.append(input(f'{line} --> ').title() + '\n')
            else: list_mod.append(line)
    with open('file.txt', 'w') as data:
        data.writelines(list_mod)
        data.close()

def delete(info):
    with open('file.txt') as data:
        list_del = []
        for line in data:
            if info in line: print(f'Данные по {line} удалены.')
            else: list_del.append(line)
    with open('file.txt', 'w') as data:
        data.writelines(list_del)
        data.close()

print('Это программа для работы со справочником.\n'
        'Введите 1 для добавления нового абонента.\n'
        'Введите 2 для выведения всех абонентов.\n'
        'Введите 3 для поиска абонента.\n'
        'Введите 4 для изменения данных в справочнике.\n'
        'Введите 5 для удаления данных в справочнике.\n'
        'Введите 6 для завершения работы программы.')
x = 0
while x != 6:
    x = int(input('Введите выбранный вариант: '))
    if x == 1: add()
    elif x == 2: output()
    elif x == 3: search(input('Введите искомые данные: '))  
    elif x == 4: mod(input('Введите данные для изменения: ').title())
    elif x == 5: delete(input('Введите данные для удаления: ').title())