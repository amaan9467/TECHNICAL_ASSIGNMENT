def calculate_sum(n):
    sum_factors = sum(i for i in range(1, n // 2 + 1) if n % i == 0)
    return sum_factors

def is_friendly(n1, n2):
    sum_of_num1 = calculate_sum(n1)
    sum_of_num2 = calculate_sum(n2)

    return (sum_of_num1 / n1) == (sum_of_num2 / n2)

# Taking input from the user
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if is_friendly(n1, n2):
    print(f"{n1} and {n2} are Friendly Pair.")
else:
    print(f"{n1} and {n2} are NOT Friendly Pair.")
