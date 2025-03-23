def power_of_n(n, p):
    res = 1
    for _ in range(p):
        res *= n
    return res

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    p = int(input("Enter the power: "))
    
    result = power_of_n(n, p)
    print(f"The result is {result}")