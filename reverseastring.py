# reverse a string with both slicing and normal way.

# slicing.
def rev(str):
    reverse_str = str[::-1] # starting, ending and step. (string slicing methods)

    return reverse_str

print(rev("hello"))


# normal way.
def reverse(str):
    # creating a temp variable. 
    temp = "" # in str form.

    for char in str.lower():
        temp = char + temp
    return temp

print(reverse("arit gon"))
        