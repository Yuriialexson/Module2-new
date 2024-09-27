# def is_member(string, list_to_search):
#     for string in list_to_search:
#         if string is list_to_search or string == list_to_search:
#             return True
#     return False

# print(is_member('Urban', ['ban', 'BaNaN', 'urBAN']))

# list_to_search = ['ban', 'BaNaN', 'urBAN', 'Urban']
# for i in list_to_search:
#     list_to_search.lower()
#
# print(list_to_search.lower())

number = 40203


multiplication_list = []
str_number = str(number)
first = str_number[0:1]
tail = str_number[1:]
print(first)
print(tail)
multiplication_list.append(first)
print(multiplication_list)

new_number1 = tail
print(new_number1)
first1 = new_number1
str_number1 = str(new_number1)
first1 = new_number1[0:1]
tail1 = new_number1[1:]
print(first1)
print(tail1)
multiplication_list.append(first1)
print(multiplication_list)

new_number2 = tail1
print(new_number2)
first1 = new_number2
str_number2 = str(new_number2)
first2 = new_number2[0:1]
tail2 = new_number2[1:]
print(first2)
print(tail2)
multiplication_list.append(first2)
print(multiplication_list)

new_number3 = tail2
print(new_number3)
first2 = new_number3
str_number3 = str(new_number3)
first3 = new_number3[0:1]
tail3 = new_number3[1:]
print(first3)
print(tail3)
multiplication_list.append(first3)
print(multiplication_list)

new_number4 = tail3
print(new_number4)
first4 = new_number4
str_number4 = str(new_number4)
first4 = new_number4[0:1]
tail4 = new_number4[1:]
print(first4)
print(tail4)
multiplication_list.append(first4)
print(multiplication_list)

multiplication_list = [int(i) for i in multiplication_list]
print(multiplication_list)
# import math
# math.prod(multiplication_list)
import functools
print (functools.reduce(lambda a, b : a * b, multiplication_list))









# tail = number





# tail = str_number
# first = str_number[0:1]
# tail = str_number[1:]
# print(first)
# print(tail)
# multiplication_list.append(first)


# def form_multiplication_list():
#     multiplication_list.append(first)
#
#
# # first = str_number[1:]
# print(first)
# print(tail)