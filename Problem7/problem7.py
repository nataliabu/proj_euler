primes = []
num = 2
while len(primes) < 10002:
    is_prime = True
    for prime in primes:
        if num % prime == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    num += 1

print(primes[10000])


