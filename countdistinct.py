def count_distinct(nums):
    return len(set(nums))

nums = [1, 2, 2, 3, 6, 2]

n = count_distinct(nums)
print(f"The distinct elements are {n}")
