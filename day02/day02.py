from collections import defaultdict
from itertools import combinations, permutations, product
import regex as re
import sys
sys.path.append('..')
import aoc


def solve_part_1(games):
    n_r, n_g, n_b = 12, 13, 14
    ss = 0
    for i, g in enumerate(games):
        sets = g.split(';')
        ok = True
        for s in sets:
            p = defaultdict(int)
            cubes = s.split(',')
            for c in cubes:
                if 'green' in c:
                    p['g'] = aoc.get_ints(c)[0]
                elif 'red' in c:
                    p['r'] = aoc.get_ints(c)[0]
                elif 'blue' in c:
                    p['b'] = aoc.get_ints(c)[0]
            if not (p['g'] <= n_g and p['r'] <= n_r and p['b'] <= n_b):
                ok = False
        if ok:
            ss += i + 1
    return ss


def solve_part_2(games):
    n_r, n_g, n_b = 12, 13, 14
    ss = 0
    for i, g in enumerate(games):
        sets = g.split(';')
        p = defaultdict(int)
        for s in sets:
            cubes = s.split(',')
            for c in cubes:
                if 'green' in c:
                    p['g'] = max(aoc.get_ints(c)[0], p['g'])
                elif 'red' in c:
                    p['r'] = max(aoc.get_ints(c)[0], p['r'])
                elif 'blue' in c:
                    p['b'] = max(aoc.get_ints(c)[0], p['b'])
        ss += p['g'] * p['b'] * p['r']
    return ss


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        in_data = [l.strip().split(': ')[1] for l in f]
    sol1 = solve_part_1(in_data)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(in_data)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
