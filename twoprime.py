import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def express_as_two_primes(n):
    for i in range(2, n):
        for j in range(i + 1, n):
            if is_prime(i) and is_prime(j) and i + j == n:
                return True
    return False

n = int(input("Enter the number: "))
if express_as_two_primes(n):
    print(f"{n} is the sum of two prime numbers")
else:
    print(f"{n} is not the sum of two prime numbers")