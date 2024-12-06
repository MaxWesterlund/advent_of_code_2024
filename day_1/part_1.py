with open("input.txt", "r") as file:
    left_row = []
    right_row = []

    for line in file:
        numbers = line.split("   ")
        left_row.append(int(numbers[0]))
        right_row.append(int(numbers[1]))

    left_row.sort()
    right_row.sort()

    tot = 0

    for i in range(len(left_row)):
        tot += abs(right_row[i] - left_row[i])

    print(tot)