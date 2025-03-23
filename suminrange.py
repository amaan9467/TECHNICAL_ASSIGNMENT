def sum_in_range(num1, num2):
    return sum(range(num1, num2 + 1))

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Sum of range {num1} and {num2} is: {sum_in_range(num1, num2)}")
