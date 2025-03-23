def scalar_product(arr1, arr2):
    return sum(x * y for x, y in zip(arr1, arr2))

arr1 = [10, 30, 50, 20]
arr2 = [2, 4, 5, 1]

arr1.sort()  
arr2.sort()  

result = scalar_product(arr1, arr2)
print("The maximum Scalar product:", result)
