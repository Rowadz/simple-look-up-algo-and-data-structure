def binary_search(arr, el, low, heigh):
    if low >= heigh: return False
    mid = int((low + heigh) / 2)
    if arr[mid] == el: return True
    if arr[mid] > el: return binary_search(arr, el, low, mid - 1)
    else: return binary_search(arr, el, mid + 1, heigh)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(arr, 10, 0, len(arr)))
print(binary_search(arr, 1, 0, len(arr)))
print(binary_search(arr, -1, 0, len(arr)))
print(binary_search(arr, 3232, 0, len(arr)))

