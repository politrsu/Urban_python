numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:
    is_prime = True  # число простое
    for divisor in range(2, number):
        if number % divisor == 0: # если делитель без остатка
            is_prime = False  # число не простое
            break # прерывание цикла
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print("Primes:", primes)
print("Not Primes:", not_primes)