"""
Задача 5
Реализуйте алгоритм перемешивания списка.
random.shuffle(lst)  # Встроенная функция перемешивания
"""

import random
import my_Lib as My
from functools import reduce

print('Перемешивание заданного списка:')
l_size = My.GetInputNumber(1, txt='\nЗадайте размер списка', end='-')
if My.CheckExit(l_size):
    exit()

lst = list(set(random.randint(0, l_size) for _ in range(l_size + 1)))  # делаем элементы списка уникальными

while True:
    print(f'\nИсходный список     -> {lst}')
    lst = reduce(lambda _, __: _ + [lst.pop(random.randint(0, len(lst) - 1))], range(len(lst)), [])
    print(f'Перемешанный список -> {lst}')

    if My.CheckExit():
        break
