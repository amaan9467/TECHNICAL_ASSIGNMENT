def decimal_to_binary(n):
    return bin(n)[2:] 

n = int(input("Enter the decimal number: "))
print(decimal_to_binary(n))
