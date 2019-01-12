def palindromicNumbers6Digits():
    result = []
    for i in range(1, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                result.append(i * 100000 + j * 10000 + k * 1000 + k * 100 + j * 10 + i)

    return result

def isProductOf3DigitsNumber(n):
    for i in range(999, 315, -1):
        if n % i == 0:
            j = n / i
            if j >= 100 and j <= 999:
                print(j)
                return True

    return False


numberList = palindromicNumbers6Digits()

result = []
for number in numberList:
    if isProductOf3DigitsNumber(number):
        print(number)


