reader = open("Euler0008.txt", "r")
s = reader.read()

largest = 0

for i in range(1, s.__len__() -14):

    sum = 1
    for j in range(0, 13):
       sum *= int(s[i + j])
    
    if sum > largest:
        largest = sum

print(largest)