numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]   # - исходный список

i = 0
primes = []
not_primes = []
#compared_item = my_list[index]

for i in numbers:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            primes.append(i)
    else:
        not_primes.append(i)
print("Здесь только простые числа из списка: ", primes)
print(f"Здесь все не простые числа : {not_primes} Вот эти вот все. Это они.")