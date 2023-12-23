from collections import defaultdict, deque
import sys
sys.path.append('..')
import aoc
import heapq

N = (-1, 0)
W = (0, -1)
E = (0, 1)
S = (1, 0)
DIRS = {'E': E, 'S': S, 'N': N, 'W': W}


def dir_rule(is_p2):
    if is_p2:
        return lambda new_k, direction, n_dir: new_k == direction and n_dir == 10 or direction != 'X' and new_k != direction and n_dir < 4
    return lambda new_k, direction, n_dir: new_k == direction and n_dir == 3


def dijkstra(grid, start, target, is_p2):
    rs, cs = start
    dists = defaultdict(lambda: float('inf'))
    q = [(0, start, 'X', 0)]

    while q:
        item = heapq.heappop(q)
        cost, current, direction, n_dir = item
        cr, cc = current
        # print(item)
        for new_k, (dr, dc) in DIRS.items():
            nr, nc = cr + dr, cc + dc
            if (new_k == 'N' and direction == 'S') or (new_k == 'S' and direction == 'N') or (new_k == 'W' and direction == 'E') or (new_k == 'E' and direction == 'W'):
                continue
            if (nr, nc) not in grid:
                continue
            rule = dir_rule(is_p2)
            if rule(new_k, direction, n_dir):
                continue
            new_cost = grid[nr, nc] + cost
            if new_k == direction:
                new_dir = n_dir + 1
            else:
                new_dir = 1
            if (nr, nc) == target:
                return new_cost

            key = (nr, nc, new_k, new_dir)
            new_item = (new_cost, (nr, nc), new_k, new_dir)
            if new_cost < dists[key]:
                dists[key] = new_cost
                heapq.heappush(q, new_item)


def solve_part_1(grid):
    mr, mc = aoc.get_max_size(grid)
    return dijkstra(grid, (0, 0), (mr, mc), False)


def solve_part_2(grid):
    mr, mc = aoc.get_max_size(grid)
    print(mr, mc)
    return dijkstra(grid, (0, 0), (mr, mc), True)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    grid = {}
    with open(in_f) as f:
        for r, l in enumerate(f.readlines()):
            for c, v in enumerate(l.strip()):
                grid[r, c] = int(v)
    sol1 = solve_part_1(grid)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(grid)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
