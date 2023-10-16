import math

n = str(2 ** 1000)

print(n)

sum = 0

for i in range(0, len(n)):
    sum += int(n[i])
   
print(sum)