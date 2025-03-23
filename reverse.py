def reverse_number(n):
    rev = 0
    while n != 0:
        r = n % 10
        rev = rev * 10 + r
        n //= 10  
    return rev

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    reversed_number = reverse_number(num)
    print("Reversed Number:", reversed_number)
