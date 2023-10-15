import math

def isPrime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
        
    return True

count = 0
i = 0

while count <= 10001:
        
    i += 1

    if isPrime(i) == True:
        count += 1
    
print(count)
print(i)

#INCOMPLETE