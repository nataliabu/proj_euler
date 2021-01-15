import math

primes = [2, 3]

total = 5

def is_prime(number):
    square_root = math.floor(math.sqrt(number))
    for prime in primes:
        # Any number n can have only one primefactor greater than sqrt(n)
        if prime <= square_root:
            if number % prime == 0:
                return False
        else: 
            break
    return True

#All primes greater than 3 can be written in the form 6q+1 or 6q-1
for n in range(6, 2000000, 6):
    one_less = n - 1
    one_more = n + 1
    if is_prime(one_less):
        primes.append(one_less)
        total += one_less
    if is_prime(one_more):
        primes.append(one_more)
        total += one_more

print(total)
