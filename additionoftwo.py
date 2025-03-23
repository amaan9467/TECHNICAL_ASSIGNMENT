import math

def find_lcm(b, d):
    return (b * d) // math.gcd(b, d) 

def add_fractions(a, b, c, d):
    lcm = find_lcm(b, d)
    numerator_sum = (a * (lcm // b)) + (c * (lcm // d))

    gcd = math.gcd(numerator_sum, lcm)
    final_numerator = numerator_sum // gcd
    final_denominator = lcm // gcd

    return f"{final_numerator}/{final_denominator}"

a, b = map(int, input("Enter the first fraction (numerator denominator): ").split())
c, d = map(int, input("Enter the second fraction (numerator denominator): ").split())

print(add_fractions(a, b, c, d))
