def is_palindrome(n):
    return str(n) == str(n)[::-1]

def longest_palindromic(arr):
    max_palindrome = -1
    index = -1

    for i, num in enumerate(arr):
        if is_palindrome(num) and num > max_palindrome:
            max_palindrome = num
            index = i

    return max_palindrome, index

arr = [11, 212, 53453, 123, 1236123]
max_palindrome, index = longest_palindromic(arr)

if max_palindrome != -1:
    print(f"Longest palindromic number is {max_palindrome} at index {index}")
else:
    print("No palindromic number found")