# missing integer.

def missing_num(arr):
    # take length of the array and using formula to find out sum of n numbers.
    n = len(arr) + 1
    expected_sum = (n * (n+1) // 2)

    # actual sum of array.
    actual_sum = sum(arr)

    missingNumber = expected_sum - actual_sum
    return missingNumber

array = [1,3,4,5,6]
print(missing_num(array))