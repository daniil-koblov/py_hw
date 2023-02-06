# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12

scr_dict = dict.fromkeys(['a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'], 1)
scr_dict.update(dict.fromkeys(['d', 'g'], 2))
scr_dict.update(dict.fromkeys(['b', 'c', 'm', 'p'], 3))
scr_dict.update(dict.fromkeys(['f', 'h', 'v', 'w', 'y'], 4))
scr_dict.update(dict.fromkeys(['k'], 5))
scr_dict.update(dict.fromkeys(['j', 'x'], 8))
scr_dict.update(dict.fromkeys(['q', 'z'], 10))
scr_dict.update(dict.fromkeys(['а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'], 1))
scr_dict.update(dict.fromkeys(['д', 'к', 'л', 'м', 'п', 'у'], 2))
scr_dict.update(dict.fromkeys(['б', 'г', 'ё', 'ь', 'я'], 3))
scr_dict.update(dict.fromkeys(['й', 'ы'], 4))
scr_dict.update(dict.fromkeys(['ж', 'з', 'х', 'ц', 'ч'], 5))
scr_dict.update(dict.fromkeys(['ш', 'э', 'ю'], 8))
scr_dict.update(dict.fromkeys(['ф', 'щ', 'ъ'], 10))

word = input('Введите слово: ')

sum = 0

for i in range(len(word)):
    sum += scr_dict[word[i]]

print(sum)