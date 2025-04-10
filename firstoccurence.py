# first occurence.
def first_occurence(arr, find_num):
    for i in arr:
        if i == find_num:
            return True
    return "not found"

find_number = 1
array = [4,5,6,3,1,5]
print(first_occurence(array, find_number))


