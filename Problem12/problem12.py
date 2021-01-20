import math

not_found = True
count = 500

def triangular(n):
    total = (n * (n + 1)) / 2
    return int(total)

def num_factors(num):
    # every number is divisible by 1
    total_factors = 1
    square_rt = math.floor(math.sqrt(num))    
    # range starts at 2 because we already counted 1 as a factor
    for possible_factor in range(2, square_rt + 1):
         if num % possible_factor == 0:
            total_factors += 1
    # we duplicate the result because all quotients are also divisors 
    total_factors *= 2
    return total_factors

while not_found:
    count += 1
    if num_factors(triangular(count)) > 500:
        print(triangular(count))
        not_found = False
