#"Нули ничто, отрицание недопустимо!"

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
new_list = []
#compared_item = my_list[index]

while index < len(my_list):
    compared_item = my_list[index]
    index = index + 1
    #index += 1
    if compared_item > 0:
        new_list.append(compared_item)
    elif compared_item == 0:
        continue
    else:
        break
print(new_list)



# как оптимальнее для памяти?:
# 1) останавливать цикл при столкновении с отрицательным числом или через elif есть отрицательное число => break
# 2) и с нулем: пропускать его через continue при столкновении с нулем или через >=

# while len(my_list) == index:
#     index = 0
#     for i in my_list:
#         print(my_list[index])






# index = index + 1
# compared_item = my_list([index])
# print(compared_item)
#
# index = 0
# print(my_list[index])
# print(my_list[index + 1])

# while len(my_list) == index:
#     compared_item = my_list[index]
#     if compared_item > 0:
#         print(compared_item)
#     if compared_item > 0:
#         compared_item = my_list[index + 1]
#         index = index + 1

# while  <= len(my_list):
#   compared_item = my_list[index+1]

# compared_item = my_list[index]


