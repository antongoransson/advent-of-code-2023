from collections import defaultdict
from itertools import combinations, permutations, product
import regex as re
import sys
sys.path.append('..')
import aoc


def solve_part_1(ts, ds):
    ws = []
    s = 1
    for i in range(len(ts)):
        n = 0
        for t in range(ts[i]):
            sp = t
            if (ts[i] - t) * sp > ds[i]:
                n += 1
        s *= n
    return s


def solve_part_2(ts, ds):
    tt = int(''.join([str(t) for t in ts]))
    dd = int(''.join([str(d) for d in ds]))
    n = 0
    for t in range(tt):
        sp = t
        if (tt - t) * sp > dd:
            n += 1
    return n


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        a = f.read().split('\n')
        t = aoc.get_ints(a[0])
        d = aoc.get_ints(a[1])
    sol1 = solve_part_1(t, d)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(t, d)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
