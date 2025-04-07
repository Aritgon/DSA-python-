# first non repeating character in a given string. 
# For example, "aabbccdc" -> as a,b and c got repeated 2 times but d is only one time, so d will be non repeating character.

# a = "aabbccdc"

# freq = {}
# for char in a:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# print(freq)

# # loop through the string to find out the char with count = 1.
# for char in a:
#     if freq[char] == 1:
#         print(char)
#     print(None)

def nonrepeating(arr):

    # initialize an empty dict.
    freq_dict = {}
    for char in arr:
        if char in freq_dict:
            freq_dict[char] += 1 # update the value if it already exists.
        else:
            freq_dict[char] = 1 # assign the value if it doesn't exist.
    
    # loop through the string and for each character, check if count == 1.
    for char in arr:
        if freq_dict[char] == 1:
            return f"{char} : {freq_dict[char]}"
    return None # return none if you don't find anything.

a = "aabbccddddc"
print(nonrepeating(a))

