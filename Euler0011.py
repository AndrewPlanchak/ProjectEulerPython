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

    leftCheck = (j >= 3)
    downCheck = (i <= 15)
    rightCheck = (j <= 15)

    l = 0
    d = 0
    dl = 0
    dr = 0

    if(leftCheck): l = lines[i][j] * lines[i][j-1] * lines[i][j-2] * lines[i][j-3]

    if(downCheck): d = lines[i][j] * lines[i+1][j] * lines[i+2][j] * lines[i+3][j]
    
    if(downCheck and leftCheck): dl = lines[i][j] * lines[i+1][j-1] * lines[i+2][j-2] * lines[i+3][j-3]

    if(downCheck and rightCheck): dr = lines[i][j] * lines[i+1][j+1] * lines[i+2][j+2] * lines[i+3][j+3]

    return max(l, d, dl, dr)

largestProduct = 0

for i in range (0, 19):
    for j in range(0, 19):
        largestProduct = max(largestProduct, checkDiagProduct(i, j, lines))

print (largestProduct)