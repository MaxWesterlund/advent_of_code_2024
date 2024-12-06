import re

with open("input.txt", "r") as file:
    content = file.read()
    regex = re.findall(r"mul[(](\d+),(\d+)[)]", content)

    tot = 0

    for item in regex:
        tot += int(item[0]) * int(item[1])
    
    print(tot)