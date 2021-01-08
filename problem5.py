import numpy as np

numbers = []

for n in range(1, 21):
    numbers.append(n)

num = np.array(numbers)
lowest_common_multiple = np.lcm.reduce(num)

print(lowest_common_multiple)
