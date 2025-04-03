# Prime Number checker.

def is_prime(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n):
            if n % i == 0:
                return f"{n} is not a prime number."
        return f"{n} is a prime number."
    
choice = int(input("Enter a number to check: "))
print(is_prime(choice))
