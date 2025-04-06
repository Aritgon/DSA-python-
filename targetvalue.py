# find two values in an array which sums up to a target value.

def target(arr, target_val):
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target_val:
                return (arr[i], arr[j])
    return None

array = [3,4,6,5,1,7,10]
target_value = 7
print(target(array, target_value))