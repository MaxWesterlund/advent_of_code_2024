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
        increasing = False
        safe = True
        for i in range(len(level)):
            if i == 0:
                continue
            
            nbr = level[i]
            last_nbr = level[i - 1]
            
            if nbr == last_nbr:
                safe = False
                break

            diff = nbr - last_nbr

            if abs(diff) < 1 or abs(diff) > 3:
                safe = False
                break

            if i == 1:
                increasing = diff > 0
            elif increasing and diff < 0:
                safe = False
                break
            elif not increasing and diff > 0:
                safe = False
                break
        
        if safe:
            tot += 1
    
    print(tot)
            