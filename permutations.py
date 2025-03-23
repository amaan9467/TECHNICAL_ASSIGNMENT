def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def nPr(n, r):
    return factorial(n) // factorial(n - r)

n = int(input("Enter the number of students: "))
r = int(input("Enter the number of chairs: "))

perm = nPr(n, r)
print(perm)
