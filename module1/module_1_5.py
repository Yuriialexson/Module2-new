#создаем кортеж:
immutable_var = 45, 'стул', 'Девять', 'Пи = 3,14', False, 282.1
print(immutable_var)
#пытаемся менять значения и вывести на экран:
immutable_var [3] = "Пи = 6,28"
print(immutable_var) # НО! Python против изменения математических констант, а кортеж – это неизменяемая упорядоченная коллекция

#Создание изменяемых структур данных:
mutable_list = [1, "желудь", 12.34, True]
print(mutable_list)
mutable_list.extend([False, 'лопата', 888])
print(mutable_list)
mutable_list[0]=2
print(mutable_list)
print(mutable_list[::-1])
