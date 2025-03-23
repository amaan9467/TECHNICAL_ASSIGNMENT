def move_negatives(arr):
    l, r = 0, len(arr) - 1

    while l < r:
        while l < r and arr[l] >= 0:
            l += 1
        while l < r and arr[r] < 0:
            r -= 1
        if l < r:
            arr[l], arr[r] = arr[r], arr[l]  

n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the elements: ").split()))

move_negatives(arr)

print("The arranged elements are:")
print(*arr)  
