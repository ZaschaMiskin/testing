def day13():
    """

    :return: nothing, done through prints at the end
    """
    file = open("inputs/input13.txt")
    stage = 2
    x_max, y_max = 0, 0
    for line in file:
        if line == '\n':
            break
        x, y = list(map(int, line.strip().split(',')))
        if x > x_max:
            x_max = x
        if y > y_max:
            y_max = y
    grid = [['.' for i in range(x_max + 1)] for j in range(y_max + 1)]
    file = open("inputs/input13.txt")
    for line in file:
        if line == '\n':
            break
        x, y = list(map(int, line.strip().split(',')))
        grid[y][x] = '#'
    for line in file:
        if line == '\n':
            break
        imp = line.strip().split()[2]
        direction, val = imp.split('=')
        val = int(val)
        current_offset = 0
        if direction == 'x':
            while val + current_offset < x_max:
                current_offset += 1
                for i, row in enumerate(grid):
                    if row[val + current_offset] == '#':
                        grid[i][val - current_offset] = '#'
            x_max = val - 1
            for i in range(len(grid)):
                grid[i] = grid[i][:val]
        else:
            while val + current_offset < y_max:
                current_offset += 1
                for i in range(x_max + 1):
                    if grid[val + current_offset][i] == '#':
                        grid[val - current_offset][i] = '#'
            y_max = val-1
            grid = grid[:val]

        if stage == 1:
            count = 0
            for row in grid:
                print(row)
                for el in row:
                    if el == '#':
                        count += 1
            return count
    for row in grid:
        print(row)


print(day13())
