# palindrome checker.

# with index slicing.

def pal(str):
    reverse = str[::-1]

    if reverse == str:
        return True
    return False

# print(pal("eye"))

# without slicing.

def palin(str):
    temp = ""

    # reversing the string and 
    for char in str.lower():
        temp = char + temp

    if temp == str:
        return True
    return False

print(palin("eye"))