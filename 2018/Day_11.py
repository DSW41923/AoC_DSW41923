import argparse


def get_cells_data(input_string):
    grid_serial_number = int(input_string)
    cells = [[0 for _ in range(301)] for _ in range(301)]
    for x in range(1, 301):
        for y in range(1, 301):
            rack_id = x + 10
            power_level = rack_id * y
            power_level += grid_serial_number
            power_level *= rack_id
            power_level = int(str(power_level)[-3])
            power_level -= 5
            cells[y][x] = power_level
    return cells


def part_1(input_string):
    cells = get_cells_data(input_string)
    max_power_level = 0
    result = None
    for x in range(1, 299):
        for y in range(1, 299):
            total_power_level = sum(cells[y][x:x+3]) + sum(cells[y+1][x:x+3]) + sum(cells[y+2][x:x+3])
            if total_power_level > max_power_level:
                max_power_level = total_power_level
                result = (x,y)
    print(','.join(list(map(str, result))))


def part_2(input_string):
    cells = get_cells_data(input_string)
    max_power_level = 0
    result = None
    for size in range(1, 301):
        temp_max = 0
        for x in range(1, 302-size):
            for y in range(1, 302-size):
                total_power_level = 0
                for i in range(size):
                    total_power_level += sum(cells[y+i][x:x+size])
                temp_max = max(temp_max, total_power_level)
                if total_power_level > max_power_level:
                    max_power_level = total_power_level
                    result = (x,y,size)
        if temp_max == 0:
            break
    print(','.join(list(map(str, result))))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_11.txt', 'r')
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
