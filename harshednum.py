def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def is_harshad_number(n):
    return n % digit_sum(n) == 0

n = int(input("Enter the number: "))

if is_harshad_number(n):
    print("Harshad Number")
else:
    print("Not a Harshad Number")
