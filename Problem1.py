sum = 0
S = 1000
n5 = int(S / 5) + 1
n3 = int(S / 3) + 1

for i in range(n5):
    num = 5 * i
    if num < S:
        print(num)
        sum += num

for i in range(n3):
    num = 3 * i
    if num < S and num % 5 != 0:
        print(num)
        sum += num


print(sum)
