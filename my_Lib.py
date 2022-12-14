"""
Отдельные полезные функции, составляющие мою библиотеку
"""


# Организация выхода:
# Варианты:
# 1. sign = None
# 2. sign = True
# 1. sign = '[symbol_EXIT]' - передан символ для запроса выхода, например, "Y"
# или строка символов, каждый из которых ведет к "Выходу"
def CheckExit(sign='YyНн', txt_req='Продолжить? ("Y" - ДА) -> '):

    if isinstance(sign, str):
        out = not (f'-{input(txt_req)}' in map(lambda el: f'-{el}', sign))
    else:
        out = sign is None or isinstance(sign, bool) and sign

    if out:
        print("\nРабота с программой завершена, До встречи!");
        return True
    return False


# Организация ввода и возврат целого или вещественного числа (в т.ч. отрицательное)
# в заданном диапазоне или выход. C полным контролем корректности
def GetInputNumber(*rang, txt='Введите число', end=None):
    borders = '' if len(rang) == 0 else \
              f' ({rang[0]}, ... )' if len(rang) == 1 else \
              f' ({rang[0]}, ... {rang[1]}).'
    txt_input = f'{txt}{borders}'
    frm, to = (rang + (None, None))[:2]

    while True:
        key_forCancel = (f'введите "{end}" или ' if not (end is None) else '') + '[Enter]'
        numb = input(txt_input + f' (для отказа {key_forCancel}) -> ')

        if not (end is None) and numb == end or len(numb) == 0: return None
        try:
            numb = int(numb)
        except ValueError:
            try:
                numb = float(numb)
            except ValueError:
                print(f'Введенная строка "{numb}" не является числом. ', end='')
                txt_input = 'Повторите ввод.'
                continue

        if not (frm is None) and numb < frm or not (to is None) and numb > to:
            print(f'Введенное число {numb} должно быть в диапазоне ({rang[0]} ... {rang[1]}) -> ', end='')
            txt_input = 'Повторите ввод.'
            continue

        return numb


# Ввод нескольких целых чисел - Возврат введенных чисел в виде кортежа
def GetInputTuple(*inputParams, end=None):
    tup_iPar = tuple()
    for param in inputParams:
        inputParam = GetInputNumber(txt=param, end=end)
        if inputParam is None: return None
        tup_iPar += (inputParam,)
    return tup_iPar
