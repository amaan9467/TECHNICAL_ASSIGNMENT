def sum_of_digits(n):
    sum_digits = 0
    while n != 0:
        digit = n % 10
        sum_digits += digit
        n //= 10
    return sum_digits

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(sum_of_digits(n))
