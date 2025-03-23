#jiska square last digit se match hota hai woh automorphic number hota hai
# 5*5=25

def calculate_digit(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def is_automorphic(n):
    digit = calculate_digit(n)
    sq = n * n
    zeroes = 10 ** digit 
    return n == sq % zeroes

n = int(input("Enter the number: "))

if is_automorphic(n):
    print("Automorphic number")
else:
    print("Not an Automorphic number")