def numberToWord(n):
    words = ""
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    teens = [ "", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
    tens = [ "", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]
    
    if n == 1000: return len("onethousand")
    if n / 100 > 0:
        words += ones[int(n / 100)] + "hundred"
        n %= 100
        if n > 0: words += "and"
    
    if n > 10 and n < 20: words += teens[n % 10]
    else:
        if n / 10 > 0:
            words += tens[int(n / 10)]
            n %= 10
        if n > 0: words += ones[n]
        
    return len(words)

count = 0

for i in range(1, 1000):
    count += numberToWord(i)
    
print(count)
