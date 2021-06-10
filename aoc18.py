def calc2(expr):
    expr = ''.join(expr.split())

    while '+' in expr:
        for i, el in enumerate(expr):
            if el == '+':
                start, stop = 0, 0
                for j in range(i - 1, 0, -1):
                    if not expr[j].isnumeric():
                        start = j + 1
                        break
                for j in range(i + 1, len(expr)):
                    if not expr[j].isnumeric():
                        stop = j
                        break
                if stop == 0:
                    stop = len(expr)
                no1, no2 = int(expr[start:i]), int(expr[i + 1:stop])
                expr = expr[:start] + str(no1 + no2) + expr[stop:]
                break
    while '*' in expr:
        for i, el in enumerate(expr):
            if el == '*':
                start, stop = 0, 0
                for j in range(i - 1, 0, -1):
                    if not expr[j].isnumeric():
                        start = j + 1
                        break
                for j in range(i + 1, len(expr)):
                    if not expr[j].isnumeric():
                        stop = j
                        break
                if stop == 0:
                    stop = len(expr)
                no1, no2 = int(expr[start:i]), int(expr[i + 1:stop])
                expr = expr[:start] + str(no1 * no2) + expr[stop:]
                break
    return expr


def calc(expr):
    expr = ''.join(expr.split())
    while '+' in expr or '*' in expr:
        for i, el in enumerate(expr):
            if el == '+' or el == '*':
                no1 = int(expr[:i])
                stop = 0
                for j in range(i + 1, len(expr)):
                    if not expr[j].isnumeric():
                        stop = j
                        break
                if stop == 0:
                    stop = len(expr)
                no2 = int(expr[i + 1:stop])
                if el == '+':
                    expr = str(no1 + no2) + expr[stop:]
                    break
                if el == '*':
                    expr = str(no1 * no2) + expr[stop:]
                    break
    return expr


def aoc_181():
    out = 0
    file = open('input18.txt', 'r')
    for line in file:
        tmp_line = line
        while '(' in tmp_line:
            start, stop = 0, 0
            for i, el in enumerate(tmp_line):
                if el == '(':
                    start = i
                if el == ')':
                    stop = i
                    expr = tmp_line[start + 1:stop]
                    tmp_line = tmp_line[:start] + calc(expr) + tmp_line[stop + 1:]
                    break
        tmp_line = calc(tmp_line)
        out += int(tmp_line)
    return out


def aoc_182():
    out = 0
    file = open('input18.txt', 'r')
    for line in file:
        tmp_line = line
        while '(' in tmp_line:
            start, stop = 0, 0
            for i, el in enumerate(tmp_line):
                if el == '(':
                    start = i
                if el == ')':
                    stop = i
                    expr = tmp_line[start + 1:stop]
                    tmp_line = tmp_line[:start] + calc2(expr) + tmp_line[stop + 1:]
                    break
        tmp_line = calc2(tmp_line)
        out += int(tmp_line)
    return out