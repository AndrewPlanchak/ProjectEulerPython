import math

def PrimeSieve(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):
 
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 
    return prime

def SumArray(array):
    sum = 0

    for i in range(2, len(array)):
        if array[i]:
            sum += i

    return sum

print(SumArray(PrimeSieve(2000000)))