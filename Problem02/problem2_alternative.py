total = 0
even = 0
odd1 = 1

while even < 4000000:
    total += even
    odd2 = even + odd1
    even = odd1 + odd2
    odd1 = odd2 + even

print(total)
