numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes_ = []
not_primes = []
is_prime = 0
for i in numbers_[1:]:
    for j in range(2,i):
        if i % j == 0:
            is_prime = False
            if is_prime == False:
                not_primes.append(i)
                break
        elif j == i-1:
            is_prime = True
            if is_prime == True:
                primes_.append(i)
                break
l = 2
if l % l == 0 and l % 1 == 0:
    primes_.insert(0, l)
else:
    not_primes(0, l)
print(primes_)
print(not_primes)


numbers_2 = [17, 22, 33, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes_2 = []
not_primes_2 = []
is_prime_2 = True
for i_2 in numbers_2:
    for j_2 in range(2,i_2):
        if i_2 % j_2 == 0:
            is_prime_2 = False
            if is_prime_2 == False:
                not_primes_2.append(i_2)
                break
        elif j_2 == i_2-1:
            is_prime_2 = True
            if is_prime_2 == True:
                primes_2.append(i_2)
                break
print(primes_2)
print(not_primes_2)


























