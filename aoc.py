import regex as re


def get_max_size(grid):
    max_c = max(x for x, y in grid)
    max_r = max(y for x, y in grid)
    return max_r, max_c


def get_s_grid(grid):
    min_c = min(x for x, y in grid)
    max_c = max(x for x, y in grid)
    min_r = min(y for x, y in grid)
    max_r = max(y for x, y in grid)
    s = '\n'
    for y in range(max_r + 2, -1, -1):
        s += str(y) + ' |'
        for x in range(0, 7):
            s += '#' if (x, y) in grid else '.'
        s += '|\n'
    return s


def neighbours(grid, p, diag=False):
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if diag:
        deltas += [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    x, y = p
    neigbours = set()
    for dx, dy in deltas:
        xx = x + dx
        yy = y + dy
        if (xx, yy) in grid:
            neigbours.add((xx, yy))
    return neigbours


def get_ints(s, sign=True):
    if sign:
        return list(map(int, re.findall(r'-?\d+', s)))
    else:
        return list(map(int, re.findall(r'\d+', s)))
