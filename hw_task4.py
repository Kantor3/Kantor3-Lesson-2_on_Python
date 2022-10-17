"""
Задача 4
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.
"""

import random
import my_Lib as My
from functools import reduce


def Create_FilePos(max_count):
    pos_rnd = set(el for el in list(random.randint(1, max_count + 1) for _ in range(max_count + 1)))
    fil = open('file.txt', 'w')
    fil.close()
    with open('file.txt', 'a') as fil:
        fil.writelines(f'{el}\n' for el in pos_rnd)
    return


""" 
==============================================================================================
Основное тело программы
==============================================================================================
"""
print('Расчет произведения 2N элементов из списка [-N, N] на заданных в файле file.txt позициях:')

while True:
    number = My.GetInputNumber(1, txt='\nВведите количество элементов для расчета из интервала [-N, N]', end='-')
    if My.CheckExit(number):
        break
    list_numbs = [i for i in range(-number, 0)] + [i for i in range(1, number + 1)]
    Create_FilePos(2 * number - 1)

    with open('file.txt', 'r') as f:
        list_pos = list([int(el) for el in f])

    multi = reduce(lambda acc, curr: acc * list_numbs[curr - 1], list_pos, 1)

    print(f'\nСписок элементов -> {list_numbs}')
    print(f'Позиции элементов для перемножения (из файла "file.txt") -> {list_pos}')
    print(f'Выбранные элементы для перемножения -> {list(map(lambda i: list_numbs[i - 1], list_pos))}')
    print(f'Результат перемножения выбранных элементов -> {multi}')
