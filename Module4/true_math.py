# Функция работает при делении на ноль

from math import inf

def true_divide(first, second):
    if second == 0:
        return inf
    return first / second

