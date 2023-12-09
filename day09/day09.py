import sys
sys.path.append('..')
import aoc


def diffs(seq):
    return [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]


def get_diffs(seq):
    ad = [seq]
    while not all(x == 0 for x in seq):
        seq = diffs(seq)
        ad.append(seq)
    return ad


def solve_part_1(seqs):
    t = 0
    for seq in seqs:
        ad = get_diffs(seq)
        t += sum(ad[i][-1] for i in range(len(ad) - 2, -1, -1))
    return t


def solve_part_2(seqs):
    t = 0
    for seq in seqs:
        ad = get_diffs(seq)
        s = 0
        for i in range(len(ad) - 2, -1, -1):
            s = ad[i][0] - s
        t += s
    return t


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        seqs = [aoc.get_ints(l) for l in f.readlines()]
    sol1 = solve_part_1(seqs)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(seqs)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
