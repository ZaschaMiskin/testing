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
    iterations = 40  # stage 1: 10   stage 2:40

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
    for i in range(iterations):
        tmp = Counter()
        for el in occ:
            tmp[el[0] + conn[el]] += occ[el]
            tmp[conn[el] + el[1]] += occ[el]
            pass
        occ = tmp
    # count first letter of every pattern + last letter of
    # origin word(will be last letter of finished word) to get every letter
    c = Counter()
    for el in occ:
        c[el[0]] += occ[el]
    c[op[-1]] += 1
    return max(c.values()) - min(c.values())


print(day14())
