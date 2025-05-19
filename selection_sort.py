"""
Select largest element an put it in right place
worst case and best case : O(n*n)
"""

arr = [40,2,1,30,5,6]

def find_max(start,end,arr):
    max_index = start
    for i in range(start,end):
        if arr[i] > arr[max_index]:
            max_index = i
    return max_index

for i in range(len(arr)):
    max_el = find_max(0,len(arr)-i,arr)
    temp = arr[len(arr)-i-1]
    arr[len(arr)-i-1] = arr[max_el]
    arr[max_el] = temp
    
print(arr)