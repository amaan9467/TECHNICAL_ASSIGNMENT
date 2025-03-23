def calculate_lcm(n1, n2):
    max_val = max(n1, n2)
    lcm = max_val
    while True:
        if lcm % n1 == 0 and lcm % n2 == 0:
            return lcm
        lcm += max_val

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

print(f"The LCM of {n1} and {n2} is: {calculate_lcm(n1, n2)}")
