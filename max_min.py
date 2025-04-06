# maximum value in array.

def maxmin(arr):
    n = len(arr)
    for i in arr:
        # assuming that the first index will be either max or min.
        max_int = arr[0]
        min_int = arr[0]

        # looping from the 1st index.
        for j in range(i+1, n):
            if arr[j] > max_int:
                max_int = arr[j] # updating the maximum value.
            elif arr[j] < min_int:
                min_int = arr[j] # updating the minimum value.
    return max_int, min_int

array = [6,7,2,6,1,4,9,11,0]
print(maxmin(array))