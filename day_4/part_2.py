with open("input.txt", "r") as file:
    grid = []
    for line in file:
        grid.append(line.replace("\n", ""))
    
    height = len(grid)
    width = len(grid[0])
    
    tot = 0

    for y in range(1, height - 1):
        for x in range(1, width - 1):
            letter = grid[y][x]

            if letter != "A":
                continue
            
            nw_letter = grid[y - 1][x - 1]
            ne_letter = grid[y - 1][x + 1]
            se_letter = grid[y + 1][x + 1]
            sw_letter = grid[y + 1][x - 1]

            if (nw_letter == "M" and se_letter == "S" or nw_letter == "S" and se_letter == "M") and (ne_letter == "M" and sw_letter == "S" or ne_letter == "S" and sw_letter == "M"):
                tot += 1

    print(tot)