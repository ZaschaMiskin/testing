from collections import defaultdict, Counter
import sys


def day21():
    file = open("inputs/input21.txt")
    p1, p2 = 0, 0
    p1_score, p2_score = 0, 0
    for line in file:
        data = line.strip().split()
        data = data[4]
        if p1:
            p2 = int(data)
        else:
            p1 = int(data)
    current = 1
    total_rolls = 0
    turn1 = True
    roll = 0
    while p1_score < 1000 and p2_score < 1000:
        if turn1:
            roll += 1
            p1 += current % 100
            if current % 100 == 0:
                p1 += 100
            if roll == 3:
                roll = 0
                p1 %= 10
                if p1 == 0:
                    p1 = 10
                total_rolls += 3
                p1_score += p1
                turn1 = False
        else:
            roll += 1
            p2 += current % 100
            if current % 100 == 0:
                p2 += 100
            if roll == 3:
                roll = 0
                p2 %= 10
                if p2 == 0:
                    p2 = 10
                total_rolls += 3
                p2_score += p2
                turn1 = True
        current += 1
        if current == 101:
            current = 1
    return total_rolls, p1_score, p2_score


def day21_2():
    ll = [int(x.split(": ")[1]) for x in open("inputs/input21.txt").read().strip().split('\n')]
    print(ll)
    dice = list(Counter(i + j + k for i in range(1, 4) for j in range(1, 4) for k in range(1, 4)).items())
    universes = {(0, ll[0], 0, ll[1]): 1}
    p1wins, p2wins = 0, 0
    while universes:
        nuv = defaultdict(int)
        for state, cnt in list(universes.items()):
            score1, pos1, score2, pos2 = state
            for d, dcount in dice:
                p1 = (pos1 + d - 1) % 10 + 1
                s1 = score1 + p1
                if s1 >= 21:
                    p1wins += cnt * dcount
                    continue
                for d2, d2count in dice:
                    p2 = (pos2 + d2 - 1) % 10 + 1
                    s2 = score2 + p2
                    if s2 >= 21:
                        p2wins += cnt * dcount * d2count
                        continue
                    nuv[(s1, p1, s2, p2)] += cnt * dcount * d2count
        universes = nuv
    return max([p1wins, p2wins])


print(day21_2())
