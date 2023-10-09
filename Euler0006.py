def sumOfSquares(i):
    sum = 0
    for j in range(0, i+1):
        sum += j*j
    
    return sum

def squareOfSum(i):
    sum = 0
    for j in range(0, i+1):
        sum += j
    
    return sum*sum

print(squareOfSum(100) - sumOfSquares(100))
    