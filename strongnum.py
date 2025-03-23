def factorial(r):
    fact = 1
    for i in range(1, r + 1):
        fact *= i
    return fact

def is_strong(n):
    sum_digits = 0
    temp = n
    while n > 0:
        r = n % 10
        sum_digits += factorial(r)
        n //= 10
    return temp == sum_digits

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    if is_strong(n):
        print(f"The number is Strong: {n}")
    else:
        print(f"The number is not Strong: {n}")
