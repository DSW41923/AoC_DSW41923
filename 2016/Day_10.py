import argparse
import copy
import re

def part_1(instructions):
    bots = {}
    get_value = True
    while True:
        for instruction in instructions:
            if instruction.startswith('bot'):
                bot_num, low_dest, low_dest_num, high_dest, high_dest_num = \
                    re.findall(r'bot (\d+) gives low to ([a-z]+) (\d+) and high to ([a-z]+) (\d+)', instruction)[0]
                if bots.get(bot_num) and all(bots.get(bot_num)):
                    if low_dest == 'bot':
                        if bots.get(low_dest_num):
                            bots[low_dest_num] = tuple(sorted((bots[low_dest_num][0], bots[bot_num][0])))
                        else:
                            bots[low_dest_num] = (bots[bot_num][0], None)
                    if high_dest == 'bot':
                        if bots.get(high_dest_num):
                            bots[high_dest_num] = tuple(sorted((bots[high_dest_num][0], bots[bot_num][1])))
                        else:
                            bots[high_dest_num] = (bots[bot_num][1], None)
                    del bots[bot_num]
            elif instruction.startswith('value') and get_value:
                value, bot_num = re.findall(r'value (\d+) goes to bot (\d+)', instruction)[0]
                value = int(value)
                if bots.get(bot_num):
                    bots[bot_num] = tuple(sorted((bots[bot_num][0], value)))
                else:
                    bots[bot_num] = (value, None)
            for bot_num, bot_values in bots.items():
                if bot_values == (17, 61):
                    print("The number of the bot that is responsible for "
                          "comparing value-61 microchips with value-17 microchips is {}".format(bot_num))
                    return

        get_value = False


def update_bot_chips(bots, target_bot_num, value):
    if target_bot_num in bots:
        if bots[target_bot_num]['low'] < value:
            bots[target_bot_num]['high'] = value
        else:
            bots[target_bot_num]['high'] = bots[target_bot_num]['low']
            bots[target_bot_num]['low'] = value
    else:
        bots.update({target_bot_num: {'low': value, 'high': None}})


def update_output_bins(output_bins, target_bin_num, value):
    if target_bin_num in output_bins:
        output_bins[target_bin_num].append(value)
    else:
        output_bins.update({target_bin_num: [value]})


def part_2(instructions):
    bots = {}
    output_bins = {}
    get_value = True
    running_instructions = copy.deepcopy(instructions)
    while not bots.items() or any([bots[b].get('low') for b in bots.keys()]+[bots[b].get('high') for b in bots.keys()]):
        old_bots = copy.deepcopy(bots)
        new_running_instructions = []
        for instruction in running_instructions:
            if instruction.startswith('bot'):
                new_running_instructions.append(instruction)
                bot_num, low_dest, low_dest_num, high_dest, high_dest_num = \
                    re.findall(r'bot (\d+) gives low to ([a-z]+) (\d+) and high to ([a-z]+) (\d+)', instruction)[0]
                if bots.get(bot_num) and all([bots[bot_num].get('low'), bots[bot_num].get('high')]):
                    if low_dest == 'bot':
                        update_bot_chips(bots, low_dest_num, bots[bot_num]['low'])
                    elif low_dest == 'output':
                        update_output_bins(output_bins, low_dest_num, bots[bot_num]['low'])

                    if high_dest == 'bot':
                        update_bot_chips(bots, high_dest_num, bots[bot_num]['high'])
                    elif high_dest == 'output':
                        update_output_bins(output_bins, high_dest_num, bots[bot_num]['high'])

                    del bots[bot_num]

            elif instruction.startswith('value') and get_value:
                value, bot_num = re.findall(r'value (\d+) goes to bot (\d+)', instruction)[0]
                value = int(value)
                update_bot_chips(bots, bot_num, value)

        if bots == old_bots:
            break
        else:
            running_instructions = new_running_instructions

    print("The multiplication is {}".format(output_bins['0'][0] * output_bins['1'][0] * output_bins['2'][0]))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_10.txt', 'r')
    instructions = file_input.readlines()
    file_input.close()

    if args.part == '1':
        part_1(instructions)
    elif args.part == '2':
        part_2(instructions)
    else:
        part_1(instructions)
        part_2(instructions)


if __name__ == "__main__":
    main()
