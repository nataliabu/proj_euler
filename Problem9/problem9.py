import math

perimeter = 1000

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
