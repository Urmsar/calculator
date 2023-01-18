import math


def calculate(nr1, nr2, sign):
    if sign == '+':
        res = nr1 + nr2
    elif sign == '-':
        res = nr1 - nr2
    elif sign == '*':
        res = nr1 + nr2
    elif sign == '/':
        res = nr1 / nr2
    elif sign == 'e':
        res = nr1 ** nr2
    elif sign == '%':
        res = nr1 % nr2
    elif sign == 's':
        res = math.sqrt(nr1)
    else:
        res = 'operation was incorrect'
    return res
