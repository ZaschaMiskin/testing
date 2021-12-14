paths = []


def add_paths(path, connections, dup):
    """
    adds finished paths to global paths and follows paths in progress
    :param path: currently followed path
    :param connections: list of available connections (static)
    :param dup: current duplicate element for assignment 2 (static)
    :return: nothing i guess, maybe TODO: without global variables, ref. assignment 9
    """
    current = path[-1]
    part = 2  # which part of assignment
    if current == 'end':
        if path not in paths:
            paths.append(path)
            return
    for a, c in enumerate(connections):
        if c[0] == current and c[1] == dup and path.count(c[1]) < part:
            add_paths(path + [c[1]], connections, dup)
        elif c[0] == current and not (c[1] in path and c[1].islower()):
            add_paths(path + [c[1]], connections, dup)


def day12():
    file = open('inputs/input12.txt')
    connections = []
    for line in file:
        connections.append(line.strip().split('-'))
        connections.append(list(reversed(line.strip().split('-'))))
    lower_nodes = []
    for c in connections:
        c0 = c[0]
        c1 = c[1]
        if c0 not in lower_nodes and c0.islower() and c0 != 'start' and c0 != 'end':
            lower_nodes.append(c0)
        if c1 not in lower_nodes and c1.islower() and c1 != 'start' and c1 != 'end':
            lower_nodes.append(c1)

    for dup in lower_nodes:
        for i, c in enumerate(connections):
            if c[0] == 'start':
                path = connections[i]
                add_paths(path, connections, dup)
    return len(paths)


print(day11())
