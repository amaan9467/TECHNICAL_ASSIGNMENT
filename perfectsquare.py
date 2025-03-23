import math

def is_perfect_square(n):
    x = int(math.sqrt(n))
    return x * x == n

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    
    if is_perfect_square(n):
        print(f"The number {n} is a Perfect Square.")
    else:
        print(f"The number {n} is NOT a Perfect Square.")