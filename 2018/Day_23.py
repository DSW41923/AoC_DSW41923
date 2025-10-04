import argparse
import re

from itertools import product


def manhatton_distance(p_0, p_1):
    return sum([abs(a - b) for a, b in zip(p_0, p_1)])


def parse_data(input_string):
    nanobots = []
    for x, y, z, r in re.findall(r"pos=<([\d-]+),([\d-]+),([\d-]+)>, r=(\d+)", input_string):
        nanobots.append(tuple(map(int, (x, y, z, r))))
    return nanobots


def get_max_overlap(nanobots, index):
    min_range, max_range = min([b[index] for b in nanobots]), max([b[index] for b in nanobots])
    bot_ranges = [(bot[index]-bot[-1], bot[index]+bot[-1]) for bot in nanobots]
    while (max_range - min_range) > 2:
        left, right = 0, 0
        mid = (min_range + max_range) // 2
        for bot_range in bot_ranges:
            if bot_range[0] <= mid:
                left += 1
            if mid <= bot_range[1]:
                right += 1
        # print(left, mid, right)
        if left > right:
            max_range = mid
        elif right > left:
            min_range = mid
        else:
            break
    return min_range, max_range


def get_dot_count(box):
    return (box[0][1]-box[0][0]+1)*(box[1][1]-box[1][0]+1)*(box[2][1]-box[2][0]+1)


def part_1(input_string):
    nanobots = parse_data(input_string)
    nanobots.sort(key=lambda b: b[-1], reverse=True)
    print(len([bot for bot in nanobots if manhatton_distance(nanobots[0][:-1], bot[:-1]) <= nanobots[0][-1]]))


def part_2(input_string):
    nanobots = parse_data(input_string)
    x_range = (min([b[0] for b in nanobots]), max([b[0] for b in nanobots]))
    y_range = (min([b[1] for b in nanobots]), max([b[1] for b in nanobots]))
    z_range = (min([b[2] for b in nanobots]), max([b[2] for b in nanobots]))
    large_range = 2
    while large_range < x_range[1]:
        large_range *= 2
    box = (x_range, y_range, z_range)
    boxes = [((-large_range+1, large_range), (-large_range+1, large_range), (-large_range+1, large_range))]
    while boxes:
        new_boxes = []
        for box in boxes:
            x_range, y_range, z_range = box
            x_mid = (x_range[0] + x_range[1]) // 2
            y_mid = (y_range[0] + y_range[1]) // 2
            z_mid = (z_range[0] + z_range[1]) // 2
            box_volume = 0
            for i in range(8):
                new_x_range = (x_range[0], x_mid)
                if i >= 4:
                    new_x_range = (x_mid+1, x_range[1])
                new_y_range = (y_range[0], y_mid)
                if i % 4 >= 2:
                    new_y_range = (y_mid+1, y_range[1])
                new_z_range = (z_range[0], z_mid)
                if i % 2 == 1:
                    new_z_range = (z_mid+1, z_range[1])
                new_mid = ((new_x_range[0] + new_x_range[1]) / 2, (new_y_range[0] + new_y_range[1]) / 2, (new_z_range[0] + new_z_range[1]) / 2)
                r = (new_x_range[1]-new_x_range[0])/2
                in_range_count = 0
                for bot in nanobots:
                    ti = tuple([bot[i]-new_mid[i] for i in range(3)])
                    check = sum([max(0, abs(ti[i])-r) for i in range(3)])
                    if check <= bot[-1]:
                        in_range_count += 1
                new_boxes.append((new_x_range, new_y_range, new_z_range, in_range_count))
        new_boxes.sort(key=lambda b: b[-1], reverse=True)
        if len([b for b in new_boxes if b[-1] == new_boxes[0][-1]]) == 1:
            boxes = [new_boxes[0][:-1]]
        else:
            boxes = [n[:3] for n in new_boxes if n[-1] == new_boxes[0][-1]]
        # print(boxes)
        if all([get_dot_count(box) <= 8 for box in boxes]):
            break
    in_range_counts = []
    for box in boxes:
        x_range, y_range, z_range = box
        for (x, y), z in product(product(x_range, y_range), z_range):
            in_range_count = 0
            for bot in nanobots:
                if manhatton_distance((x, y, z), bot[:-1]) <= bot[-1]:
                    in_range_count += 1
            in_range_counts.append((x, y, z, in_range_count))
        in_range_counts.sort(key=lambda b: b[-1], reverse=True)
    if len([c for c in in_range_counts if c[-1] == in_range_counts[0][-1]]) == 1:
        print(manhatton_distance(in_range_counts[0][:3], (0, 0, 0)))
    else:
        nearest = [(c[0], c[1], c[2], c[3], manhatton_distance(c[:3], (0, 0, 0))) for c in in_range_counts if c[-1] == in_range_counts[0][-1]]
        nearest.sort(key=lambda n: n[-1])
        print(nearest)
        print(manhatton_distance(nearest[0][:3], (0, 0, 0)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_23.txt', 'r')
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
