import math 

def isPrime(input):
    if(input <= 1):
        return False
    if(input <= 2):
        return True
    if (input % 2 == 0):
        return False

    square_root_input = math.floor(math.sqrt(input))

    for i in range(3, square_root_input):
        if input % i == 0:
            return False

    return True


number = 600851475143
factor = 2

while number > 1:
    if number % factor == 0:
        number /= factor
    else:
        factor += 1
        if factor * factor > number:
            print(number)
            break