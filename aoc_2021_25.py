def day25():
    grid = []
    file = open("inputs/input25.txt")
    for line in file:
        grid.append(list(line.strip()))
    steps = 0
    while True:
        moves = False
        gridcopy = [row[:] for row in grid]
        for i, line in enumerate(grid):
            for j, el in enumerate(line):
                if el == '>':
                    if j == len(line) - 1:
                        if line[0] == '.':
                            moves=True
                            gridcopy[i][0] = '>'
                            gridcopy[i][j] = '.'
                    else:
                        if line[j + 1] == '.':
                            moves = True
                            gridcopy[i][j + 1] = '>'
                            gridcopy[i][j] = '.'
        grid = [row[:] for row in gridcopy]
        gridcopy = [row[:] for row in grid]
        for i, line in enumerate(grid):
            for j, el in enumerate(line):
                if el == 'v':
                    if i == len(grid) - 1:
                        if grid[0][j] == '.':
                            moves = True
                            gridcopy[0][j] = 'v'
                            gridcopy[i][j] = '.'
                    else:
                        if grid[i+1][j] == '.':
                            moves = True
                            gridcopy[i+1][j] = 'v'
                            gridcopy[i][j] = '.'
        grid = [row[:] for row in gridcopy]
        steps += 1
        if not moves:
            return steps


print(day25())
