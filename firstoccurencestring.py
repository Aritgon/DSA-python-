# first occurence check in string.
def first_occur(arr):
    n = len(arr)

    # storing datas in the dictionary.
    freq_dict= {}
    for char in arr:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    # again looping through the string.
    for char in arr:
        if freq_dict[char] > 1:
            return f"{char} : {freq_dict[char]}"
    return None

array = "abcsedbd"
print(first_occur(array))