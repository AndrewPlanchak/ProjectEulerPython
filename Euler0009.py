found = False

def isPythagoreanTriplet(a, b, c): #Ensures Numbers Provided are a triplet - returns bool

    aSquare = a*a
    bSquare = b*b
    cSquare = c*c

    if a > b or b > c:
        return False

    if(aSquare + bSquare == cSquare):
        return True
    else:
        return False

def sumTo1000(a, b, c): #If sum == 1000 return true else return false - makes code more readable
    if(a + b + c == 1000):
        return True
    else:
        return False

while found == False:
    for a in range(0, 500):
        for b in range(0, 500):
            for c in range(0, 500):
                if isPythagoreanTriplet(a, b, c) == True and sumTo1000(a, b, c) == True:
                    print(a*b*c)
                    break