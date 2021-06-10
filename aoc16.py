def aoc_161():
    file = open('input16.txt', 'r')
    bounds = []
    stage = 1
    out = 0
    for line in file:
        if line == '' or line == '\n':
            continue
        if line.split(' ')[0] == 'your':
            stage = 2
            continue
        if line.split(' ')[0] == 'nearby':
            stage = 3
            continue
        if stage == 1:
            line = line.strip('\n')
            info = (line.split(':')[1]).split(' ')[1:]
            info = info[:1] + info[2:]
            for i in info:
                bounds.append(i.split('-'))
        if stage == 3:
            line = (line.strip('\n')).split(',')
            for el in line:
                el = int(el)
                for b in bounds:
                    if int(b[0]) <= el <= int(b[1]):
                        break
                    if int(b[0]) == 463 and int(b[1]) == 969:
                        out += int(el)
    return out
