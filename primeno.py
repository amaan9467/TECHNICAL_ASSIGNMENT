import math

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    if is_prime(n):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
