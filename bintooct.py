def binary_to_octal(binary_str):
    decimal = int(binary_str, 2) 
    octal = oct(decimal)[2:]  
    return octal

binary_str = input("Enter the binary number: ")
print(binary_to_octal(binary_str))
