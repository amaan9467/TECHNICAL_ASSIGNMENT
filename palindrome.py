def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    
    if is_palindrome(n):
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
