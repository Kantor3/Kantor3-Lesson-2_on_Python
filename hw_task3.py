"""
Задача 3
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
Пример:
- Для n = 3: {1: 2.0, 2: 2.25, 3: 2.37 }
"""
import my_Lib as My

print('Формирование последовательности n-первых значений приближения к экспоненте:')

while True:
    number = My.GetInputNumber(1, txt='\nВведите число членов приближения', end='-')
    if My.CheckExit(number):
        break
    sequence = []
    dic_exp = dict([(i+1, round((1 + 1/(i+1)) ** (i+1), 3)) for i in range(number)])
    print(f'N = {number} -> {dic_exp}')
