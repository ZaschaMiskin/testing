def countadj(i, j, lines):
    out = 0
    for a in range(i, 0, -1):
        if lines[a][j] == 'L':
            break
        if lines[a][j] == '#':
            out += 1
            break
    for a in range(i, len(lines)):
        if lines[a][j] == 'L':
            break
        if lines[a][j] == '#':
            out += 1
            break
    for a in range(j, 0, -1):
        if lines[i][a] == 'L':
            break
        if lines[i][a] == '#':
            out += 1
            break
    for a in range(j, len(lines[0])):
        if lines[i][a] == 'L':
            break
        if lines[i][a] == '#':
            out += 1
            break
    a, b = i, j
    while a > 0 and b > 0:
        a -= 1
        b -= 1
        if lines[a][b] == 'L':
            break
        if lines[a][b] == '#':
            out += 1
            break
    a, b = i, j
    while a < len(lines) - 1 and b > 0:
        a += 1
        b -= 1
        if lines[a][b] == 'L':
            break
        if lines[a][b] == '#':
            out += 1
            break
    a, b = i, j
    while a > 0 and b < len(lines[0]) - 1:
        a -= 1
        b += 1
        if lines[a][b] == 'L':
            break
        if lines[a][b] == '#':
            out += 1
            break
    a, b = i, j
    while a < len(lines) - 1 and b < len(lines[0]) - 1:
        a += 1
        b += 1
        if lines[a][b] == 'L':
            break
        if lines[a][b] == '#':
            out += 1
            print('found occ at ' + str(b) + ',' + str(a) + ' for x,y=' + str(j) + ',' + str(i))
            break

    return out


def aoc_111():
    file = open('input11.txt', 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    prev = lines.copy()
    while 1:
        for i in range(len(lines)):
            # every line
            tmp = [c for c in lines[i]]
            for j, el in enumerate(tmp):
                if el == 'L':
                    if countadj(i, j, lines) == 0:
                        tmp[j] = '#'
                if el == '#':
                    if countadj(i, j, lines) > 4:
                        tmp[j] = 'L'
            prev[i] = ''.join(tmp)
        if lines == prev:
            break
        lines = prev.copy()
    occ = 0
    for line in lines:
        for el in line:
            if el == '#':
                occ += 1
    return occ


def aoc_131():
    file = open('input13.txt', 'r')
    info = []
    for line in file:
        info.append(line.strip('\n'))
    start_time = int(info[0])
    info = info[1]
    ids = []
    info = info.split(',')
    for i in info:
        if i.isnumeric():
            ids.append(int(i))
    low = 1000
    found_id = 0
    for i, tmp in enumerate(ids):
        x = start_time % tmp
        x = tmp - x
        if x < low:
            low = x
            found_id = i
    return ids[found_id] * low


def aoc_132():
    file = open('input13.txt', 'r')
    info = []
    for line in file:
        info.append(line.strip('\n'))
    info = info[1]
    ids = []
    info = info.split(',')
    offset = []
    c_off = 0
    for i in info:
        if i.isnumeric():
            ids.append(int(i))
            offset.append(c_off)
        c_off += 1
    t = 305068317272990
    # t = 1044388633269293 n + 305068317272992, n element Z
    while True:
        for i, off in enumerate(offset):
            if not (t + off) % ids[i] == 0:
                break
            if off == offset[-1]:
                return t
        t += 1
        print(t)


def aoc_141():
    file = open('input14.txt', 'r')
    current_mask = ''
    registry = dict()
    for line in file:
        if line[:4] == 'mask':
            current_mask = (line[7:].strip('\n'))
        else:
            tgt_start = 4
            tgt_end = 0
            for i, el in enumerate(line):
                if el == ']':
                    tgt_end = i
            tgt = int(line[tgt_start:tgt_end])
            val = int(line[tgt_end + 4:])
            val = str(bin(val)[2:])
            while len(val) < 36:
                val = '0' + val
            for i, el in enumerate(val):
                if current_mask[i] != 'X':
                    val = val[:i] + current_mask[i] + val[i + 1:]
            val = int(val, 2)
            registry[tgt] = val
    all_values = 0
    for el in registry:
        all_values += registry[el]
    return all_values


def aoc_142():
    file = open('input14.txt', 'r')
    current_mask = ''
    registry = dict()
    floats = []
    for line in file:
        if line[:4] == 'mask':
            floats = []
            current_mask = (line[7:].strip('\n'))
            for i, c in enumerate(current_mask):
                if c == 'X':
                    floats.append(i)
        else:
            tgt_end = 0
            for i, el in enumerate(line):
                if el == ']':
                    tgt_end = i
            tgt = int(line[4:tgt_end])
            val = int(line[tgt_end + 4:])
            tgt = bin(tgt)
            tgt = tgt[2:]
            while len(tgt) < 36:
                tgt = '0' + tgt
            tmp = (2 ** len(floats))

            # create target - apply 1-masking
            for i, el in enumerate(tgt):
                if current_mask[i] == '1':
                    tgt = tgt[:i] + '1' + tgt[i + 1:]
                if current_mask[i] == 'X':
                    tgt = tgt[:i] + 'X' + tgt[i + 1:]

            # create combinations
            combinations = []
            for i in range(tmp):
                comb = bin(i)[2:]
                while len(comb) < len(floats):
                    comb = '0' + comb
                combinations.append(comb)

            # create targets
            targets = []
            for c in combinations:
                c_tgt = tgt
                for i, el in enumerate(floats):
                    c_tgt = c_tgt[:el] + c[i] + c_tgt[el + 1:]
                targets.append(int(c_tgt, 2))

            # write into dict
            for t in targets:
                registry[t] = val
    all_values = 0
    for el in registry:
        all_values += registry[el]
    return all_values


def aoc_151():
    nums = [1, 20, 8, 12, 0, 14]
    seen = [None] * 30000000
    last = nums[-1]
    for t, last in enumerate(nums):
        seen[last] = t + 1
    for i in range(len(nums), 30000000):
        seen[last], last = i, i - seen[last] if seen[last] is not None else 0
    return last
