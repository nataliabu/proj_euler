num = 600851475143
factor = 2

while factor * factor <= num:
    while num % factor == 0:
        num = num / factor
        #in case num is a perfect square:
        if num / factor == 1:
            print(num)
    factor += 1
print(num)
