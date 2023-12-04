import sys
sys.path.append('..')
import aoc


def solve_part_1(in_data):
    s = 0
    for c in in_data:
        w, y = c
        y = aoc.get_ints(y)
        w = aoc.get_ints(w)
        ws = len(set(y) & set(w))
        if ws > 0:
            s += 2 ** (ws - 1)
    return s


def solve_part_2(in_data):
    wins = {}
    for i in range(len(in_data)):
        card = in_data[i]
        w, y = card
        y = aoc.get_ints(y)
        w = aoc.get_ints(w)
        ws = len(set(y) & set(w))
        wins[i] = ws
    cache = {}
    s = len(in_data)
    return s + sum(n_cards(c, wins, cache) for c in range(len(in_data)))


def n_cards(c, wins, cache):
    if c in cache:
        return cache[c]
    if wins[c] == 0:
        return 0
    n = sum(1 + n_cards(c + x + 1, wins, cache) for x in range(wins[c]))
    cache[c] = n
    return n


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        in_data = [l.strip().split(': ')[1].split('|') for l in f]
    sol1 = solve_part_1(in_data)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(in_data)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
