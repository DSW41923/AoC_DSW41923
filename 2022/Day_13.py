import argparse
import functools


def is_right_order(packet_l, packet_r):
    for p in range(len(packet_l)):
        value_l = packet_l[p]
        if p >= len(packet_r):
            return -1
        value_r = packet_r[p]
        if type(value_l) == int and type(value_r) == int:
            if value_l < value_r:
                return 1
            if value_l > value_r:
                return -1
            continue
        if type(value_l) != list:
            if result:=is_right_order([value_l], value_r):
                return result
            continue
        if type(value_r) != list:
            if result:=is_right_order(value_l, [value_r]):
                return result
            continue
        if result:=is_right_order(value_l, value_r):
            return result

    if len(packet_r) > len(packet_l):
        return 1
    
    # Since we looped through packet_l 
    # and return when index out of the bound of packet_r
    # This if never hit
    if len(packet_r) < len(packet_l):
        print("REALLY?")
        return -1

    return 0


def part_1(input_string):
    packet_pairs = input_string.split('\n\n')
    right_order_pairs_count = 0
    for p, packet_pair in enumerate(packet_pairs):
        packet_left, packet_right = tuple(map(eval, packet_pair.split('\n')[:2]))
        if result:=is_right_order(packet_left, packet_right) > 0:
            right_order_pairs_count += (p + 1)
    print(right_order_pairs_count)


def part_2(input_string):
    packets = [s for s in input_string.split('\n') if len(s) > 0]
    divider_packets = ['[[2]]', '[[6]]']
    packets.extend(divider_packets)
    packets = list(map(eval, packets))
    packets.sort(key=functools.cmp_to_key(is_right_order), reverse=True)
    print((packets.index(eval(divider_packets[0])) + 1) * (packets.index(eval(divider_packets[1])) + 1))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2022/Input_13.txt', 'r')
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

