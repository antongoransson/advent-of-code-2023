import sys
sys.path.append('..')
import aoc

N = (-1, 0)
W = (0, -1)
E = (0, 1)
S = (1, 0)
DIRS = {'E': E, 'S': S, 'N': N, 'W': W}


def cant_move(grid, p, new_dir):
    if new_dir == 'E' and grid[p] == '<':
        return True
    if new_dir == 'W' and grid[p] == '>':
        return True
    if new_dir == 'S' and grid[p] == '^':
        return True
    if new_dir == 'N' and grid[p] == 'v':
        return True
    return False


def find_crossroads(grid):
    crossroads = set()
    for p in grid:
        neighbours = 0
        r, c = p
        for _, (dr, dc) in DIRS.items():
            nr, nc = r + dr, c + dc
            if (nr, nc) in grid:
                neighbours += 1
        if neighbours >= 3:
            crossroads.add((p))
    return crossroads


def find_connecting_crossroads(crossroad, crossroads, graph, grid, start, p1):
    visited = set([crossroad])
    q = [start]
    while q:
        current = q.pop()
        r, c = current
        visited.add(current)
        for direction, (dr, dc) in DIRS.items():
            nr, nc = r + dr, c + dc
            if (nr, nc) not in grid or (nr, nc) in visited:
                continue
            new_path = set(visited)
            if p1:
                if cant_move(grid, (nr, nc), direction):
                    continue
                while grid[nr, nc] in '<>^v':
                    if grid[nr, nc] == '>':
                        new_path = new_path | set([(nr, nc)])
                        nc += 1
                    if grid[nr, nc] == '<':
                        new_path = new_path | set([(nr, nc)])
                        nc -= 1
                    if grid[nr, nc] == 'v':
                        new_path = new_path | set([(nr, nc)])
                        nr += 1
                    if grid[nr, nc] == '^':
                        new_path = new_path | set([(nr, nc)])
                        nr -= 1
            if (nr, nc) in crossroads:
                graph[crossroad][nr, nc] = len(new_path)
                return
            q.append((nr, nc))


def dfs(grid, start, targets):
    visited = set([start])
    q = [start]
    while q:
        current = q.pop()
        r, c = current
        visited.add(current)
        for direction, (dr, dc) in DIRS.items():
            nr, nc = r + dr, c + dc
            if (nr, nc) not in grid or (nr, nc) in visited:
                continue
            if (nr, nc) in targets:
                return (nr, nc), len(visited)
            q.append((nr, nc))


def longest_path(graph, current, target, visited):
    if current == target:
        return 0
    visited[current] = True
    max_length = -1
    for n in graph[current]:
        if visited[n]:
            continue
        new_length = graph[current][n] + longest_path(graph, n, target, visited)
        max_length = max(max_length, new_length)
    visited[current] = False
    return max_length


def get_graph(crossroads, grid, p1):
    graph = {c: {} for c in crossroads}
    for crossroad in crossroads:
        r, c = crossroad
        for _, (dr, dc) in DIRS.items():
            nr, nc = r + dr, c + dc
            if (nr, nc) not in grid:
                continue
            find_connecting_crossroads(crossroad, crossroads, graph, grid, (nr, nc), p1)
    return graph


def solve(grid, p1):
    mr, mc = aoc.get_max_size(grid)
    start = [(0, c) for c in range(mc + 1) if (0, c) in grid and grid[0, c] == '.'][0]
    target = [(mr, c) for c in range(mc + 1) if (mr, c) in grid and grid[mr, c] == '.'][0]
    crossroads = find_crossroads(grid)
    graph = get_graph(crossroads, grid, p1)
    start_crossroad, start_l = dfs(grid, start, crossroads)
    end_crossroad, end_l = dfs(grid, target, crossroads)
    visited = {}
    for c in crossroads:
        visited[c] = False
    return longest_path(graph, start_crossroad, end_crossroad, visited) + start_l + end_l


def solve_part_1(grid):
    return solve(grid, True)


def solve_part_2(grid):
    return solve(grid, False)


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    grid = {}
    with open(in_f) as f:
        for r, l in enumerate(f.readlines()):
            for c, v in enumerate(l.strip()):
                if v != '#':
                    grid[r, c] = v
    sol1 = solve_part_1(grid)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(grid)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
