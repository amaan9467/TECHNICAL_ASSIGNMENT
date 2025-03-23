def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i] 

arr = [3, 1, 5, 6, 4, 2, 8]

bubble_sort(arr)  
print("Sorted array:", arr)
