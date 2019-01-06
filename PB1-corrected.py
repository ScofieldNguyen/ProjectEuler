target = 999

def sumDivisibleBy(n):
    p = target // n
    sum = n * (p * (p + 1)) / 2
    return sum

result = sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15)
print(result)
