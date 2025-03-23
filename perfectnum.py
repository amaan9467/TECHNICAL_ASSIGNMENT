def is_perfect(n):
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_of_divisors == n

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    
    if is_perfect(n):
        print(f"The number {n} is a Perfect Number.")
    else:
        print(f"The number {n} is NOT a Perfect Number.")
