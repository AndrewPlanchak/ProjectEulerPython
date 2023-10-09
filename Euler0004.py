def checkIfPalendrome(input):
    strInp = str(input)
    lenInp = len(strInp)
    
    for i in range(len(strInp)):
        if not strInp[i] == strInp[lenInp - i - 1]:
            return False
        
    return True

largest = 0

for i in range(111, 999):
    for j in range(111, 999):
        if checkIfPalendrome(i * j) == True and (i*j) > largest:
            largest = i * j

print("The largest sum is: ", largest)