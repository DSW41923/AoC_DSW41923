import argparse
import re


def get_min_x_velocity(x_min, x_max):
    v_x = 1
    while v_x * (v_x + 1) / 2 <= x_max:
        if x_min <= v_x * (v_x + 1) / 2:
            break
        v_x += 1

    return v_x


def probe_step(v_x, v_y, x_range, y_range, part):
    x_min, x_max = x_range
    y_min, y_max = y_range
    pos = [(0, 0)]
    velocity = (v_x, v_y)
    while pos[-1][0] <= x_max and pos[-1][1] >= y_min:
        pos.append((pos[-1][0] + velocity[0], pos[-1][1] + velocity[1]))
        velocity = (velocity[0] - 1, velocity[1] - 1) if velocity[0] > 0 else (0, velocity[1] - 1)
        if x_min <= pos[-1][0] <= x_max and y_max >= pos[-1][1] >= y_min:
            if part == 1:
                return max([p[1] for p in pos])

            if part == 2:
                return True

    if part == 1:
        return -1

    if part == 2:
        return False


def part_1(input_string):
    x_min, x_max, y_min, y_max = map(int, re.search(r'x=(\d+)\.\.(\d+), y=([-\d]+)\.\.([-\d]+)', input_string).groups())
    v_x = get_min_x_velocity(x_min, x_max)
    max_y = 0
    while v_x <= x_max:
        new_max_y = 0
        v_y = 1
        while v_y <= abs(y_min):
            high_y = probe_step(v_x, v_y, (x_min, x_max), (y_min, y_max), part=1)

            # Since min v_x is calculated, this check is not required.
            # if velocity[0] == 0 and pos[-1][0] < x_min:
            #     break

            if high_y:
                new_max_y = max(new_max_y, high_y)

            v_y += 1

        if new_max_y < max_y:
            break

        max_y = max(max_y, new_max_y)
        v_x += 1

    print(max_y)


def part_2(input_string):
    x_min, x_max, y_min, y_max = map(int, re.search(r'x=(\d+)\.\.(\d+), y=([-\d]+)\.\.([-\d]+)', input_string).groups())
    v_x = get_min_x_velocity(x_min, x_max)
    velocities = []
    while v_x <= x_max:
        v_y = y_min
        while v_y <= abs(y_min):
            will_in_area = probe_step(v_x, v_y, (x_min, x_max), (y_min, y_max), part=2)
            if will_in_area:
                velocities.append((v_x, v_y))
            v_y += 1

        v_x += 1

    print(len(velocities))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    input_string = "target area: x=153..199, y=-114..-75"

    if args.part == '1':
        part_1(input_string)
    elif args.part == '2':
        part_2(input_string)
    else:
        part_1(input_string)
        part_2(input_string)


if __name__ == "__main__":
    main()
