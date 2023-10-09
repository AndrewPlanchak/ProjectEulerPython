a = 1
b = 2
c = 0
sum = 0

while c < 4000000:
    c = a + b
    if c % 2 == 0 and c  not > 400000:
        sum += c

    a = b
    b = c

print("The sum is: ", sum)