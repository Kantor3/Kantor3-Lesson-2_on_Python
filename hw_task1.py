"""
Задача 1
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
"""
import my_Lib as My


def Get_digit_symbol(symbol):
    try:
        return int(symbol)
    except ValueError:
        return 0


print('Расчет суммы цифр вещественного числа:')

while True:
    number = My.GetInputNumber(txt='\nВведите любое вещественное число', end='-')
    if My.CheckExit(number):
        break
    summa_digs = sum(map(Get_digit_symbol, str(number)))
    print(f'- {number} -> {summa_digs}')
