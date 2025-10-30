import argparse

from math import inf, gcd


def parse_data(input_string):
    region_map = list(map(list, input_string.split('\n')))
    y_range = len(region_map)
    x_range = len(region_map[0])
    asteroids = []
    for y in range(y_range):
        for x in range(x_range):
            if region_map[y][x] == '#':
                asteroids.append((y, x))
    return asteroids


def get_monitor_location(asteroids):
    max_count = 0
    monitor_location = None
    for a in asteroids:
        vectors = set()
        for o in asteroids:
            if o != a:
                vec = (o[0]-a[0], o[1]-a[1])
                while gcd(abs(vec[0]), abs(vec[1])) > 1:
                    vec_gcd = gcd(abs(vec[0]), abs(vec[1]))
                    vec = (vec[0]//vec_gcd, vec[1]//vec_gcd)
                vectors.add(vec)
        vectors_count = len(vectors)
        if vectors_count > max_count:
            max_count = vectors_count
            monitor_location = a
    return max_count, monitor_location


def manhatton_distance(p_0, p_1):
    return sum([abs(a - b) for a, b in zip(p_0, p_1)])


def part_1(input_string):
    asteroids = parse_data(input_string)
    max_count, _ = get_monitor_location(asteroids)
    print(max_count)


def part_2(input_string):
    asteroids = parse_data(input_string)
    _, monitor_location = get_monitor_location(asteroids)
    asteroids_direction_r = []
    asteroids_direction_l = []
    for a in asteroids:
        if a != monitor_location:
            vec = (a[0]-monitor_location[0], a[1]-monitor_location[1])
            while gcd(abs(vec[0]), abs(vec[1])) > 1:
                vec_gcd = gcd(abs(vec[0]), abs(vec[1]))
                vec = (vec[0]//vec_gcd, vec[1]//vec_gcd)
            if vec[1] > 0 or (vec[0] < 0 and vec[1] == 0):
                asteroids_direction_r.append((a, vec))
            if vec[1] < 0 or (vec[0] > 0 and vec[1] == 0):
                asteroids_direction_l.append((a, vec))
    asteroids_direction_r.sort(key=lambda ad: -ad[1][0]/((ad[1][0]**2+ad[1][1]**2)**0.5), reverse=True)
    asteroids_direction_l.sort(key=lambda ad: -ad[1][0]/((ad[1][0]**2+ad[1][1]**2)**0.5))
    asteroids_direction = asteroids_direction_r + asteroids_direction_l
    destory_order = [[(asteroids_direction[0])]]
    for a, v in asteroids_direction[1:]:
        if destory_order[-1][-1][1] == v:
            destory_order[-1].append((a, v))
            continue
        destory_order.append([(a, v)])
    for d in destory_order:
        if len(d) > 1:
            d.sort(key=lambda d: manhatton_distance(d[0], monitor_location))
    destory_count = 0
    while destory_count < 200:
        for d in destory_order:
            destoryed = None
            if len(d) > 0:
                destoryed = d.pop(0)
                destory_count += 1
            if destoryed and destory_count == 200:
                print(destoryed[0][1]*100+destoryed[0][0])
                break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_10.txt', 'r')
    input_string = file_input.read()
    file_input.close()

    if args.part == '1':
        part_1(input_string)
    elif args.part == '2':
        part_2(input_string)
    else:
        part_1(input_string)
        part_2(input_string)


if __name__ == "__main__":
    main()
