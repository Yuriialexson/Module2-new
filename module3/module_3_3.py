def print_params(a=1, b='строка', c=True):
    print(a, b, c)

#1.Функция с параметрами по умолчанию:

print_params(a=2, b=1)  # вызов работает
print_params(a=2)   # вызов работает
#print_params(a=2, b=1, c=2323, d=23)   # ошибка, вывод после ошибки не работает
print_params()  # вызов работает
print_params(b=25)  # вызов работает
print_params(c=[1, 2, 3])  # вызов работает


#2.Распаковка параметров:

values_list = [2, 'STRING', False]
values_dict = {'a': 3, 'b': 'STROKA', 'c': None}

print_params(*values_list)
print_params(**values_dict)

#3.Распаковка + отдельные параметры:

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)