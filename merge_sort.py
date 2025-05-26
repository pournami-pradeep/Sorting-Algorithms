"""
Divide and conquer
time complexity = nlogn
space complexity = O(n)
"""


def merge_sort(arr):
    if len(arr) == 1 or not arr:
        return arr
    
    mid = len(arr) // 2

    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])

    return merge(left,right)


def merge(left,right):
    l1 = 0
    r1 = 0
    new_arr = []
    while l1 < len(left) and r1 < len(right):
        if left[l1] <= right[r1]:
            new_arr.append(left[l1])
            l1 += 1
        else:
            new_arr.append(right[r1])
            r1 += 1

    while l1 < len(left):
        new_arr.append(left[l1])
        l1 += 1

    while r1 < len(right):
        new_arr.append(right[r1])
        r1 += 1
    return new_arr
        

arr = [100,2000,110]

arr = merge_sort(arr)
print(arr)