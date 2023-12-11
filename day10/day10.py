from collections import defaultdict
from itertools import combinations, permutations, product
import regex as re
import sys
sys.path.append('..')
import aoc


def get_pipe(d1, d2):
    ds = set([d1, d2])
    if len(ds & set(['E', 'S'])) == 2:
        return 'F'
    elif len(ds & set(['N', 'S'])) == 2:
        return '|'
    if len(ds & set(['W', 'S'])) == 2:
        return '7'
    if len(ds & set(['W', 'N'])) == 2:
        return 'J'
    if len(ds & set(['E', 'N'])) == 2:
        return 'L'
    if len(ds & set(['W', 'E'])) == 2:
        return '-'
    assert False, f'{ds}'


def get_s_grid(grid):
    min_r = min(r for r, c in grid)
    max_r = max(r for r, c in grid)
    min_c = min(c for r, c in grid)
    max_c = max(c for r, c in grid)
    s = '\n'
    # for x in range(max_c + 2):
    #     s += str(x)
    # s += '\n'
    for r in range(max_r + 1):
        s += '0' * (r < 10) + '0' * (r < 100) + str(r) + ' |'
        for c in range(0, max_c + 1):
            # s += '#' if (r,c) in grid else '.'
            s += grid[r, c]
        s += '|\n'
    return s


def find_connected_pipes(p, g):
    r, c = p
    ps = []
    if g[r + 1, c] in '|LJ':
        ps.append(('S', (r + 1, c)))
    if g[r - 1, c] in '|F7':
        ps.append(('N', (r - 1, c)))
    if g[r, c + 1] in 'J7-':
        ps.append(('E', (r, c + 1)))
    if g[r, c - 1] in '-FL':
        ps.append(('W', (r, c - 1)))
    return ps


def traverse(d, p, g):
    pipe = g[p]
    if pipe == '|':
        assert d in ('N', 'S'), f'{d} {pipe}'
        if d == 'N':  # Going north
            new_p = (p[0] - 1, p[1])
        elif d == 'S':  # Going South
            new_p = (p[0] + 1, p[1])
    if pipe == '-':
        assert d in ('E', 'W'), f'{d} {pipe}'
        if d == 'E':  # Going east
            new_p = (p[0], p[1] + 1)
        elif d == 'W':  # Going West
            new_p = (p[0], p[1] - 1)
    if pipe == 'L':
        assert d in ('W', 'S'), f'{d} {pipe}'  # Going south or west
        if d == 'S':  # Going South
            new_p = (p[0], p[1] + 1)
            d = 'E'
        elif d == 'W':  # Going West
            new_p = (p[0] - 1, p[1])
            d = 'N'
    if pipe == 'J':
        assert d in ('E', 'S'), f'{d} {pipe}'  # Going south or east
        if d == 'S':  # Going South
            new_p = (p[0], p[1] - 1)
            d = 'W'
        elif d == 'E':  # Going East
            new_p = (p[0] - 1, p[1])
            d = 'N'
    if pipe == '7':
        assert d in ('N', 'E'), f'{d} {pipe}'  # Going North or east
        if d == 'N':  # Going North
            new_p = (p[0], p[1] - 1)
            d = 'W'
        elif d == 'E':  # Going East
            new_p = (p[0] + 1, p[1])
            d = 'S'
    if pipe == 'F':
        assert d in ('N', 'W'), f'{d} {pipe}'  # Going south or West
        if d == 'N':  # Going North
            new_p = (p[0], p[1] + 1)
            d = 'E'
        elif d == 'W':  # Going West
            new_p = (p[0] + 1, p[1])
            d = 'S'
    return d, new_p


def solve_part_1(s, g):
    ps = find_connected_pipes(s, g)
    m = {}
    for p in ps:
        d, cp = p
        m[cp] = {}
        t = 1
        while g[cp] != 'S':
            d, cp = traverse(d, cp, g)
            t += 1
            m[p[1]][cp] = t
    m1 = m[ps[0][1]]
    m2 = m[ps[1][1]]
    for p in m1:
        if m1[p] == m2[p]:
            return m1[p]
    assert False


def solve_part_2(s, g):
    ps = find_connected_pipes(s, g)
    m = {}
    for p in ps:
        d, cp = p
        m[cp] = {}
        t = 1
        while g[cp] != 'S':
            d, cp = traverse(d, cp, g)
            t += 1
            m[p[1]][cp] = s
    m1 = set(m[ps[1][1]]) | set(m[ps[0][1]])
    for p in g:
        if p not in m1:
            g[p] = '#'
    bigger_grid = {}
    max_r = max(r for r, c in g)
    max_c = max(c for r, c in g)
    d1, d2 = ps[0][0], ps[1][0]
    t = get_pipe(d1, d2)
    g[s] = t
    p_c = ' '
    o_c = '#'
    for r in range(max_r + 1):
        for c in range(max_c + 1):
            if (r, c) not in m1:
                bigger_grid[r * 3 + 0, c * 3 + 1] = o_c
                bigger_grid[r * 3 + 1, c * 3 + 1] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 1] = o_c
                bigger_grid[r * 3 + 0, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 0, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 1, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 1, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 2] = o_c
            elif g[r, c] == 'F':
                bigger_grid[r * 3 + 0, c * 3 + 1] = o_c
                bigger_grid[r * 3 + 1, c * 3 + 1] = p_c
                bigger_grid[r * 3 + 2, c * 3 + 1] = p_c
                bigger_grid[r * 3 + 1, c * 3 + 2] = p_c
                bigger_grid[r * 3 + 0, c * 3 + 2] = o_c

                bigger_grid[r * 3 + 0, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 1, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 2] = o_c
            elif g[r, c] == 'L':
                bigger_grid[r * 3 + 0, c * 3 + 1] = p_c
                bigger_grid[r * 3 + 1, c * 3 + 1] = p_c
                bigger_grid[r * 3 + 1, c * 3 + 2] = p_c

                bigger_grid[r * 3 + 2, c * 3 + 1] = o_c
                bigger_grid[r * 3 + 0, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 0, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 1, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 0] = o_c
            elif g[r, c] == '7':
                bigger_grid[r * 3 + 0, c * 3 + 1] = o_c
                bigger_grid[r * 3 + 1, c * 3 + 1] = p_c
                bigger_grid[r * 3 + 2, c * 3 + 1] = p_c
                bigger_grid[r * 3 + 1, c * 3 + 0] = p_c

                bigger_grid[r * 3 + 0, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 0, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 1, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 0] = o_c
            elif g[r, c] == 'J':
                bigger_grid[r * 3 + 0, c * 3 + 1] = p_c
                bigger_grid[r * 3 + 1, c * 3 + 1] = p_c
                bigger_grid[r * 3 + 1, c * 3 + 0] = p_c

                bigger_grid[r * 3 + 0, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 0, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 1, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 1] = o_c
            elif g[r, c] == '|':
                bigger_grid[r * 3 + 0, c * 3 + 1] = p_c
                bigger_grid[r * 3 + 1, c * 3 + 1] = p_c
                bigger_grid[r * 3 + 2, c * 3 + 1] = p_c

                bigger_grid[r * 3 + 0, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 0, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 1, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 1, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 0] = o_c
            elif g[r, c] == '-':
                bigger_grid[r * 3 + 1, c * 3 + 1] = p_c
                bigger_grid[r * 3 + 1, c * 3 + 0] = p_c
                bigger_grid[r * 3 + 1, c * 3 + 2] = p_c

                bigger_grid[r * 3 + 0, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 0, c * 3 + 1] = o_c
                bigger_grid[r * 3 + 0, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 2] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 0] = o_c
                bigger_grid[r * 3 + 2, c * 3 + 1] = o_c
    max_r = max(r for r, c in bigger_grid)
    max_c = max(c for r, c in bigger_grid)
    items = []
    for r in range(max_r + 1):
        for c in range(max_c + 1):
            if bigger_grid[r, c] == o_c:
                items.append((r, c))
    changed = True
    n_c = 0
    while changed:
        n_c += 1
        changed = False
        for i in items:
            if is_safe(i, bigger_grid):
                changed = True
                bigger_grid[i] = 'X'
        items = [x for x in items if not bigger_grid[x] == 'X']
    seen = set()
    t = 0
    for r in range(max_r + 1):
        for c in range(max_c + 1):
            is_square = True
            sq = set()
            for rr in range(3):
                for cc in range(3):
                    p = (r + rr, c + cc)
                    if p in seen:
                        is_square = False
                        continue
                    sq.add((r + rr, c + cc))
                    if not (p in bigger_grid and bigger_grid[p] == '#'):
                        is_square = False
            if is_square:
                t += 1
                seen |= sq
    return t


def is_safe(p, g):
    r, c = p
    for rr, cc in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        if (r + rr, cc + c) not in g or g[(r + rr, cc + c)] == 'X':
            return True


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        g = {}
        for i, r in enumerate(f.readlines()):
            for j, c in enumerate(r.strip()):
                g[i, j] = c
                if c == 'S':
                    s = (i, j)
    sol1 = solve_part_1(s, g)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(s, g)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
