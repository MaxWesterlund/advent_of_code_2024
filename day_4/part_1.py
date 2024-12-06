with open("input.txt", "r") as file:
    grid = []
    for line in file:
        grid.append(line.replace("\n", ""))
    
    height = len(grid)
    width = len(grid[0])
    
    tot = 0

    for y in range(height):
        for x in range(width):
            for i in range(4):
                x_pos = x
                y_pos = y
                x_dir = 0
                y_dir = 0

                match i:
                    case 0:
                        x_dir = -1
                        y_dir = 1
                    case 1:
                        y_dir = 1
                    case 2:
                        x_dir = 1
                        y_dir = 1
                    case 3:
                        x_dir = 1

                word = ""
                for j in range(0, 4):
                    if min(x_pos, y_pos) < 0 or x_pos >= width or y_pos >= height:
                        break
                    
                    next_letter = grid[y_pos][x_pos]
                    word += next_letter

                    x_pos += x_dir
                    y_pos += y_dir
                
                if word == "XMAS" or word == "SAMX":
                    tot += 1

    print(tot)
