from collections import defaultdict
from itertools import combinations, permutations, product
import regex as re
import sys
sys.path.append('..')
import aoc


def is_part_number(grid, p):
    neigbours = aoc.neighbours(grid, p, True)
    return any(grid[n] not in '1234567890.' for n in neigbours)


def solve_part_1(grid):
    max_r, max_c = aoc.get_max_size(grid)
    s = 0
    for r in range(max_r + 1):
        c = 0
        while c <= max_c:
            p = (r, c)
            if grid[p] in '1234567890' and is_part_number(grid, p):
                n = grid[p]
                n_p = (r, c - 1)
                while n_p in grid and grid[n_p] in '1234567890':
                    n = grid[n_p] + n
                    n_p = (r, n_p[1] - 1)
                n_p = (r, c + 1)
                while n_p in grid and grid[n_p] in '1234567890':
                    n = n + grid[n_p]
                    n_p = (r, n_p[1] + 1)
                print(n, p)
                s += int(n)
                c = max(c + 1, n_p[1])
            else:
                c += 1
    return s


def solve(grid, p):
    neigbours = aoc.neighbours(grid, p, True)
    ns = [n for n in neigbours if grid[n] in '1234567890']
    numbers = set(find_number(grid, n) for n in ns)
    if len(numbers) == 2:
        x, y = numbers
        print(x, y)
        return int(x) * int(y)
    return 0


def find_number(grid, p):
    n = grid[p]
    r, c = p
    n_p = (r, c - 1)
    while n_p in grid and grid[n_p] in '1234567890':
        n = grid[n_p] + n
        n_p = (r, n_p[1] - 1)
    n_p = (r, c + 1)
    while n_p in grid and grid[n_p] in '1234567890':
        n = n + grid[n_p]
        n_p = (r, n_p[1] + 1)
    return n


def solve_part_2(grid):
    max_r, max_c = aoc.get_max_size(grid)
    s = 0
    for r in range(max_r + 1):
        c = 0
        while c <= max_c:
            p = (r, c)
            if grid[p] == '*':
                n = grid[p]
                s += solve(grid, p)
            c += 1
    return s


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        grid = {}
        for i, r in enumerate(f.readlines()):
            for j, c in enumerate(r.strip()):
                grid[i, j] = c
    sol1 = solve_part_1(grid)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(grid)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
