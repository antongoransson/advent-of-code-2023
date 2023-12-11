from itertools import combinations
import sys
sys.path.append('..')


def dist(p1, p2):
    r1, c1 = p1
    r2, c2 = p2
    return abs(r1 - r2) + abs(c1 - c2)


def solve(g, size_factor):
    row_to_dup = []
    col_to_dup = []
    for r in range(len(g)):
        if all(g[r][c] == '.' for c in range(len(g[r]))):
            row_to_dup.append(r)
    for c in range(len(g[0])):
        if all(g[r][c] == '.' for r in range(len(g))):
            col_to_dup.append(c)
    points = []
    for i, r in enumerate(g):
        for j, c in enumerate(r):
            if c == '#':
                points.append((i, j))

    for r in row_to_dup[::-1]:
        for i, p in enumerate(points):
            if p[0] > r:
                points[i] = (p[0] + size_factor - 1, p[1])
    for c in col_to_dup[::-1]:
        for i, p in enumerate(points):
            if p[1] > c:
                points[i] = (p[0], p[1] + size_factor - 1)
    return sum(dist(p1, p2) for (p1, p2) in combinations(points, 2))


def solve_part_1(g):
    return solve(g, 2)


def solve_part_2(g):
    return solve(g, 1000000)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    g = []
    with open(in_f) as f:
        for r, l in enumerate(f.readlines()):
            g.append([v for v in l.strip()])

    sol1 = solve_part_1(g)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(g)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
