fibonacci = [1, 2]
total = 2

while (fibonacci[-1]+fibonacci[-2]) < 4000000:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if fibonacci[-1] % 2 == 0:
        total += fibonacci[-1]

print(total)
