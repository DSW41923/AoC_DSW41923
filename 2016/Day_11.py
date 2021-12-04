import argparse
import copy
import itertools
import re


class Arrangement(object):

    def __init__(self, arrangement_strings, elevator_floor=1):
        self.elevator_floor = elevator_floor
        floor_num_mapping = {'first': '1', 'second': '2', 'third': '3', 'fourth': '4'}
        self.floor_arrangement = {'1': [], '2': [], '3': [], '4': []}
        for line in arrangement_strings:
            floor_num = floor_num_mapping[re.search(r'The (\w+) floor', line).group(1)]
            for generator_name in re.findall(r'an? (\w+) generator', line):
                self.floor_arrangement[floor_num].append(generator_name + '_generator')
            for microchip_name in re.findall(r'an? (\w+)-compatible microchip', line):
                self.floor_arrangement[floor_num].append(microchip_name + '_microchip')
        self.chip_locations, self.generator_locations = [], []
        self.update_element_locations()

    def __str__(self):
        return "Elevator floor: {}. Arrangement: {}".format(self.elevator_floor, self.floor_arrangement)

    def __eq__(self, another):
        """Overrides the default implementation"""
        if isinstance(another, Arrangement):
            if (self.chip_locations, self.generator_locations) == (another.chip_locations, another.generator_locations):
                return self.elevator_floor == another.elevator_floor
            else:
                return False
        return NotImplemented

    def move_element(self, moving_elements, direction):
        if (self.elevator_floor + direction) % 5 == 0:
            # Invalid Direction!
            return
        else:
            new_floor = self.elevator_floor + direction
            for element in moving_elements:
                self.floor_arrangement[str(self.elevator_floor)].remove(element)
                self.floor_arrangement[str(new_floor)].append(element)
            self.elevator_floor = new_floor
            self.update_element_locations()

    def update_element_locations(self):
        chip_locations = []
        generator_locations = []
        for floor in self.floor_arrangement:
            for item in self.floor_arrangement[floor]:
                if item.endswith('microchip'):
                    chip_locations.append(int(floor))
                elif item.endswith('generator'):
                    generator_locations.append(int(floor))
        self.chip_locations, self.generator_locations = chip_locations, generator_locations

    def get_current_floor_elements(self):
        return self.floor_arrangement[str(self.elevator_floor)]


def random_move_elments(history, next_arrangements, arrangement, moving_elements_count):
    for moving_elements in itertools.combinations(arrangement.get_current_floor_elements(), moving_elements_count):
        # Only move if moving
        # two generators, two microchips (len=2+1=3)
        # one generator and one microchip with same name (len=1+2=3)
        # or only one generator or microchip (len=1+1=2)
        if len(set([c.split('_')[0] for c in moving_elements] + [c.split('_')[1] for c in moving_elements])) < 4:
            for direction in [-1, 1]:
                new_arrangement = copy.deepcopy(arrangement)
                new_arrangement.move_element(moving_elements, direction)
                if is_valid_arrangement(new_arrangement):
                    is_new_arrangement = True
                    for old_arrangement in reversed(history + next_arrangements):
                        if old_arrangement == new_arrangement:
                            is_new_arrangement = False
                            break
                    if is_new_arrangement:
                        next_arrangements.append(new_arrangement)


def is_valid_arrangement(arrangement):
    for floor in arrangement.floor_arrangement:
        microchip_names = [c.split('_')[0] for c in arrangement.floor_arrangement[floor] if c.endswith('microchip')]
        generator_names = [c.split('_')[0] for c in arrangement.floor_arrangement[floor] if c.endswith('generator')]
        for microchip_name in microchip_names:
            if generator_names and microchip_name not in generator_names:
                return False
    return True


def count_steps_required(initial_arrangement):
    steps_count = 0
    arrangement_history = []
    current_arrangements = [initial_arrangement]
    while True:
        arrangement_history.extend(current_arrangements)
        next_arrangements = []
        for arrangement in current_arrangements:
            for moving_elements_count in [1, 2]:
                random_move_elments(arrangement_history, next_arrangements, arrangement, moving_elements_count)
        current_arrangements = next_arrangements

        steps_count += 1
        for arrangement in current_arrangements:
            if not (arrangement.floor_arrangement['1'] or
                    arrangement.floor_arrangement['2'] or
                    arrangement.floor_arrangement['3']):
                return steps_count


def part_1(input_string):
    initial_arrangement = Arrangement(input_string)
    print("Steps used is: {}".format(count_steps_required(initial_arrangement)))


def part_2(input_string):
    input_string.append(
        "The first floor contains an elerium generator, "
        "an elerium-compatible microchip, a dilithium generator, "
        "and a dilithium-compatible microchip.")
    initial_arrangement = Arrangement(input_string)
    print("Steps used is actually: {}".format(count_steps_required(initial_arrangement)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_11.txt', 'r')
    input_string = file_input.readlines()
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
