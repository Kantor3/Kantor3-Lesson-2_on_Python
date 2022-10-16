"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""
import my_Lib as My

print('Формирование ряда произведений последовательности натуральных чисел заданного размера:')
while True:
    number = My.GetInputNumber(1, txt='\nВведите натуральное число', end='-')
    if My.CheckExit(number):
        break
    rang = range(number)
    sequence = []
    set(map(lambda i, j: sequence.append(1 if i == 0 else sequence[i - 1] * (j + 1)), rang, rang))
    print(f'N = {number} -> {sequence}')
