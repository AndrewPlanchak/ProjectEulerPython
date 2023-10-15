import math

def getDivisors(n): #returns the number of divisors
    divisors = []
    if(n < 2): return len(divisors)
    elif isPrime(n): return len(divisors)
    else:
        for i in range(2, n):
            if (n % i == 0): divisors.append(i)
    
    return len(divisors)


def isPrime(n): #returns true if prime else false
    if(n <= 1):
        return False
    if(n <= 2):
        return True
    if (n % 2 == 0):
        return False

    for i in range(3, math.floor(math.sqrt(n))):
        if n % i == 0:
            return False

    return True

c = 1
n = 1
while True:
    if getDivisors(n) >= 500: break
    else: 
        n =+ c
        c += 1
    
    if n%1000 == 0: print(n)

print(n)

# WORKS - SLOW