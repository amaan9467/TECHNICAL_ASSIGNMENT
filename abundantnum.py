# vo number jiska sum of factors n se jyada hota hai woh abundant number hota hai

def calculate_sum(n):
    return sum(i for i in range(1, n) if n % i == 0)

def is_abundant(n):
    return calculate_sum(n) > n

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    
    if is_abundant(n):
        print("The number is abundant.")
    else:
        print("The number is not abundant.")
        