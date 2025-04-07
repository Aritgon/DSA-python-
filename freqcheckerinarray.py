# most frequenct element or a character in an array.
array = [2,2,2,4,5,1,7,6,8,5,5,4]

# freq = {} # initializes an empty dict.

# for num in array:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# print(freq)

def freq_checker(arr):
    freq_dict = {} # initializes an empty dict.

    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    # steps to return the most repeated character from the array.

    max_freq = max(freq_dict.values()) # this will count the values only.
    result = {char: count for char, count in freq_dict.items() if count == max_freq}
    return result

print(freq_checker(array))