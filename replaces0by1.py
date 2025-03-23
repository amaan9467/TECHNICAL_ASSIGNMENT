def reverse_number(n):
    rev_n = 0
    while n > 0:
        rev_n = rev_n * 10 + n % 10
        n //= 10
    return rev_n

def replace_zeros_with_ones(n):
    res = 0
    while n > 0:
        rem = n % 10
        if rem == 0:
            res = res * 10 + 1
        else:
            res = res * 10 + rem
        n //= 10
    return reverse_number(res)

n = int(input("Enter the number: "))
ans = replace_zeros_with_ones(n)
print(ans)
