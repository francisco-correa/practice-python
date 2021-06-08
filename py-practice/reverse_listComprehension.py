arr = [45, 67, 87, 23, 5,  32, 60]
print(arr)

rev  = arr[::-1]
print(rev)

new_list = []
for x in reversed(arr):
    new_list.append(x)
print(new_list)


# newlist = [expression for item in iterable if condition == True]

def reverse_arr(lista):
    return [x for x in reversed(lista)]
print(reverse_arr([2, 4, 8]))


# Create a variable new_list
# Using a loop, invert the "arr" list.
# Append the result loop into the new_list variable .
# With print() function output in the console the result that you have.