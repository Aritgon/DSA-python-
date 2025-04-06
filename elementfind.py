# element finding using linear search.

def linear(arr, target):
    for i in arr:
        if arr[i] == target:
            return f"index: ", i
    return False

target = 1
array = [5,6,7,8,912,34,1,67,3,8,4]
print(linear(array,target))