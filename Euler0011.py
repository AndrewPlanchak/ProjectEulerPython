reader = open("Euler0011.txt", "r")

lines = []

for i in range(1, 20):

    line = reader.readline()
    lineStringArray = line.split(' ')
    lineIntArray = []

    for s in lineStringArray: lineIntArray.append(int(s))

    lines.append(lineIntArray)


def checkDiagProduct(i, j, lines): #will return the largest product of 4 adjacent numbers

    #NB: 1ST NUMBER IS VERTICAL SECOND IS HORIZONTAL

    largestProduct = 0

    if i >= 3: upCheck = True
    else: upCheck = False
    
    if j >= 3: leftCheck = True
    else: leftCheck = False

    if i <= 15: downCheck = True
    else: downCheck = False

    if j<= 15: rightCheck = True
    else: rightCheck = False

    #Bugfixing Tat
    #print("i: ", i, " j: ", j)
    #print("upCheck: ", upCheck)
    #print("downCheck: ", downCheck)
    #print("leftCheck: ", leftCheck)
    #print("rightCheck: ", rightCheck)
    #print()

    if upCheck == True: 
        if lines[i][j] * lines[i-1][j] * lines[i-2][j] * lines[i-3][j] >= largestProduct:
            largestProduct = lines[i][j] * lines[i-1][j] * lines[i-2][j] * lines[i-3][j]

    if downCheck == True: 
        if lines[i][j] * lines[i+1][j] * lines[i+2][j] * lines[i+3][j] >= largestProduct:
            largestProduct = lines[i][j] * lines[i-1][j] * lines[i-2][j] * lines[i-3][j]

    if leftCheck == True:
        if lines[i][j] * lines[i][j-1] * lines[i][j-2] * lines[i][j-3] >= largestProduct:
            largestProduct = lines[i][j] * lines[i][j-1] * lines[i][j-2] * lines[i][j-3]

    if rightCheck == True:
        if lines[i][j] * lines[i][j+1] * lines[i][j+2] * lines[i][j+3] >= largestProduct:
            largestProduct = lines[i][j] * lines[i][j+1] * lines[i][j+2] * lines[i][j+3]

    if upCheck == True and leftCheck == True:
        if lines[i][j] * lines[i-1][j-1] * lines[i-2][j-2] * lines[i-3][j-3] >= largestProduct:
            largestProduct = lines[i][j] * lines[i-1][j-1] * lines[i-2][j-2] * lines[i-3][j-3]

    if upCheck == True and rightCheck == True:
        if lines[i][j] * lines[i-1][j+1] * lines[i-2][j+2] * lines[i-3][j+3] >= largestProduct:
            largestProduct = lines[i][j] * lines[i-1][j+1] * lines[i-2][j+2] * lines[i-3][j+3]

    if downCheck == True and leftCheck == True:
        if lines[i][j] * lines[i+1][j-1] * lines[i+2][j-2] * lines[i+3][j-3] >= largestProduct:
            largestProduct = lines[i][j] * lines[i+1][j-1] * lines[i+2][j-2] * lines[i+3][j-3]

    if downCheck == True and rightCheck == True:
        if lines[i][j] * lines[i+1][j+1] * lines[i+2][j+2] * lines[i+3][j+3] >= largestProduct:
            largestProduct = lines[i][j] * lines[i+1][j+1] * lines[i+2][j+2] * lines[i+3][j+3]

    return largestProduct

largestProduct = 0

for i in range (0, 19):
    for j in range(0, 19):
        largestCurrent = checkDiagProduct(i, j, lines)

        if largestCurrent > largestProduct: largestProduct = largestCurrent

print (largestProduct)