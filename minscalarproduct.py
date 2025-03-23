def scalar_product(arr1, arr2):
    return sum(a * b for a, b in zip(sorted(arr1), sorted(arr2, reverse=True)))

arr1 = [10, 30, 40, 20]
arr2 = [2, 4, 5, 1]

print("The minimum Scalar product:", scalar_product(arr1, arr2))