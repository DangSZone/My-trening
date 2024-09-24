numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes_ = []
not_primes = []
is_prime = True
for i in numbers_[1:]:
    for j in range(numbers_[1], i):
        if i % j == 0:
            is_prime = False
            not_primes.append(i)
            break
        elif j == i - 1:
            is_prime = True
            if is_prime == True:
                primes_.append(i)
                break
        elif i > j:
            continue
primes_.insert(0,2)
print(primes_)
print(not_primes)



















