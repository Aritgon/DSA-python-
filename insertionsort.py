# insertion sort.

array = [5,2,9,1]

def insertion(arr):

    n = len(arr) # 4.

    for i in range(1,n): # 1,2,3, 2 is chosen index for key.
        key = arr[i] # first index is getting stored.
        j = i - 1 # 2-1, 1(0th index) is the value for j.

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] # moving the value.
            j -= 1

        arr[j+1] = key
    return arr

print(insertion(array))

array = [5,2,9,1]
def desc_insertion(arr):
    n = len(arr) 

    for i in range(1,n): 
        key = arr[i] # assigning the second index value.
        j = i - 1 # value is 1st index.

        while j>= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr
print(desc_insertion(array))


