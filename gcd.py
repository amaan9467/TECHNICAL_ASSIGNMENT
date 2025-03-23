def gcd(a, b):
    while b:
        a, b = b, a % b  
    return a

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print(gcd(n1, n2))
