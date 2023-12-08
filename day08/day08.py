import sys


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        lcm = lcm * arr[i] // gcd(lcm, arr[i])
    return lcm


def solve_part_1(ins, n_map):
    c_n = 'AAA'
    s = 0
    while c_n != 'ZZZ':
        for i in ins:
            e = 0 if i in 'L' else 1
            c_n = n_map[c_n][e]
            s += 1
    return s


def solve_part_2(ins, n_map):
    c_ns = [a for a in n_map if a.endswith('A')]
    s = 0
    fs = {}
    while any(not x.endswith('Z') for x in c_ns):
        for i in ins:
            e = 0 if i in 'L' else 1
            for j, c in enumerate(c_ns):
                if c.endswith('Z') and c not in fs:
                    fs[c] = s
                    if len(fs) == len(c_ns):
                        return lcm([x for x in fs.values()])
                c_ns[j] = n_map[c][e]
            s += 1
    return s


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    n_map = {}
    with open(in_f) as f:
        ins, nodes = f.read().split('\n\n')
        for l in nodes.split('\n'):
            n, e = l.split(" = ")
            e1, e2 = e.strip('()').split(', ')
            n_map[n] = (e1, e2)
    sol1 = solve_part_1(ins, n_map)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(ins, n_map)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
