reader = open("Euler0013.txt", "r")

sum = 0
for i in range(0, 100): 
   line = int(reader.readline())
   sum += line

print(str(sum)[:10])
