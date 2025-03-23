def greatest_in_two_numbers(a, b):
    return a if a > b else b

if __name__ == "__main__":
    a = int(input("enter num"))
    b = 20
    c = greatest_in_two_numbers(a, b)
    print("The greatest number is:", c)
