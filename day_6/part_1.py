file = open("test_input.txt", "r").readlines()

grid = []

guard_x = 0
guard_y = 0
guard_dir = 90

for y in len(file):
    row = []
    for x in len(file[y]):
        value = file[y][x]
        if value == "^":
            guard_x = x
            guard_y = y
        row.append(value)
    grid.append(row)

while True:
    y = 0
