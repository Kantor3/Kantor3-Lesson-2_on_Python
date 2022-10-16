"""
# Некоторые записи как памятка
# 1. Работа с файлами:
with open('file_test', 'w') as data:
    data.write('srt-1\n')
    data.write('srt-2\n')

# Альтернативный подход (не самый лучший)
path = 'file_test'
data = open(path, 'a')
data.writelines('srt-33\n')
data.writelines('srt-7\n')

data = open(path, 'r')
for line in data:
    print(line, end='')
data.close()

# 2. Использование библиотеки собственных функций:
import my_Lib as My
input_list = My.GetInputTuple('a =', 'b =', 'c =', departed='-')
print(*input_list)

"""

import my_Lib as My

"""
Задача 11.
Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
Пример:
Для N = 5: 1, -3, 9, -27, 81
"""
print('Формируем последовательность ряда из N членов в логике, по образцу:')
print('Образец: Для N = 5: 1, -3, 9, -27, 81')
while True:
    number = My.GetInputNumber(txt='N =', end='-')
    if My.CheckExit(number):
        break
    print(f'N = {number}: {[(1 - 2 * (i % 2)) * 3 ** i for i in range(number)]}')
    print('\nЕще ряд ...')


"""
Задача 12
Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
Пример:
Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""
print('\nСоздаем словарь для последовательности 3n + 1 в формате {1: 4, ... n: 3n+1}:')
print('Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}')
while True:
    number = My.GetInputNumber(txt='N =', end='-')
    if My.CheckExit(number):
        break
    print(f'N = {number}: {dict([(i + 1, 3 * (i + 1) + 1) for i in range(number)])}')
    print('\nЕще ряд ...')


"""
Задача 13
Напишите программу, в которой пользователь будет задавать две строки, 
а программа - определять количество вхождений одной строки в другую.
Пример:
"hello or world", "or" -> 2
"""
print('\nИщем число вхождений одной строки в другую')
print('Пример: "hello or world", "or" -> 2')
while True:
    str_1 = input('Введите строку "ГДЕ ищем" -> ')
    str_2 = input('Введите строку "ЧТО ищем" -> ')
    len_str1 = len(str_1)
    number_of_count, pos_curr = 0, 0
    while pos_curr < len_str1-1:
        for el2 in str_2:
            pos_curr += 1
            if not el2 == str_1[pos_curr-1]:
                break
        else:
            number_of_count += 1

    print(f'"{str_1}", "{str_2}" -> {number_of_count}')
    print()

    if My.CheckExit():
        break

