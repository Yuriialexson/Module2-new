#"Всё не так уж просто"

print()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]   # - исходный список
print(f"Вот список: {numbers}")
print()

#составиить список primes содержащий только простые числа (имеют два различных натуральных делителя)

primes = []
not_primes = []

# for i in numbers:
#     if i != 1:
#         if i // i == 1 and i // 1 == i:
#             primes.append(i)
#     else:
#         not_primes.append(i)
#         primes = primes.append(i)
# not_primes = not_primes.append(i)

for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print("Здесь только простые числа из списка: ", primes)
print(f"Здесь все не простые числа : {not_primes} Вот эти вот все. Это они.")

