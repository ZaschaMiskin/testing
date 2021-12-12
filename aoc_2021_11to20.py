grid = []
flashes = 0


def flash_adj(i, j, flashed):
    global flashes
    xrange = list(range(i - 1, i + 2))
    yrange = list(range(j - 1, j + 2))
    if -1 in xrange:
        xrange.remove(-1)
    if 10 in xrange:
        xrange.remove(10)
    if -1 in yrange:
        yrange.remove(-1)
    if 10 in yrange:
        yrange.remove(10)
    for x in xrange:
        for y in yrange:
            if (not (x == i and y == j)) and not flashed[x][y]:
                grid[x][y] += 1
                if grid[x][y] > 9:
                    flashes += 1
                    flashed[x][y] = True
                    grid[x][y] = 0
                    flash_adj(x, y, flashed)


def day11():
    # both part 1 and 2, just change return statement
    global flashes
    file = open("inputs/input11.txt")
    for line in file:
        grid.append(list(map(int, line.strip())))
    print(grid)
    for it in range(100000):
        flashed = [[False for a in grid[0]] for b in grid]
        for i, line in enumerate(grid):
            for j, el in enumerate(line):
                if not flashed[i][j]:
                    grid[i][j] += 1
                if grid[i][j] > 9:
                    flashes += 1
                    grid[i][j] = 0
                    flashed[i][j] = True
                    flash_adj(i, j, flashed)
        for line in grid:
            print(line)
        out = True
        for line in flashed:
            for el in line:
                if not el:
                    out = False
        if out:
            return it + 1


paths = []


def add_paths(path, connections, dup):
    current = path[-1]
    if current == 'end':
        if path not in paths:
            paths.append(path)
            return
    for a, c in enumerate(connections):
        if c[0] == current and c[1] == dup and path.count(c[1]) < 2:
            add_paths(path + [c[1]], connections, dup)
        elif c[0] == current and not (c[1] in path and c[1].islower()):
            add_paths(path + [c[1]], connections, dup)


def day12():
    file = open('inputs/input12.txt')
    connections = []
    for line in file:
        connections.append(line.strip().split('-'))
        connections.append(list(reversed(line.strip().split('-'))))
    lower_nodes = []
    for c in connections:
        c0 = c[0]
        c1 = c[1]
        if c0 not in lower_nodes and c0.islower() and c0 != 'start' and c0 != 'end':
            lower_nodes.append(c0)
        if c1 not in lower_nodes and c1.islower() and c1 != 'start' and c1 != 'end':
            lower_nodes.append(c1)

    for dup in lower_nodes:
        for i, c in enumerate(connections):
            if c[0] == 'start':
                path = connections[i]
                add_paths(path, connections, dup)
    return len(paths)


print(day12())
