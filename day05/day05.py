import sys
sys.path.append('..')
import aoc


def solve_part_1(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location):
    n = 10000000000
    for s in seeds:
        v = get_dest(s, seed_to_soil)
        v = get_dest(v, soil_to_fertilizer)
        v = get_dest(v, fertilizer_to_water)
        v = get_dest(v, water_to_light)
        v = get_dest(v, light_to_temperature)
        v = get_dest(v, temperature_to_humidity)
        v = get_dest(v, humidity_to_location)
        n = min(v, n)
    return n


def solve_part_2(seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location):
    s = get_seeds_range(seeds)
    # Brute forced by changing iteration steps
    for loc in range(59370080, 1000000000, 1):
        v = get_src(loc, humidity_to_location)
        v = get_src(v, temperature_to_humidity)
        v = get_src(v, light_to_temperature)
        v = get_src(v, water_to_light)
        v = get_src(v, fertilizer_to_water)
        v = get_src(v, soil_to_fertilizer)
        v = get_src(v, seed_to_soil)
        if is_in(v, s):
            return loc


def is_in(v, s_range):
    return any(s <= v <= s + r - 1 for s, r in s_range)


def get_dest(v, l):
    for m in l:
        if m['ss'] <= v <= m['ss'] + m['r'] - 1:
            return m['ds'] - m['ss'] + v
    return v


def get_src(v, l):
    for m in l:
        if m['ds'] <= v <= m['ds'] + m['r'] - 1:
            return m['ss'] - m['ds'] + v
    return v


def get_seeds_range(seeds):
    l = []
    for i in range(0, len(seeds), 2):
        l.append([seeds[i], seeds[i + 1]])
    return l


def get_map(inp):
    rows = inp.split(':\n')[1]
    l = []
    for r in rows.split('\n'):
        ds, ss, r = [int(x) for x in r.split()]
        m = {'ds': ds, 'ss': ss, 'r': r}
        l.append(m)
    return l


def main():
    in_f = sys.argv[1] if len(sys.argv) == 2 else 'in.txt'
    with open(in_f) as f:
        categories = f.read().split('\n\n')
        seeds = aoc.get_ints(categories[0])
        seed_to_soil = get_map(categories[1])
        soil_to_fertilizer = get_map(categories[2])
        fertilizer_to_water = get_map(categories[3])
        water_to_light = get_map(categories[4])
        light_to_temperature = get_map(categories[5])
        temperature_to_humidity = get_map(categories[6])
        humidity_to_location = get_map(categories[7])
    sol1 = solve_part_1(seeds,
                        seed_to_soil,
                        soil_to_fertilizer,
                        fertilizer_to_water,
                        water_to_light,
                        light_to_temperature,
                        temperature_to_humidity,
                        humidity_to_location)
    print(f'Part 1: {sol1}')

    sol2 = solve_part_2(seeds,
                        seed_to_soil,
                        soil_to_fertilizer,
                        fertilizer_to_water,
                        water_to_light,
                        light_to_temperature,
                        temperature_to_humidity,
                        humidity_to_location)
    print(f'Part 2: {sol2}')


if __name__ == "__main__":
    main()
