def day17_1():
    file = open("inputs/input17.txt")
    for line in file:
        data = line.strip().split(': ')[1]
        x, y = data.split(', ')
        y1, y2 = list(map(int, y[2:].split('..')))
        y_bound = abs(min(y1, y2))
        return (y_bound * (y_bound - 1)) / 2


def day17_2():
    """
    hardcoded AND inefficient(not that inefficient)
    :return: num of starting velocities
    """
    file = open("inputs/input17.txt")
    x1, x2, y1, y2, y_bound = 0, 0, 0, 0, 0
    for line in file:
        data = line.strip().split(': ')[1]
        x, y = data.split(', ')
        x1, x2 = list(map(int, x[2:].split('..')))
        y1, y2 = list(map(int, y[2:].split('..')))
    out = 0
    for i in range(x2 + 1):  # v_x
        for j in range(y1, -y1):  # v_y
            a, b = i, j
            pos = [0, 0]
            while pos[0] <= x2 and pos[1] >= y1:
                pos[0] += a
                pos[1] += b
                if x1 <= pos[0] <= x2 and y2 >= pos[1] >= y1:  # found
                    out += 1
                    break
                if a > 0:
                    a -= 1
                b -= 1
    return out


print(day17_2())
