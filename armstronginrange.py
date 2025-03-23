def total_digits(n):
    return len(str(n))

def is_armstrong(n):
    total_digit = total_digits(n)
    sum_of_powers = sum(int(digit) ** total_digit for digit in str(n))
    return sum_of_powers == n

if __name__ == "__main__":
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))

    for i in range(n1, n2 + 1):
        if is_armstrong(i):
            print(f"{i} is an Armstrong number.")
        else:
            print(f"{i} is not an Armstrong number.")
