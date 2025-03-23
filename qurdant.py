def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "The first quadrant"
    elif x < 0 and y > 0:
        return "The second quadrant"
    elif x < 0 and y < 0:
        return "The third quadrant"
    elif x > 0 and y < 0:
        return "The fourth quadrant"
    elif x != 0 and y == 0:
        return "The X-axis"
    elif x == 0 and y != 0:
        return "The Y-axis"
    else:
        return "Origin"

x = int(input("Enter X-axis coordinate: "))
y = int(input("Enter Y-axis coordinate: "))

print(find_quadrant(x, y))
