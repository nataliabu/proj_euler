import math

perimeter = 1000

#Euclid's formula: given an arbitrary pair of integers m and n  with m > n > 0, 
#the integers a = m^2-n^2, b = 2mn, c = m^2+n^2 form a Pythagorean triple

for m in range(1, math.ceil(math.sqrt(perimeter))):
    for n in range(1, m):
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
        if a + b + c == 1000:
            print(a, b, c)
            product = a * b * c
            print(product)
            break
