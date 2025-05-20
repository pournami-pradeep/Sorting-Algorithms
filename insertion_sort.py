# O(n*n) : worst case 


arr = [-1,0,2,100,10]

i = 0
j = i+1
while i <= len(arr)-2:
    j = i + 1
    while j > 0:
        if arr[j] < arr[j-1]:
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j -= 1
            continue
        break
    i += 1
print(arr)