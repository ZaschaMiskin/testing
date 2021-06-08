def aoc_61():
    file = open('input6.txt', 'r')
    lines = file.readlines()
    occ = []
    out = 0
    for line in lines:
        if line == '\n':
            out += len(set(occ))
            occ = []
        else:
            line = line.strip('\n')
            for el in line:
                occ.append(el)
    return out


def aoc_62():
    file = open('input6.txt', 'r')
    lines = file.readlines()
    occ = []
    out = 0
    for line in lines:
        if line == '\n':
            # out += len(set(occ))
            for check_item in occ[0]:
                item_all = True
                for array in occ:
                    if check_item not in array:
                        item_all = False
                if item_all:
                    out += 1
            occ = []
        else:
            line = line.strip('\n')
            tmp = []
            for el in line:
                tmp.append(el)
            occ.append(tmp)
    return out


# found = [] for 7_1
found = 0


def search_for(expression, src, target):
    """
    searches for expression in target and matches with src. A recursive function
    :param expression: The required expression
    :param src: Source
    :param target: Target
    :return: List of found elements that can contain original expression
    """
    expr = ""
    for i, el_i in enumerate(target):
        for el_j in el_i:
            if el_j == expression:  # and el_j not in found:
                expr = src[i]
                found.append(expr)
                search_for(expr, src, target)


def aoc_71():
    file = open('input7.txt', 'r')
    lines = file.readlines()
    src = []
    target = []
    for line in lines:
        info = line.split(' ')
        info.append('')
        src.append(info[0] + ' ' + info[1])
        info = info[4:]
        for el in info:
            if 'bag' in el:
                info.remove(el)
        tmp = []
        complete = ''
        for i, el in enumerate(info):
            if i % 3 == 0:
                if i == 0:
                    complete = el + ','
                else:
                    complete = complete[:-1]
                    tmp.append(complete.split(','))
                    complete = el + ','
            else:
                complete += (el + ' ')
        for i in range(len(tmp)):
            tmp[i] = tmp[i][1]
        target.append(tmp)

    search_for('shiny gold', src, target)
    global found
    found = list(set(found))
    return len(found)


def search_for_72(expression, src, target, tgt_amt):
    out = 0
    for i, src_el in enumerate(src):
        if src_el == expression:
            if len(target[i]) != 0:
                for j, tgt_el in enumerate(target[i]):
                    out += tgt_amt[i][j] + search_for_72(tgt_el, src, target, tgt_amt) * tgt_amt[i][j]
                else:
                    return out
            else:
                return 1


def aoc_72():
    file = open('input7.txt', 'r')
    lines = file.readlines()
    src = []
    target = []
    tgt_amt = []
    for line in lines:
        info = line.split(' ')
        info.append('')
        src.append(info[0] + ' ' + info[1])
        info = info[4:]
        for el in info:
            if 'bag' in el:
                info.remove(el)
        tmp = []
        complete = ''
        for i, el in enumerate(info):
            if i % 3 == 0:
                if i == 0:
                    complete = el + ','
                else:
                    complete = complete[:-1]
                    tmp.append(complete.split(','))
                    complete = el + ','
            else:
                complete += (el + ' ')
        tgt_tmp = tmp.copy()
        tgt_amt_tmp = tmp.copy()
        for i in range(len(tmp)):
            tgt_tmp[i] = tmp[i][1]
            tgt_amt_tmp[i] = int(tmp[i][0])
        target.append(tgt_tmp)
        tgt_amt.append(tgt_amt_tmp)
    out = search_for_72('shiny gold', src, target, tgt_amt)
    return out


def aoc_81():
    file = open('input8.txt', 'r')
    current_line = 0
    out = 0
    commands = []
    lines = file.readlines()
    for i, line in enumerate(lines):
        line = line.strip('\n')
        lines[i] = line.split(' ')
        lines[i][1] = int(lines[i][1])
    while current_line not in commands:
        commands.append(current_line)
        comm = lines[current_line][0]
        num = lines[current_line][1]
        if comm == 'acc':
            out += num
            current_line += 1
        elif comm == 'nop':
            current_line += 1
        elif comm == 'jmp':
            current_line += num

    return out


def completes(lines):
    current_line = 0
    out = 0
    commands = []
    while current_line not in commands:
        commands.append(current_line)
        comm = lines[current_line][0]
        num = lines[current_line][1]
        if comm == 'acc':
            out += num
            current_line += 1
        elif comm == 'nop':
            current_line += 1
        elif comm == 'jmp':
            current_line += num
        if current_line == 604:
            return out, commands, True
    return out, commands, False


def aoc_82():
    file = open('input8.txt', 'r')
    current_line = 0
    lines = file.readlines()
    for i, line in enumerate(lines):
        line = line.strip('\n')
        lines[i] = line.split(' ')
        lines[i][1] = int(lines[i][1])
    lines_copy = lines.copy()
    out, commands, finished = completes(lines)
    for c in commands:
        if lines_copy[c][0] == 'nop':
            lines[c][0] = 'jmp'
            out, _, finished = completes(lines)
            if finished:
                return out
            lines[c][0] = 'nop'
        if lines_copy[c][0] == 'jmp':
            lines[c][0] = 'nop'
            out, _, finished = completes(lines)
            if finished:
                return out
            lines[c][0] = 'jmp'
    return 'not found'


def aoc_91():
    file = open('input9.txt', 'r')
    nums = file.readlines()
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    for i, num in enumerate(nums):
        if i > 24:
            prev = []
            for j in range(i - 25, i):
                prev.append(nums[j])
            combination_found = False
            for a in prev:
                for b in prev:
                    if a != b:
                        if a + b == num:
                            combination_found = True
            if not combination_found:
                return num


def aoc_92():
    file = open('input9.txt', 'r')
    nums = file.readlines()
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    current_sum, start, current_line = 0, 0, 0
    while current_sum != 3199139634:
        current_sum += nums[current_line]
        current_line += 1
        if current_sum > 3199139634:
            current_sum = 0
            start += 1
            current_line = start
        if current_line == 999:
            print('didnt find')
    found_range = nums[start:current_line + 1]
    return min(found_range) + max(found_range)


def aoc_101():
    nums = []
    ones, threes = 0, 0
    file = open('input10.txt', 'r')
    lines = file.readlines()
    for num in lines:
        num = num.strip('\n')
        nums.append(int(num))
    nums = sorted(nums)
    for i, el in enumerate(nums):
        if i > 0:
            if el == nums[i - 1] + 1:
                ones += 1
            if el == nums[i - 1] + 3:
                threes += 1
        else:
            if el == 1:
                ones += 1
            if el == 3:
                threes += 1
    threes += 1
    return ones * threes

