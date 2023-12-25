import sys
sys.path.append('..')
import aoc

DIRS = ['N', 'W', 'S', 'E']


def get_rocks(d, rocks, i):
    if d in 'NS':
        return [r for r in rocks if r[1] == i]
    if d in 'WE':
        return [r for r in rocks if r[0] == i]
    assert False, f'{d}'.format(d)


def compare_rock(d):
    if d == 'N':
        return lambda r, rock: r[0] < rock[0]
    if d == 'W':
        return lambda r, rock: r[1] < rock[1]
    if d == 'S':
        return lambda r, rock: r[0] > rock[0]
    if d == 'E':
        return lambda r, rock: r[1] > rock[1]


def select_function(d):
    if d == 'N':
        return lambda r, rock: max(r, rock, key=lambda x: x[0])
    if d == 'W':
        return lambda r, rock: max(r, rock, key=lambda x: x[1])
    if d == 'S':
        return lambda r, rock: min(r, rock, key=lambda x: x[0])
    if d == 'E':
        return lambda r, rock: min(r, rock, key=lambda x: x[1])


def get_blocking_rock(d, rock, rocks):
    comp = compare_rock(d)
    target_rock = None
    s_function = select_function(d)
    for r in rocks:
        if comp(r, rock):
            target_rock = r if target_rock is None else s_function(target_rock, r)
    return target_rock


def handle_rock(d, rock, i, size, new_round_rocks, cube_line_rocks):
    blocking_rock = get_blocking_rock(d, rock, cube_line_rocks + new_round_rocks)
    if not blocking_rock:
        if d == 'N':
            return (0, i)
        if d == 'S':
            return (size - 1, i)
        if d == 'W':
            return (i, 0)
        if d == 'E':
            return (i, size - 1)
        assert False
    else:
        if d == 'N':
            return (blocking_rock[0] + 1, i)
        if d == 'S':
            return (blocking_rock[0] - 1, i)
        if d == 'W':
            return (i, blocking_rock[1] + 1)
        if d == 'E':
            return (i, blocking_rock[1] - 1)
        assert False


def tilt(d, size, round_rocks, cube_rocks):
    all_new_round_rocks = []
    for i in range(size):
        round_line_rocks = get_rocks(d, round_rocks, i)
        cube_line_rocks = get_rocks(d, cube_rocks, i)
        new_round_rocks = []
        if d in 'NW':
            for rock in round_line_rocks:
                new_rock = handle_rock(d, rock, i, size, new_round_rocks, cube_line_rocks)
                new_round_rocks.append(new_rock)
        elif d in 'SE':
            for rock in reversed(round_line_rocks):
                new_rock = handle_rock(d, rock, i, size, new_round_rocks, cube_line_rocks)
                new_round_rocks.append(new_rock)
        all_new_round_rocks += new_round_rocks
    return all_new_round_rocks


def solve_part_1(round_rocks, cube_rocks, rows):
    score = 0
    round_rocks = tilt('N', rows, round_rocks, cube_rocks)
    for rock in round_rocks:
        score += rows - rock[0]
    return score


def solve_part_2(round_rocks, cube_rocks, rows):
    new_round_rocks = round_rocks
    states = [[x for x in new_round_rocks]]
    for c in range(1000000000):
        for d in DIRS:
            new_round_rocks = tilt(d, rows, new_round_rocks, cube_rocks)
        repeats = [c + 1]
        for i, s in enumerate(states):
            if all(x in s for x in new_round_rocks):
                repeats.append(i)
        states.append(set(new_round_rocks))
        if len(repeats) > 1:
            end, start = repeats
            diff = end - start
            for k in range(diff):
                if (1000000000 - start - k) % diff == 0:
                    score = 0
                    for rock in states[start + k]:
                        score += rows - rock[0]
                    return score


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in .txt'
    round_rocks = []
    cube_rocks = []
    rows = 0
    with open(in_f) as f:
        for r, l in enumerate(f.readlines()):
            rows += 1
            for c, v in enumerate(l.strip()):
                if v == '#':
                    cube_rocks.append((r, c))
                elif v == 'O':
                    round_rocks.append((r, c))
    sol1 = solve_part_1(round_rocks, cube_rocks, rows)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(round_rocks, cube_rocks, rows)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
