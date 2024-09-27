# Максимум в списке
# Подсчет четных чисел в списке
# Уникальный список
#
# def find_max(list_):
#    max_ = list_[0]
#    for i in list_:
#        if i > max_:
#            max_ = i
#    return max_
#
# print(find_max([1, 54, 12, -1, 2, 4]))
#
# def count_even(list_):
#     counter = 0
#     for i in list_:
#         if i == 0:
#             continue
#         if i % 2 == 0:
#             counter += 1
#     return counter
#
# print(count_even([2, 2, 3, 4, 2, 1, 22, 104]))


unique = {1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8} #замена скобок {} []

# def convert1(unique):
#     return tuple(i for i in unique)
#
# def convert2(unique):
#     return (*unique, )
#
# # Driver function
#
# print(convert1(unique))
# print(convert2(unique))
print(unique)