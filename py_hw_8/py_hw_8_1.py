# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def add():
    with open('file.txt', 'a') as data:
        for i in range(int(input('Введите кол-во строк: '))):
            data.write(input('Введите фамилия: ') + '\n'.upper())
    
def output():
    path = 'file.txt'
    data = open('file.txt', 'r')
    for line in data:
        print(line)
    data.close()

def search(info):
    path = 'file.txt'
    data = open('file.txt', 'r')

    for line in data.readlines():
        if info in line: print(line)
    data.close()

def mod_del(info):
    path = 'file.txt'
    data = open('file.txt', 'r')
    for line in data.readlines():
        if info in line:
            print(f'Вы хотите изменить\n'
                    f'{line}\n'
                    'в справочнике?')
            if input().lower() == 'да':
                y = input('Введите ФИО полностью и номер телефона: ')
                data.read().replace(line, y)
                data.close()
                break
            print(f'Вы хотите удалить\n'
                    f'{line}\n'
                    'из справочника?')
            if input().lower() == 'да':
                data.read().replace(line, '')
                data.close()
                break
    data.close()

print('Это программа для работы со справочником.\n'
        'Введите 1 для добавления нового абонента.\n'
        'Введите 2 для выведения всех абонентов.\n'
        'Введите 3 для поиска абонента.\n'
        'Введите 4 для изменения или удаления искомых данных из справочника.\n'
        'Введите 5 для завершения работы программы.')
x = 0
while x != 5:
    x = int(input('Введите выбранный вариант: '))
    if x == 1: add()
    elif x == 2: output()
    elif x == 3: search(input('Введите искомую информацию: '))  
    elif x == 4: mod_del(input('Введите искомую информацию: '))
    elif x == 5: break