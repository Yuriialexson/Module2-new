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

def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number)
    first = int(str_number[0])
    return first * get_multiplied_digits(int(str_number[1:]))

print(get_multiplied_digits(number))


# вариант через цикл
result = 1
for i in str(number):
    if i != "0":
        result *= int(i)
print(result)
