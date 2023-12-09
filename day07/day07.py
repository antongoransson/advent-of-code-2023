from collections import defaultdict
from itertools import combinations, permutations, product
from functools import cmp_to_key
import regex as re
import sys
sys.path.append('..')
import aoc

VALUES_P1 = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
VALUE_MAP_P1 = {x: i for i, x in enumerate(VALUES_P1)}
VALUES_P2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
VALUE_MAP_P2 = {x: i for i, x in enumerate(VALUES_P2)}


def get_count(hand, p2=False):
    c = defaultdict(int)
    for x in hand:
        c[x] += 1
    if p2:
        m = get_c_to_add(c)
        if m is not None:
            v = [v for k, v in c.items() if k == 'J']
            if v:
                c[m] += v[0]
                del c['J']

    return c


def get_c_to_add(c):
    hv = [v for k, v in c.items() if k != 'J']
    if not hv:
        return None
    m = max(hv)
    ks = [k for k in c if c[k] == m]
    vs = max(VALUE_MAP_P2[x] for x in ks)
    k = [x for x in ks if VALUE_MAP_P2[x] == vs][0]
    return k


def noak(c, n):
    return any(n == x for x in c.values())


def fiveoak(c):
    return noak(c, 5)


def fouroak(c):
    return noak(c, 4)


def threeoak(c):
    return noak(c, 3)


def twooak(c):
    return noak(c, 2)


def two_pair(c):
    return len([x for x in c.values() if x == 2]) == 2


def get_type(c):
    if fiveoak(c):
        return 7
    if fouroak(c):
        return 6
    if threeoak(c) and twooak(c):
        return 5
    if threeoak(c):
        return 4
    if two_pair(c):
        return 3
    if twooak(c):
        return 2
    return 1


def compare_hands(h1, h2):
    c1, c2 = get_count(h1), get_count(h2)
    t1, t2 = get_type(c1), get_type(c2)
    if t1 == t2:
        for i in range(len(h1)):
            if VALUE_MAP_P1[h1[i]] > VALUE_MAP_P1[h2[i]]:
                return 1
            if VALUE_MAP_P1[h1[i]] < VALUE_MAP_P1[h2[i]]:
                return -1
    if t1 > t2:
        return 1
    if t1 < t2:
        return -1


def compare_hands_p2(h1, h2):
    c1, c2 = get_count(h1, True), get_count(h2, True)
    t1, t2 = get_type(c1), get_type(c2)
    print(h1, c1)
    print(h2, c2)
    print('-' * 100)
    if t1 == t2:
        for i in range(len(h1)):
            if VALUE_MAP_P2[h1[i]] > VALUE_MAP_P2[h2[i]]:
                return 1
            if VALUE_MAP_P2[h1[i]] < VALUE_MAP_P2[h2[i]]:
                return -1
    if t1 > t2:
        return 1
    if t1 < t2:
        return -1


def solve_part_1(hands, bids, hb):
    hands = sorted(hands, key=cmp_to_key(compare_hands), reverse=False)
    s = 0
    print(hands)
    for i, h in enumerate(hands):
        s += (i + 1) * hb[h]
        print(i + 1, hb[h])
    return s


def solve_part_2(hands, bids, hb):
    hands = sorted(hands, key=cmp_to_key(compare_hands_p2), reverse=False)
    s = 0
    print(hands)
    for i, h in enumerate(hands):
        s += (i + 1) * hb[h]
        print(i + 1, hb[h])
    return s


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    hands, bids = [], []
    hb = {}
    with open(in_f) as f:
        for l in f.readlines():
            h, b = l.split(' ')
            hands.append(h)
            hb[h] = int(b)
            bids.append(int(b))
    sol1 = solve_part_1(hands, bids, hb)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(hands, bids, hb)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
