def remove_duplicates(arr):
    return list(set(arr)) 

arr = [1, 4, 2, 3, 1, 2, 6]
unique_arr = remove_duplicates(arr)
print("Array after removing duplicates:", unique_arr)
