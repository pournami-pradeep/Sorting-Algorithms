"""
Worst case time complexity = O(n^2)
when the array is already sorted = O(n)
"""
arr = [30,4,1,2,5]

for i in range(len(arr)):
    swapped = False
    for j in range(1,len(arr)-i):
        if arr[j] < arr[j-1]:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            swapped = True
    if not swapped:
        break
print(arr)