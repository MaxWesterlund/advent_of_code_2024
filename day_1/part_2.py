with open("input.txt", "r") as file:
    left_row = []
    right_row = []

    for line in file:
        numbers = line.split("   ")
        left_row.append(int(numbers[0]))
        right_row.append(int(numbers[1]))

    tot = 0

    for nbr in left_row:
        count = 0
        for num in right_row:
            if nbr == num:
                count += 1
        tot += count * nbr
    
    print(tot)
