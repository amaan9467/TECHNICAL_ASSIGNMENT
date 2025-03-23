def sum_of_n(n):
    return sum(range(1, n + 1))

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("Sum of n numbers:", sum_of_n(n))
