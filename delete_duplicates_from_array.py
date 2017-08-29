arr = [1,1,2,3,4,6,7,7,7,8,9,15,18,20,20,22,25, 25, 27, 30,30]
# print len(arr)

def removeDuplicates(arr):
  slow = 0
  for i in range(len(arr)):
      print i
      if arr[i] != arr[i-1]:
        arr[slow] = arr[i]
        slow += 1
      # print slow
  return arr[: slow]

# arr = [1,2,3,4,7,10,4,5,5,7]

new = removeDuplicates(arr)
print new