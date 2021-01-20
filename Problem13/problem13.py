with open("input13.txt") as input:
    content = input.readlines()

total = 0
for line in content:
    number = int(line)
    total += number

total_str = str(total)
print(total_str[:10])
