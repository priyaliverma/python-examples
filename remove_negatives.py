arr = [12, 1,0, -1, -2, 7, 8, 10, -3, 5,15, -20,-3, -20]
print arr

def remove_negatives(arr):
  slow = 0
  for i in range(len(arr)):
    if arr[i] >= 0:      #The CONDITION to KEEP elements
      arr[slow] = arr[i]
      slow += 1

  return arr[: slow]


new_arr = remove_negatives(arr)
print new_arr

# PRACTISE: Remove all numbers above 10

given_arr = [1,2,3,4,7,9,10,20,30]
def remove_numbers_above_ten(arr):
    slow = 0
    for i in range (len(arr)):
        if arr[i] <= 10:        #The CONDITION to KEEP elements
            arr[slow] = arr[i]
            slow += 1
    return arr[: slow]

new_array = remove_numbers_above_ten(given_arr)
print new_array