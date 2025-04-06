# reversing an array.

# Using index slicing.
def reverse_arr(arr):
    reverse = arr[::-1]
    return reverse

array = [1,2,3,4]
# print(reverse_arr(array))

# manual method.
array = [4,3,2,1]
def reverse_array(arr): 
    # empty list.
    empty_list = []
    for i in range(len(array) - 1, -1, -1):
        empty_list.append(array[i])

    return empty_list

# print(reverse_array(array))

# sliding window / Two pointer way.
arr = [1,2,3,4,5]
start = 0
end = len(arr) - 1 # backward.

while start < end:
    arr[start], arr[end] = arr[end], arr[start]

    start += 1 # iterate forward.
    end -= 1 # iterate backward.

# print("reversed array: ", arr)