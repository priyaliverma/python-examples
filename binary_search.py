"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    if len(input_array) == 0:
        # print ('input_array 0', input_array)
        return -1

    mid = len(input_array)/2
    #print ('input_array', input_array)
    # print ('mid index', mid)
    #print ('mid value', input_array[mid])
    #print ('value', value)
    if value == input_array[mid]:
        return mid
    elif value > input_array[-1]:
        return -1
    elif value > input_array[mid]:
        input_array = input_array[mid+1:]
        idx = binary_search(input_array, value)
        if idx == -1:
            return idx
        else:
            return mid + idx + 1
    elif value < input_array[mid]:
        input_array = input_array[:mid]
        # print ('input_array value less', input_array)
        return binary_search(input_array, value)
    else:
        return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)