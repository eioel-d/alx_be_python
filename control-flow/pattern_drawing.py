length = int(input("Enter the size of the pattern: "))
counter = 0
while counter < length:
    for number in range(length):
        print("*", end="")
    counter += 1
    print()
