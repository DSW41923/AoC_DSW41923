import argparse
import copy
import itertools


def image_enhancement(algorithm, image, init_value='0'):
    new_x_range, new_y_range = len(image) + 2, len(image[0]) + 2
    enlarged_image = [[init_value for _ in range(new_x_range + 2)] for _ in range(new_y_range + 2)]
    for x, y in itertools.product(range(new_x_range - 2), range(new_y_range - 2)):
        enlarged_image[x + 2][y + 2] = image[x][y]

    new_image = [['' for _ in range(new_x_range)] for _ in range(new_y_range)]
    for x, y in itertools.product(range(new_x_range), range(new_y_range)):
        adjacent_pixels = itertools.product(list(range(max(0, x), min(new_x_range + 2, x + 3))),
                                            list(range(max(0, y), min(new_y_range + 2, y + 3))))
        algorithm_input = ''.join([enlarged_image[i][j] for i, j in adjacent_pixels])
        new_image[x][y] = algorithm[int(algorithm_input, 2)]

    return new_image


def part_1(input_string):
    input_string = input_string.replace('.', '0').replace('#', '1')
    input_data = input_string.split('\n\n')
    algorithm, input_image = input_data[0].replace('\n', ''), [list(r) for r in input_data[1].splitlines()]

    image_1 = image_enhancement(algorithm, input_image, init_value='0')
    image_2 = image_enhancement(algorithm, image_1, init_value='1')
    lit_pixels_count = sum([r.count('1') for r in image_2])
    print(lit_pixels_count)


def part_2(input_string):
    input_string = input_string.replace('.', '0').replace('#', '1')
    input_data = input_string.split('\n\n')
    algorithm, input_image = input_data[0].replace('\n', ''), [list(r) for r in input_data[1].splitlines()]

    image = copy.deepcopy(input_image)
    for i in range(50):
        image = image_enhancement(algorithm, image, init_value=str(i % 2))
    lit_pixels_count = sum([r.count('1') for r in image])
    print(lit_pixels_count)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2021/Input_20.txt', 'r')
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
