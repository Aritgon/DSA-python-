# factorial of a number.
def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fact = n * factorial(n - 1)
        return fact
    
choice = int(input("Enter a number to check: "))
print(factorial(choice))
