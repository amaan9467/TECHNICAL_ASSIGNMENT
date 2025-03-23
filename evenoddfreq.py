def count_even_odd(arr):
    even = sum(1 for num in arr if num % 2 == 0)
    odd = len(arr) - even
    return even, odd

arr = [1, 2, 3, 4, 5, 6,7]

even_count, odd_count = count_even_odd(arr)
print(f"The even and odd count is: {even_count} {odd_count}")
