# number // 3 is "fizz".
# number // 5 is "buzz".
# number // 3 & 5 is "fizzbuzz".

def fizzbuzz(n):
    if n <= 0:
        return 0
    elif n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return n

# take range.
choice = int(input("Enter a range to check fizz and buzzes: "))
for i in range(0, choice+1):
    print(fizzbuzz(i))

