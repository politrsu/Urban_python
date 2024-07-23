numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
x = 0
for number in range(2, len(numbers) + 1):
    for divisor in range(2, number):
        if number % divisor == 0:
            x = x + 1
    if x == 0:
        primes.append(number)
    else:
        x = 0
        not_primes.append(number)
print('primes:', primes)
print('not_primes:', not_primes)
