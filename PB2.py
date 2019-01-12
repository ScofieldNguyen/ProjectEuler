a = 2
b = 8
sum = a + b

while a + b <= 4000000:
    new = a + 4 * b
    if new % 2 == 0:
        sum += new
    a = b
    b = new

print(sum)



