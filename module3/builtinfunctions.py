# # a = [False, False, True]
# # print(any(a)) # вернет True
#
# # a = [True, False, True]
# # print(any(a)) # вернет True
#
# a = [1, 0, 0]
# print(any(a))   # True
#
# a = [0, 0, 0]
# print(any(a))   # False
#
# a = [0, 0, 0]
# b = '0'
# print(any(b))   # True тк есть хот один элемен и неважно что ноль
#
# a = [0, 0, 0]
# b = ''
# print(any(b))   # False
#
# a = [0, 0, 0]
# b = ''
# print(all(b))   # False
#
# print("Интероспекция")
#
# a = [0, 0, 0]
# b = ''
# print(dir(b))
# print(type(b))
# print(isinstance(b, str))
# print(isinstance(b, int))
#
# print(type(b) == str)



a = [1, 1, 1]
b = ''
d = [1, 1, 1]
c = d
print(a == d)
print(id(a))
print(id(d))
print(a is d)
print(id(c))

print(help(a))
print(help(print))

def helper():
    """
    это функция-помощник
    """
    pass

print(help(helper))
print(helper.__doc__)