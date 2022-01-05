def day20():
    file = open("inputs/input20.txt")
    steps = 50
    rules = ""
    grid = []
    for line in file:
        if line == "\n":
            break
        rules = line.strip()
    for line in file:
        grid.append(list(line.strip()))
    for i in range(steps):
        grid.append(["." for i in range(len(grid[0]))])
        grid.insert(0, ["." for i in range(len(grid[0]))])
    for i, el in enumerate(grid):
        for a in range(steps):
            grid[i].insert(0, ".")
            grid[i].append(".")
    grid_copy = [row[:] for row in grid]
    for step in range(steps):
        grid = [row[:] for row in grid_copy]
        for i, line in enumerate(grid):
            for j, el in enumerate(line):
                neigh = []
                for a in range(i - 1, i + 2):
                    for b in range(j - 1, j + 2):
                        if a < 0 or a >= len(grid) or b < 0 or b >= len(grid):
                            if step % 2 == 0:
                                neigh.append("0")
                            else:
                                neigh.append("1")
                        else:
                            if grid[a][b] == ".":
                                neigh.append("0")
                            else:
                                neigh.append("1")
                num = int("".join(neigh), 2)
                grid_copy[i][j] = rules[num]
        print(step)
    counter = 0
    for line in grid_copy:
        for el in line:
            if el == "#":
                counter += 1
    return counter


print(day20())
