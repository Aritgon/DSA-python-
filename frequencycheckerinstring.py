# check how many characters in a string reappears.

def freq_checker(str):
    freq = {} # initializing an empty dict.

    for char in str:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    # return freq

    # step 2. which returns the highest counted char from the string.
    max_char = max(freq.values()) # this will take the maximum value from the dict.(it returns the biggest item)

    # result = {}
    # for char, count in freq.items():
    #      if count == max_char:
    #           result[char] = count
    # return result

    # using list comprehension. 
    result = {char: count for char, count in freq.item() if count == max_char}
    return result

string = "hello world".replace(" ", "").lower()
print(freq_checker(string))