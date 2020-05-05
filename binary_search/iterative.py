def binary_search(arr, el):
    low = 0
    heigh = len(arr)
    while low < heigh:
        mid = int((low + heigh) / 2)
        if arr[mid] == el: return True
        if arr[mid] > el: heigh = mid - 1
        else: low = mid + 1 
    return False

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(arr, 10))
print(binary_search(arr, 1))
print(binary_search(arr, -1))
print(binary_search(arr, 3232))




