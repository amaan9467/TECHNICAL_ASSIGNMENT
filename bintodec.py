def get_decimal(num):
    dec = 0
    p = 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] == '1':
            dec += 2 ** p
        p += 1
    return dec

num = input("Enter the binary number: ")
print("The decimal number is:", get_decimal(num))
