import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    start, end = 1, 10
    print(f"Prime numbers between {start} and {end} are:")
    
    for num in range(start, end + 1):
        if is_prime(num):
            print(f"Prime number: {num}")
        else:
            print(f"Not a prime number: {num}")
