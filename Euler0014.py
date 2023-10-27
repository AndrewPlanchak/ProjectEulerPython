largest = 0

for i in range(1, 1000000):
    count = 0
    n = i

    while not n == 1:
        if(n % 2 == 0): n = n / 2
        else: n = 3 * n + 1
        count += 1
    
    largest = max(count, largest)

