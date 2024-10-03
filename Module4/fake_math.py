# Функция выдает ошибку при делении на ноль
def fake_divide(first, second):
    if second == 0:
        print("Ошибка! Деление на ноль")
    else:
        return first / second


