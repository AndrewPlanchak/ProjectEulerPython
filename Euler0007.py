import math

def isPrime(i):
    if i == 1:
        return False
    if i == 2:
        return True
    if i % 2 == 0:
        return False
    
    j = math.floor(math.sqrt(i))

    for i in range(3, j):
        if i % j == 0:
            return False
        
    return True

count = 0
i = 0

while count <= 10001:
        
    i += 1

    if isPrime(i) == True:
        count += 1
    
print(i)

#INCOMPLETE