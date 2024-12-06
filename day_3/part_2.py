import re

with open("input.txt", "r") as file:
    content = file.read()
    regex = re.findall(r"mul[(](\d+),(\d+)[)]|(do[(][)])|(don't[(][)])", content)

    tot = 0
    doing = True

    for item in regex:
        if item[2] == "do()":
            doing = True
        elif item[3] == "don't()":
            doing = False
        elif doing:
            tot += int(item[0]) * int(item[1])
    
    print(tot)