import math

def find_roots(a, b, c):
    if a == 0:
        return "Coefficient 'a' cannot be zero."

    d = b**2 - 4*a*c  # Discriminant

    if d > 0:
        r1 = (-b - math.sqrt(d)) / (2 * a)
        r2 = (-b + math.sqrt(d)) / (2 * a)
        return f"The roots of the quadratic equation are {r1:.2f} and {r2:.2f}"
    elif d == 0:
        r1 = -b / (2 * a)
        return f"The root of the quadratic equation is {r1:.2f}"
    else:
        real = -b / (2 * a)
        imag = math.sqrt(abs(d)) / (2 * a)
        return f"The roots of the quadratic equation are complex: {real:.2f} ± {imag:.2f}i"

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

print(find_roots(a, b, c))
