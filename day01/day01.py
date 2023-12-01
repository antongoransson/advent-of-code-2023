import sys


def transform_text_numbers(a):
    for i in range(len(a)):
        x = a[i]
        x = x.replace('one', 'on1e')
        x = x.replace('two', 'two2')
        x = x.replace('three', 'thr3ee')
        x = x.replace('four', '4four')
        x = x.replace('five', '5five')
        x = x.replace('six', '6six')
        x = x.replace('seven', '7seven')
        x = x.replace('eight', 'ei8ght')
        x = x.replace('nine', 'ni9ne')
        a[i] = x
    return a


def get_numbers(l):
    c = [x for x in l]
    for i in range(len(c)):
        c[i] = [x for x in c[i] if x in ('01234567890')]
    return c


def solve_part_1(l):
    ns = get_numbers(l)
    return sum(int(str(n[0]) + str(n[-1])) for n in ns)


def solve_part_2(l):
    l = transform_text_numbers(l)
    ns = get_numbers(l)
    return sum(int(str(n[0]) + str(n[-1])) for n in ns)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        in_data = [l.strip() for l in f.readlines()]
    sol1 = solve_part_1(in_data)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(in_data)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
