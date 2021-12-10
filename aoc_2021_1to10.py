import itertools


def day1():
    increased = 0
    depths = []
    file = open("inputs/input1.txt")
    for line in file:
        depths.append(int(line))
    prev = 0
    for d in depths:
        if prev != 0 and d > prev:
            increased += 1
        prev = d
    return increased


def day1_2():
    increased = 0
    depths = []
    file = open("inputs/input1.txt")
    for line in file:
        depths.append(int(line))
    i = 2
    prev = 0
    while i < len(depths):
        d = [depths[i], depths[i - 1], depths[i - 2]]
        if prev != 0 and sum(d) > prev:
            increased += 1
        prev = sum(d)
        i += 1
    return increased


def day2():
    x, y = 0, 0
    file = open("inputs/input2.txt")
    for line in file:
        command = line.split()
        if command[0] == 'forward':
            x += int(command[1])
        if command[0] == 'up':
            y -= int(command[1])
        if command[0] == 'down':
            y += int(command[1])
    return x * y


def day2_2():
    x, y = 0, 0
    aim = 0
    file = open("inputs/input2.txt")
    for line in file:
        command = line.split()
        if command[0] == 'forward':
            x += int(command[1])
            y += int(command[1]) * aim
        if command[0] == 'up':
            aim -= int(command[1])
        if command[0] == 'down':
            aim += int(command[1])
    return x * y


def day3():
    file = open("inputs/input3.txt")
    log = []
    for line in file:
        log.append(line.replace("\n", ""))
    gamma = ""
    for i in range(len(log[0])):
        counter = 0
        for el in log:
            if el[i] == '0':
                counter += 1
        if 2 * counter > len(log):
            gamma += '0'
        else:
            gamma += '1'
    epsilon = ""
    for l in gamma:
        if l == '0':
            epsilon += '1'
        else:
            epsilon += '0'
    print(gamma, epsilon)
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(gamma, epsilon)
    return gamma * epsilon


def day4():
    file = open("inputs/input4.txt")
    stage = -1
    boards, matches = [], []
    nums = []
    for line in file:
        if stage >= 0 and line != "\n":
            n = list(map(int, line.split()))
            boards[stage].append(n)
            matches[stage].append([False for i in n])
        if line == '\n':
            stage += 1
            boards.append([])
            matches.append([])
        if stage == -1:
            nums = line.split(',')
            nums[-1] = nums[-1][:2]
            for i, n in enumerate(nums):
                nums[i] = int(n)
    for num in nums:
        # change matches
        for i, board in enumerate(boards):
            for j, line in enumerate(board):
                for k, el in enumerate(line):
                    if el == num:
                        matches[i][j][k] = True
        for i, board in enumerate(boards):
            for j, line in enumerate(board):
                if all(matches[i][j]):
                    out = 0
                    for k, el in enumerate(line):
                        if not matches[i][j][k]:
                            out += el
                    return out * num
        for i, board in enumerate(boards):
            for j in range(5):
                if all([line[j] for line in matches[i]]):
                    out = 0
                    for a, l in enumerate(board):
                        for b, el in enumerate(l):
                            if not matches[i][a][b]:
                                out += el
                    return out * num


def day4_2():
    file = open("inputs/input4.txt")
    stage = -1
    boards, matches = [], []
    nums = []
    wins = set()
    for line in file:
        if stage >= 0 and line != "\n":
            n = list(map(int, line.split()))
            boards[stage].append(n)
            matches[stage].append([False for i in n])
        if line == '\n':
            stage += 1
            boards.append([])
            matches.append([])
        if stage == -1:
            nums = line.split(',')
            nums[-1] = nums[-1][:2]
            for i, n in enumerate(nums):
                nums[i] = int(n)
    for b in boards:
        print(b)
    unluck = 0
    for num in nums:
        # change matches
        for i, board in enumerate(boards):
            for j, line in enumerate(board):
                for k, el in enumerate(line):
                    if el == num:
                        matches[i][j][k] = True
        for i, board in enumerate(boards):
            for j, line in enumerate(board):
                if all(matches[i][j]):
                    wins.add(i)
        for i, board in enumerate(boards):
            for j in range(5):
                if all([line[j] for line in matches[i]]):
                    wins.add(i)
        if len(wins) == len(boards):
            print(unluck)
            out = 0
            for i, line in enumerate(boards[unluck]):
                print(line)
                for j, el in enumerate(line):
                    if not matches[unluck][i][j]:
                        out += el
            return out * num
        if len(wins) == len(boards) - 1:
            while unluck in wins:
                unluck += 1
            print(unluck)


def day5():
    file = open("inputs/input5.txt")
    maxx, maxy = 0, 0
    for line in file:
        data = line.replace('\n', '')
        data = data.replace('-> ', '')
        data = data.split()
        x1, y1 = list(map(int, data[0].split(',')))
        x2, y2 = list(map(int, data[1].split(',')))
        if x1 > maxx:
            maxx = x1
        if x2 > maxx:
            maxx = x2
        if y1 > maxx:
            maxy = y1
        if y2 > maxx:
            maxy = y2
    grid = [[0 for i in range(maxx + 2)] for j in range(maxy + 2)]
    file = open("inputs/input5.txt")
    for line in file:
        data = line.replace('\n', '')
        data = data.replace('-> ', '')
        data = data.split()
        x1, y1 = list(map(int, data[0].split(',')))
        x2, y2 = list(map(int, data[1].split(',')))
        if x1 == x2:
            if y2 > y1:
                for i in range(y1, y2 + 1):
                    grid[i][x1] += 1
            else:
                for i in range(y2, y1 + 1):
                    grid[i][x1] += 1
        if y1 == y2:
            if x2 > x1:
                for i in range(x1, x2 + 1):
                    grid[y1][i] += 1
            else:
                for i in range(x2, x1 + 1):
                    grid[y1][i] += 1
    occ = 0
    for line in grid:
        for el in line:
            if el > 1:
                occ += 1
    return occ


def day5_2():
    file = open("inputs/input5.txt")
    maxx, maxy = 0, 0
    for line in file:
        data = line.replace('\n', '')
        data = data.replace('-> ', '')
        data = data.split()
        x1, y1 = list(map(int, data[0].split(',')))
        x2, y2 = list(map(int, data[1].split(',')))
        if x1 > maxx:
            maxx = x1
        if x2 > maxx:
            maxx = x2
        if y1 > maxy:
            maxy = y1
        if y2 > maxy:
            maxy = y2
    grid = [[0 for i in range(maxx + 1)] for j in range(maxy + 1)]
    print(maxx, maxy)
    file = open("inputs/input5.txt")
    for line in file:
        data = line.replace('\n', '')
        data = data.replace('-> ', '')
        data = data.split()
        x1, y1 = list(map(int, data[0].split(',')))
        x2, y2 = list(map(int, data[1].split(',')))
        if x1 == x2:
            if y2 > y1:
                for i in range(y1, y2 + 1):
                    grid[i][x1] += 1
            else:
                for i in range(y2, y1 + 1):
                    grid[i][x1] += 1
        if y1 == y2:
            if x2 > x1:
                for i in range(x1, x2 + 1):
                    grid[y1][i] += 1
            else:
                for i in range(x2, x1 + 1):
                    grid[y1][i] += 1
        if x2 > x1 and y2 > y1:
            for i, j in zip(range(x1, x2 + 1), range(y1, y2 + 1)):
                grid[j][i] += 1
        if x1 > x2 and y2 > y1:
            for i, j in zip(range(x2, x1 + 1), range(y2, y1 - 1, -1)):
                grid[j][i] += 1
        if x2 > x1 and y1 > y2:
            for i, j in zip(range(x1, x2 + 1), range(y1, y2 - 1, -1)):
                grid[j][i] += 1
        if x1 > x2 and y1 > y2:
            for i, j in zip(range(x2, x1 + 1), range(y2, y1 + 1)):
                grid[j][i] += 1
    occ = 0
    for line in grid:
        for el in line:
            if el > 1:
                occ += 1
    return occ


def day6():
    # also 6_2, just change days
    days = 256
    with open("inputs/input6.txt", 'r') as file:
        data = file.readlines()
        data = list(map(int, data[0].strip().split(",")))
    cnt = [data.count(i) for i in range(9)]
    for i in range(days):
        new = cnt[0]
        cnt = cnt[1:]
        cnt[6] += new
        cnt.append(new)
    return sum(cnt)


def day7():
    with open("inputs/input7.txt", "r") as file:
        data = file.readlines()
        data = list(map(int, data[0].strip().split(",")))
    max_el = max(data)
    min_move = 1000000000
    for i in range(max_el + 1):
        edited_data = data.copy()
        for j, el in enumerate(data):
            edited_data[j] = abs(edited_data[j] - i)
        move = sum(edited_data)
        if move < min_move:
            min_move = move
    return min_move


def day7_2():
    with open("inputs/input7.txt", "r") as file:
        data = file.readlines()
        data = list(map(int, data[0].strip().split(",")))
    max_el = max(data)
    min_move = 1000000000
    for i in range(max_el + 1):
        edited_data = data.copy()
        for j, el in enumerate(data):
            x = abs(el - i)
            edited_data[j] = int((x ** 2 + x) / 2)
        move = sum(edited_data)
        if move < min_move:
            min_move = move
    return min_move


def day8():
    file = open("inputs/input8.txt", "r")
    occ = 0
    for line in file:
        data = line.strip().split("|")
        after = data[1].split()
        for el in after:
            length = len(el)
            if length == 2 or length == 3 or length == 4 or length == 7:
                occ += 1
    return occ


def day8_2():
    file = open("inputs/input8.txt", "r")
    out = 0
    for line in file:
        before, after = line.strip().split("|")
        together = before.split() + after.split()
        pairs = [0 for i in range(10)]
        checklist = [-1 for i in range(7)]
        for el in together:
            if len(el) == 2:
                pairs[1] = el
            if len(el) == 3:
                pairs[7] = el
            if len(el) == 4:
                pairs[4] = el
            if len(el) == 7:
                pairs[8] = el
        for el in pairs[7]:
            if el not in pairs[1]:
                checklist[0] = el
        # engage '3'
        for el in together:
            if len(el) == 5 and pairs[1][0] in el and pairs[1][1] in el and pairs[3] == 0:
                for letter in el:
                    if letter in pairs[4] and letter not in pairs[1]:
                        checklist[6] = letter
                    if letter not in checklist and letter not in pairs[1]:
                        checklist[3] = letter
                pairs[3] = el
        # complete the '4'
        for letter in pairs[4]:
            if letter not in checklist and letter not in pairs[1]:
                checklist[5] = letter
        # engage '5'
        for el in together:
            if len(el) == 5 and pairs[5] == 0:
                in_list = 0
                for letter in el:
                    if letter in checklist:
                        in_list += 1
                if in_list == 4:
                    for letter in el:
                        if letter not in checklist:
                            checklist[2] = letter
                            pairs[5] = el
        # complete the '1'
        for letter in pairs[1]:
            if letter not in checklist:
                checklist[1] = letter
        # complete checklist with missing letter from alphabet
        alph = [chr(i) for i in range(ord('a'), ord('g') + 1)]
        for el in alph:
            if el not in checklist:
                for i, c in enumerate(checklist):
                    if c == -1:
                        checklist[i] = el
        # fill missing
        for el in together:
            if len(el) == 5:
                if checklist[0] in el and checklist[1] in el and checklist[6] in el and checklist[4] in el and \
                        checklist[3] in el:
                    pairs[2] = el
            if len(el) == 6:
                if checklist[0] in el and checklist[1] in el and checklist[2] in el and checklist[3] in el and \
                        checklist[4] in el and checklist[5] in el:
                    pairs[0] = el
                if checklist[0] in el and checklist[6] in el and checklist[2] in el and checklist[3] in el and \
                        checklist[4] in el and checklist[5] in el:
                    pairs[6] = el
                if checklist[0] in el and checklist[1] in el and checklist[2] in el and checklist[3] in el and \
                        checklist[6] in el and checklist[5] in el:
                    pairs[9] = el

        for i, el in enumerate(pairs):
            pairs[i] = ''.join(sorted(el))
        to_add = ''
        after = after.split()
        for el in after:
            for i, pair in enumerate(pairs):
                if ''.join(sorted(el)) == pair:
                    to_add += str(i)
        out += int(to_add)
    return out


def day9():
    file = open("inputs/input9.txt", "r")
    grid = []
    out = 0
    for line in file:
        data = list(map(int, line.strip()))
        grid.append(data)
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            low_point = True
            if i == 0:
                if grid[i + 1][j] <= el:
                    low_point = False
            elif i == len(grid) - 1:
                if grid[i - 1][j] <= el:
                    low_point = False
            else:
                if grid[i + 1][j] <= el or grid[i - 1][j] <= el:
                    low_point = False
            if j == 0:
                if line[j + 1] <= el:
                    low_point = False
            elif j == len(line) - 1:
                if line[j - 1] <= el:
                    low_point = False
            else:
                if line[j - 1] <= el or line[j + 1] <= el:
                    low_point = False
            if low_point:
                out += el + 1
    return out


def getneighbors(i, j, matrix, visited):
    """
    returns unvisited neighbors of (i, j)
    :param i: row of matrix
    :param j: element of row
    :param matrix: matrix
    :param visited: copy of matrix with True if visited, else False
    :return: list of unvisited neighbors
    """
    unv = []
    if i > 0 and not visited[i - 1][j] and matrix[i - 1][j] != 9:
        unv.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j] and matrix[i + 1][j] != 9:
        unv.append([i + 1, j])
    if j > 0 and not visited[i][j - 1] and matrix[i][j - 1] != 9:
        unv.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1] and matrix[i][j + 1] != 9:
        unv.append([i, j + 1])
    return unv


def findpath(i, j, visited, unv, matrix):
    group = [[i, j]]
    visited[i][j] = True
    for n in unv:
        visited[n[0]][n[1]] = True
        if matrix[n[0]][n[1]] != 9:
            group.extend(findpath(n[0], n[1], visited, getneighbors(n[0], n[1], matrix, visited),
                                  matrix))
    group.sort()
    group = list(group for group, _ in itertools.groupby(group))
    return group


def day9_2():
    file = open("inputs/input9.txt", "r")
    grid = []
    out = []
    for line in file:
        data = list(map(int, line.strip()))
        grid.append(data)
    for i, line in enumerate(grid):
        for j, el in enumerate(line):
            low_point = True
            if i == 0:
                if grid[i + 1][j] <= el:
                    low_point = False
            elif i == len(grid) - 1:
                if grid[i - 1][j] <= el:
                    low_point = False
            else:
                if grid[i + 1][j] <= el or grid[i - 1][j] <= el:
                    low_point = False
            if j == 0:
                if line[j + 1] <= el:
                    low_point = False
            elif j == len(line) - 1:
                if line[j - 1] <= el:
                    low_point = False
            else:
                if line[j - 1] <= el or line[j + 1] <= el:
                    low_point = False
            if low_point:
                out.append([i, j])

    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    lengths = []
    for starts in out:
        if not visited[starts[0]][starts[1]]:
            visited[starts[0]][starts[1]] = True
            unv = getneighbors(starts[0], starts[1], grid, visited)
            lengths.append(len(findpath(starts[0], starts[1], visited, unv, grid)))
    lengths = sorted(lengths)
    return lengths[-1] * lengths[-2] * lengths[-3]


def day10():
    file = open("inputs/input10.txt", "r")
    out = 0
    closers = [">", ")", "]", "}"]
    for line in file:
        data = line.strip()
        expected_closer = []
        for el in data:
            if el == "<":
                expected_closer.append(">")
            if el == "(":
                expected_closer.append(")")
            if el == "[":
                expected_closer.append("]")
            if el == "{":
                expected_closer.append("}")
            if el in closers:
                exp = expected_closer[-1]
                if el == exp:
                    expected_closer = expected_closer[:-1]
                else:
                    if el == closers[0]:
                        out += 25137
                        break
                    if el == closers[1]:
                        out += 3
                        break
                    if el == closers[2]:
                        out += 57
                        break
                    if el == closers[3]:
                        out += 1197
                        break
    return out


def day10_2():
    file = open("inputs/input10.txt", "r")
    scores = []
    closers = [">", ")", "]", "}"]
    for line in file:
        data = line.strip()
        expected_closer = []
        score = 0
        for el in data:
            if el == "<":
                expected_closer.append(">")
            if el == "(":
                expected_closer.append(")")
            if el == "[":
                expected_closer.append("]")
            if el == "{":
                expected_closer.append("}")
            if el in closers:
                exp = expected_closer[-1]
                if el == exp:
                    expected_closer = expected_closer[:-1]
                else:
                    break
        else:
            while len(expected_closer) > 0:
                score *= 5
                el = expected_closer.pop()
                if el == ")":
                    score += 1
                if el == "]":
                    score += 2
                if el == "}":
                    score += 3
                if el == ">":
                    score += 4
            scores.append(score)

    scores = sorted(scores)
    return scores[int(len(scores)/2)]


print(day10_2())
