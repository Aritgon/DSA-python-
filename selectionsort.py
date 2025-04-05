# selection sort.

array = [11,1,4,2,6,5,9,7]

def selectionSort(arr):
    # assuming the first index is the minimum.

    # len of array.
    n = len(arr)

    for i in range(n):
        min_index = i # assuming the first index will be the minimum value.
        for j in range(i+1, n): # looping through the rest of the array.
            if arr[j] < arr[min_index]:
                min_index = j # updating the newly found minimum value.
        # swapping.
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# print(selectionSort(array))

# descending order.

array = [11,1,4,2,6,5,9,7]

# print(array[-1])

def desc_selectionSort(arr):
    n = len(arr)

    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

print(desc_selectionSort(array))