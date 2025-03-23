def find_frequency(arr, choice):
    freq_map = {}

    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1

    return freq_map.get(choice, 0)

n = int(input("Enter the size of an array: "))
arr = list(map(int, input("Enter the elements of the array: ").split()))

choice = int(input("Enter the element to find the frequency: "))

frequency = find_frequency(arr, choice)
print(f"The frequency of {choice} is: {frequency}")