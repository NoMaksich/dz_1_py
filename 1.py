length = int(input("Введите длину: "))
height = int(input("Введите высоту: "))

for line in range(height):
    for column in range(length):
        if column == 0 or column == length - 1:
            print('|', end='')
        elif line == 0 or line == height - 1:
            print("-", end="")
        else:
            print(" ", end="")
    print()
