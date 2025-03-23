def decimal_to_hex(n):
    return hex(n)[2:].upper()  

n = int(input("Enter a decimal number: "))
print(decimal_to_hex(n))