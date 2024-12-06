with open("input.txt", "r") as file:
    levels = []

    for line in file:
        numbers = line.split(" ")
        level = []
        for n in numbers:
            level.append(int(n))
        levels.append(level)

    tot = 0

    for level in levels:
        for i in range(-1, len(level)):
            row = level.copy()
            if i != -1:
                row.pop(i)
            increasing = False
            safe = True
            for j in range(len(row)):
                if j == 0:
                    continue

                failed = False
                
                nbr = row[j]
                last_nbr = row[j - 1]
                
                if nbr == last_nbr:
                    safe = False
                    break

                diff = nbr - last_nbr

                if abs(diff) < 1 or abs(diff) > 3:
                    safe = False
                    break

                if j == 1:
                    increasing = diff > 0
                elif increasing and diff < 0:
                    safe = False
                    break
                elif not increasing and diff > 0:
                    safe = False
                    break
            
            if safe:
                tot += 1
                break
    
    print(tot)