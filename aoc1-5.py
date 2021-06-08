def aoc_11():
    file = open('input1.txt', 'r')
    numbers = []
    for line in file:
        numbers.append(int(line))
    for i, el1 in enumerate(numbers):
        for j, el2 in enumerate(numbers):
            tmp_sum = el1 + el2
            print(tmp_sum, i, j)
            if tmp_sum == 2020 and i != j:
                return el1 * el2


def aoc_12():
    file = open('input1.txt', 'r')
    numbers = []
    for line in file:
        numbers.append(int(line))
    for i, el1 in enumerate(numbers):
        for j, el2 in enumerate(numbers):
            for k, el3 in enumerate(numbers):
                tmp_sum = el1 + el2 + el3
                if tmp_sum == 2020 and i != j and i != k and j != k:
                    return el1 * el2 * el3


def aoc_21():
    file = open('input2.txt', 'r')
    out = 0
    for line in file:
        expr, text = line.split(':')
        num, letter = expr.split(' ')
        lbar, hbar = num.split('-')
        occ = text.count(letter)
        if int(lbar) <= occ <= int(hbar):
            out += 1
    return out


def aoc_22():
    file = open('input2.txt', 'r')
    out = 0
    for line in file:
        expr, text = line.split(':')
        num, letter = expr.split(' ')
        findex, sindex = num.split('-')
        findex = int(findex)
        sindex = int(sindex)
        if (text[findex] == letter) != (text[sindex] == letter):
            out += 1
    return out


def aoc_31():
    file = open('input3.txt', 'r')
    lines = file.readlines()
    pos = 0
    out = 0

    for line in lines[1:]:
        pos += 3
        pos %= len(line) - 1
        if line[pos] == '#':
            out += 1
    return out


def aoc_32():
    file = open('input3.txt', 'r')
    lines = file.readlines()
    pos = 0
    out = 0
    nums = []

    for line in lines[1:]:
        pos += 1
        pos %= len(line) - 1
        if line[pos] == '#':
            out += 1
    nums.append(out)
    out = 0
    pos = 0
    for line in lines[1:]:
        pos += 3
        pos %= len(line) - 1
        if line[pos] == '#':
            out += 1
    nums.append(out)
    out = 0
    pos = 0
    for line in lines[1:]:
        pos += 5
        pos %= len(line) - 1
        if line[pos] == '#':
            out += 1
    nums.append(out)
    out = 0
    pos = 0
    for line in lines[1:]:
        pos += 7
        pos %= len(line) - 1
        if line[pos] == '#':
            out += 1
    nums.append(out)
    out = 0
    pos = 0
    for line in lines[2::2]:
        pos += 1
        pos %= len(line) - 1
        if line[pos] == '#':
            out += 1
    nums.append(out)
    out = 1
    for n in nums:
        out *= n
    return out


def aoc_41():
    file = open('input4.txt', 'r')
    lines = file.readlines()
    out = 0
    customer = 0
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for line in lines:
        if line == '\n':
            customer += 1
            if len(keys) == 0:
                out += 1
            else:
                keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        info = line.split(' ')
        for i in info:
            relevant = i[:3]
            if relevant in keys:
                keys.remove(relevant)
    return out


def checkinvalidity(key, value):
    if key == 'byr':
        value = int(value)
        if value < 1920 or value > 2002:
            return True
    if key == 'iyr':
        value = int(value)
        if value < 2010 or value > 2020:
            return True
    if key == 'eyr':
        value = int(value)
        if value < 2020 or value > 2030:
            return True
    if key == 'hgt':
        startingindex = 0
        for i in range(len(value)):
            if not value[i].isnumeric():
                startingindex = i - 1
        if 'cm' in value:
            actual_value = value[:startingindex]
            actual_value = int(actual_value)
            if actual_value < 150 or actual_value > 193:
                return True
        if 'in' in value:
            actual_value = value[:startingindex]
            actual_value = int(actual_value)
            if actual_value < 59 or actual_value > 76:
                return True
    if key == 'hcl':
        if value[0] != '#':
            return True
        else:
            tmpval = value[1:]
            if len(tmpval) != 6:
                return True
            else:
                tolerated = '1234567890abcdef'
                for el in tmpval:
                    if el not in tolerated:
                        return True
    if key == 'ecl':
        if value != 'amb' and value != 'blu' and value != 'brn' and value != 'gry' and value != 'grn' and value != 'hzl' and value != 'oth':
            return True
    if key == 'pid':
        tolerated = '1234567890'
        if len(value) != 9:
            return True
        for el in value:
            if el not in tolerated:
                return True
    return False


def aoc_42():
    file = open('input4.txt', 'r')
    lines = file.readlines()
    out = 0
    customer = 0
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for line in lines:
        if line == '\n':
            customer += 1
            if len(keys) == 0:
                out += 1
            else:
                keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        else:
            info = line.split(' ')
            for i in info:
                key, value = i.split(':')
                value = value.strip('\n')
                if key in keys:
                    keys.remove(key)
                    if checkinvalidity(key, value):
                        keys.append('invalid')
    return out


def aoc_51():
    file = open('input5.txt', 'r')
    max_id = 0
    for line in file:
        base_y = [i for i in range(128)]
        base_x = [i for i in range(8)]
        for el in line:
            if el == 'F':
                base_y = base_y[:int(len(base_y) / 2)]
            if el == 'B':
                base_y = base_y[int(len(base_y) / 2):]
            if el == 'L':
                base_x = base_x[:int(len(base_x) / 2)]
            if el == 'R':
                base_x = base_x[int(len(base_x) / 2):]
        base_y = base_y[0]
        base_x = base_x[0]
        current_id = base_y * 8 + base_x
        if current_id > max_id:
            max_id = current_id


def aoc_52():
    file = open('input5.txt', 'r')
    ids = []
    for line in file:
        base_y = [i for i in range(128)]
        base_x = [i for i in range(8)]
        for el in line:
            if el == 'F':
                base_y = base_y[:int(len(base_y) / 2)]
            if el == 'B':
                base_y = base_y[int(len(base_y) / 2):]
            if el == 'L':
                base_x = base_x[:int(len(base_x) / 2)]
            if el == 'R':
                base_x = base_x[int(len(base_x) / 2):]
        base_y = base_y[0]
        base_x = base_x[0]
        current_id = base_y * 8 + base_x
        ids.append(current_id)
    ids = sorted(ids)
    for el in range(len(ids) - 1):
        if ids[el] + 2 == ids[el + 1]:
            return ids[el] + 1


print(aoc_12())
