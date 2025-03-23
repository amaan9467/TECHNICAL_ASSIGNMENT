def second_largest(arr):
    if len(arr) < 2:
        return "Array must have at least two elements."

    max_num = second_max = float('-inf')

    for num in arr:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num

    return second_max if second_max != float('-inf') else "No second largest number."

n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the numbers: ").split()))

print("Second largest number is:", second_largest(arr))
