from collections import defaultdict
from math import inf
import heapq
from itertools import filterfalse
from timeit import default_timer

grid = []


def neighbors(r, c, height, width):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = (r + dr, c + dc)
        if 0 <= rr <= width and 0 <= cc <= height:
            yield rr, cc


def day15():
    file = open('inputs/input15.txt')
    for line in file:
        grid.append([int(x) for x in line.strip()])
    height, width = len(grid) - 1, len(grid) - 1
    visited = set()
    src = (0, 0)
    tgt = (height - 1, width - 1)
    minimum_distance = defaultdict(lambda: inf, {src: 0})
    q = [(0, src)]
    iterations = 0
    while q:
        iterations += 1
        dist, node = heapq.heappop(q)
        print(dist, node)
        if node == tgt:
            return dist
        if node in visited:
            continue
        visited.add(node)
        r, c = node
        ns = neighbors(r, c, height, width)
        ns2 = []
        for i in ns:
            if i not in visited:
                ns2.append(i)
        for neigh in ns2:
            nr, nc = neigh
            newdist = dist + grid[nr][nc]
            if newdist < minimum_distance[neigh]:
                minimum_distance[neigh] = newdist
                heapq.heappush(q, (newdist, neigh))
        if iterations == 10:
            return
    return inf


def day15_2():
    file = open('inputs/input15.txt')
    for line in file:
        grid.append([int(x) for x in line.strip()])

    tile_width = len(grid)
    tile_height = len(grid[0])
    for _ in range(4):
        for row in grid:
            tail = row[-tile_width:]
            row.extend((x + 1) if x < 9 else 1 for x in tail)

    for _ in range(4):
        for row in grid[-tile_height:]:
            row = [(x + 1) if x < 9 else 1 for x in row]
            grid.append(row)

    height, width = len(grid) - 1, len(grid) - 1
    visited = set()
    src = (0, 0)
    tgt = (height - 1, width - 1)
    minimum_distance = defaultdict(lambda: inf, {src: 0})
    q = [(0, src)]
    while q:
        dist, node = heapq.heappop(q)
        if node == tgt:
            return dist
        if node in visited:
            continue
        visited.add(node)
        r, c = node
        ns = neighbors(r, c, height, width)
        ns2 = []
        for i in ns:
            if i not in visited:
                ns2.append(i)
        for neigh in ns2:
            nr, nc = neigh
            newdist = dist + grid[nr][nc]
            if newdist < minimum_distance[neigh]:
                minimum_distance[neigh] = newdist
                heapq.heappush(q, (newdist, neigh))
    return inf


def try1():
    file = open('inputs/input15.txt')
    for line in file:
        grid.append([int(x) for x in line.strip()])
    Q = [[-1 for i in grid] for j in grid]
    Q[0][0] = 0
    q = [(0, 0)]
    pos = [0, 0]
    X = len(grid[0]) - 1
    Y = len(grid) - 1
    while pos != [X, Y]:
        neigh = []
        if pos[0] > 0:
            neigh.append((pos[0] - 1, pos[1]))
        if pos[0] < X:
            neigh.append((pos[0] + 1, pos[1]))
        if pos[1] > 0:
            neigh.append((pos[0], pos[1] - 1))
        if pos[1] < Y:
            neigh.append((pos[0], pos[1] + 1))
        for n in neigh:
            if n not in q and (Q[pos[0]][pos[1]] + grid[n[0]][n[1]] < Q[n[0]][n[1]] or Q[n[0]][n[1]] == -1):
                Q[n[0]][n[1]] = Q[pos[0]][pos[1]] + grid[n[0]][n[1]]
        min_i, min_j, min_el = 0, 0, 1000000
        for i, line in enumerate(Q):
            for j, el in enumerate(line):
                if 0 < el < min_el and (i, j) not in q:
                    min_i, min_j, min_el = i, j, el
        q.append((min_i, min_j))
        pos = [min_i, min_j]
        print(len(q))
    for l in Q:
        print(l)
    print(q, pos)
    return Q[-1][-1]


print(day15())
