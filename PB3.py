import math 

def primeFactors(n):
    result = []

    while n % 2 == 0:
        n = n / 2
        result.append(2)

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            result.append(i)
            n = n / i

    if n > 2:
        result.append(n)

    return result

def largestPrimeFactor(n):
    result = 0

    while n % 2 == 0:
        n = n / 2
        result = 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            result = i
            n = n / i

    return result

n = 600851475143
print(primeFactors(n))
print(largestPrimeFactor(n))
