# sum of all elements in an array.

def sumOfElements(arr):
    temp = 0 # setting up a counter variable.
    for i in arr:
        temp += i
    return temp

array = [6,9,1,2]
print(sumOfElements(array))
