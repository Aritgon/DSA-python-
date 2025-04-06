# average of an array.
array = [80, 70,50, 40, 20]
# (total number of elements) / (len of array)
def avg(arr):
    sum = 0

    for i in arr:
        sum += i
    return sum // len(arr)

print(avg(array))