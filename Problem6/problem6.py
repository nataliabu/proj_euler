sum1 = 0
sum2 = 0

for n in range(1, 101):
    sum1 += (n ** 2)
    sum2 += n

total = (sum2**2) - sum1
print(total)
