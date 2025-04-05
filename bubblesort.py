# Bubble sort.

def bubbleSort(arr):
    # basic length.
    n = len(arr)

    for i in range(n): # process to be repeated n times.
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swapping elements.
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

array = [5,9,1,6,3]
print("sorted array: ", bubbleSort(array))
