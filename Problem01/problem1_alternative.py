num1 = 3
num2 = 5
num3 = num1 * num2
limit = 999

def sum_divisible_by(number):
    n = limit // number
    return number * (n * (n + 1)) / 2

result = sum_divisible_by(num1) + sum_divisible_by(num2) - sum_divisible_by(num3)
print(result)
