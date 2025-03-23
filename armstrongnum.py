def total_digits(n):
    return len(str(n))

def is_armstrong(n):
    total_digit = total_digits(n)
    sum_of_powers = sum(int(digit) ** total_digit for digit in str(n))
    return sum_of_powers == n

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    if is_armstrong(n):
        print("The number is an Armstrong number.")
    else:
        print("The number is not an Armstrong number.")
