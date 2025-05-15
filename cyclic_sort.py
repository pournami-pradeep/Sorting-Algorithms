""" 
When given numbers from 1 to n use cyclic sort
after sorting this types of array index will be equal to value - 1
worst case time complexity is (2n-1)
"""
arr = [3,2,1,4,5]

i = 0
while i < len(arr):
    if arr[i] == i + 1:
        i += 1
        continue
    temp = arr[arr[i]-1]
    arr[arr[i]-1] = arr[i]
    arr[i] = temp

print(arr)