# duplicate value.

# this will return the duplicate values.
def duplicateValue(arr):

    # length.
    n = len(arr)
    for i in arr:
        for j in range(i+1, n):
            if arr[j] == arr[i]:
                return arr[j]
    return None

array = [1,2,3,3,4,5,6,7,7]

print(duplicateValue(array))

def duplicate(arr):

    n = len(arr)

    # Initializing a set.
    seen = set() 

    for i in arr:
        for j in range(i +1 , n):
            if arr[j] == arr[i]:
                return True 
            seen.add(i)
    return None

# print(duplicate(array))