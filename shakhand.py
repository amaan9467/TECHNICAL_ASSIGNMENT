def calculate_handshakes(n):
    total_handshakes = 0
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            total_handshakes += 1
    return total_handshakes

n = int(input("Enter the number of people: "))
handshakes = calculate_handshakes(n)
print(handshakes)
