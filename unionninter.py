def find_union(arr1, arr2):
    return list(set(arr1) | set(arr2)) 

def find_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2)) 

arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]

print("Union of the two arrays:")
print(find_union(arr1, arr2))


print("Intersection of the two arrays:")
print(find_intersection(arr1, arr2))
