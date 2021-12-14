from collections import Counter


def day14():
    """
    just change iterations variable for stage
    :return: number of most occuring "pattern" - number of least occuring "pattern"
    """
    file = open('inputs/input14.txt')
    op = ""
    conn = dict()
    occ = Counter()

    for line in file:
        if line == "\n":
            break
        op = line.strip()
    for line in file:
        src, tgt = line.strip().split(' -> ')
        conn[src] = tgt
    for l in range(len(op) - 1):
        viewed = op[l:l + 2]
        occ[viewed] += 1
    for i in range(40):
        tmp = Counter()
        for el in occ:
            tmp[el[0] + conn[el]] += occ[el]
            tmp[conn[el] + el[1]] += occ[el]
            pass
        occ = tmp
    c = Counter()
    for el in occ:
        c[el[0]] += occ[el]
    c[op[-1]] += 1
    return max(c.values()) - min(c.values())



print(day14_2())
