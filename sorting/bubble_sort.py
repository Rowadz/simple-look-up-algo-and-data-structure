def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]: arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
        

print(bubble_sort([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))
print(bubble_sort([21, 4, 1, 3, 9, 20, 25, 6, 1, -1]))
