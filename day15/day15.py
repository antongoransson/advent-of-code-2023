from collections import defaultdict
import sys
sys.path.append('..')


def do_hash(s):
    current_v = 0
    for c in s:
        current_v = ((current_v + ord(c)) * 17) % 256
    return current_v


def solve_part_1(in_data):
    return sum(do_hash(c) for c in in_data.split(','))


def solve_part_2(in_data):
    commands = in_data.split(',')
    m = defaultdict(list)
    for command in commands:
        if '=' in command:
            label, v = command.split('=')
            sign = '='
        elif '-' in command:
            label, _ = command.split('-')
            sign = '-'
        h = do_hash(label)
        current = m[h]
        found = False
        if sign == '=':
            for i, label_maps in enumerate(current):
                if label_maps[0] == label:
                    current[i] = (label, v)
                    found = True
            if not found:
                current.append((label, v))
        if sign == '-':
            to_remove = None
            for i, label_maps in enumerate(current):
                if label_maps[0] == label:
                    del current[i]
    score = 0
    for box in m:
        for i, lens in enumerate(m[box]):
            score += (box + 1) * (i + 1) * int(lens[1])
    return score


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        in_data = f.read()
    sol1 = solve_part_1(in_data)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(in_data)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
