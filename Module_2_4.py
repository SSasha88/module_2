numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes содержащий только простые числа
# not_primes, содержащий все не простые
for i in numbers:
    for j in numbers:
          is_prime = i % j
          if is_prime == 0:
              print(f'{i} % {j} = {is_prime}')




