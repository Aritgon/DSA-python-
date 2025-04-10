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
print("sorted array(ascending order): ", bubbleSort(array))


# bubble sort in descending order.
def desc_bubblesort(arr):

    n = len(arr)

    for i in range(n): # process to run n times.
        for j in range(0, n - i - 1): # avoid already sorted items.
            if arr[j] < arr[j+1]:
                # swapping elements.
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

array = [5,6,9,1,3]
print("Sorted array(descending order): ", desc_bubblesort(array))