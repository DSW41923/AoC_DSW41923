import argparse


def is_space(x, y, offset):
    s = (x + y) * (x + y) + 3 * x + y + offset
    bin_s = bin(s)
    return bin_s.count('1') % 2 == 0


def step_forward(points, history_points, offset):
    new_points = []

    for point in points:
        possible_points = [(point[0] + p[0], point[1] + p[1]) for p in [(1, 0), (0, 1), (-1, 0), (0, -1)]]

        for p_x, p_y in possible_points:
            if p_x < 0 or p_y < 0:
                continue

            if is_space(p_x, p_y, offset):
                if (p_x, p_y) not in (new_points + history_points):
                    new_points.append((p_x, p_y))

    return new_points


def part_1(favorite_number):
    start = (1, 1)
    target = (31, 39)
    steps = 0
    front_points = [start]
    history_points = []

    while target not in front_points:
        new_points = step_forward(front_points, history_points, favorite_number)
        history_points.extend(front_points)
        front_points = new_points
        steps += 1

    print(steps)


def part_2(favorite_number):
    start = (1, 1)
    front_points = [start]
    history_points = []

    for steps in range(50):
        new_points = step_forward(front_points, history_points, favorite_number)
        history_points.extend(front_points)
        front_points = new_points

    print(len(history_points + front_points))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    favorite_number = 1350

    if args.part == '1':
        part_1(favorite_number)
    elif args.part == '2':
        part_2(favorite_number)
    else:
        part_1(favorite_number)
        part_2(favorite_number)


if __name__ == "__main__":
    main()
