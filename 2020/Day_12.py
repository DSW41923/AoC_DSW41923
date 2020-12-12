import sys
import getopt
import re


class Ferry(object):

    def __init__(self, facing, x=0, y=0):
        super(Ferry, self).__init__()
        self.facing = facing
        self.origin = (x, y)
        self.x, self.y = x, y

    def moving_forward(self, value):
        if self.facing == 'E':
            self.x += value
        if self.facing == 'W':
            self.x -= value
        if self.facing == 'N':
            self.y += value
        if self.facing == 'S':
            self.y -= value

    def turn(self, direction, value):
        facing = ['N', 'W', 'S', 'E']
        if direction == 'L':
            self.facing = facing[(facing.index(self.facing) + value // 90) % 4]
        if direction == 'R':
            self.facing = facing[(facing.index(self.facing) - value // 90) % 4]

    def move(self, direction, value):
        if direction == 'E':
            self.x += value
        if direction == 'W':
            self.x -= value
        if direction == 'N':
            self.y += value
        if direction == 'S':
            self.y -= value

    def distance_to_origin(self):
        return abs(self.x - self.origin[0]) + abs(self.y - self.origin[1])


class Newferry(Ferry):

    def __init__(self, waypoint, facing, x=0, y=0):
        super(Newferry, self).__init__(facing, x, y)
        self.waypoint = waypoint

    def moving_ferry(self, value):
        for w_facing, w_value in self.waypoint:
            self.facing = w_facing
            self.moving_forward(value * w_value)

    def rotate_waypoint(self, direction, value):
        facing = ['N', 'W', 'S', 'E']
        waypoint = []
        for w_facing, w_value in self.waypoint:
            if direction == 'L':
                new_facing = facing[(facing.index(w_facing) + value // 90) % 4]
            if direction == 'R':
                new_facing = facing[(facing.index(w_facing) - value // 90) % 4]
            waypoint.append((new_facing, w_value))
        self.waypoint = waypoint

    def move_waypoint(self, direction, value):
        value = -value if direction in ['W', 'S'] else value
        waypoint = []
        for w_facing, w_value in self.waypoint:
            direct_value = -w_value if w_facing in ['W', 'S'] else w_value
            new_value = direct_value + value
            if w_facing in ['E', 'W'] and direction in ['E', 'W']:
                if new_value > 0:
                    waypoint.append(('E', abs(new_value)))
                else:
                    waypoint.append(('W', abs(new_value)))
            elif w_facing in ['N', 'S'] and direction in ['N', 'S']:
                if new_value > 0:
                    waypoint.append(('N', abs(new_value)))
                else:
                    waypoint.append(('S', abs(new_value)))
            else:
                waypoint.append((w_facing, w_value))
        self.waypoint = waypoint


# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_12.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_12.py [-h | --help]')
            print('Advent of Code 2020 Day 12')
            sys.exit()

    file_input = open('Input_12.txt', 'r')
    instruction_strings = file_input.read()
    file_input.close()
    instructions = []
    ferry = Ferry(facing='E')
    for action, value in re.findall(r'([NSEWLRF])(\d+)', instruction_strings):
        instructions.append((action, int(value)))
        if action == 'F':
            ferry.moving_forward(int(value))
        elif action in ['N', 'E', 'W', 'S']:
            ferry.move(action, int(value))
        elif action in ['L', 'R']:
            ferry.turn(action, int(value))
    print(ferry.distance_to_origin())

    new_ferry = Newferry((('E', 10), ('N', 1)), 'E')
    for action, value in instructions:
        if action == 'F':
            new_ferry.moving_ferry(value)
        elif action in ['N', 'E', 'W', 'S']:
            new_ferry.move_waypoint(action, value)
        elif action in ['L', 'R']:
            new_ferry.rotate_waypoint(action, value)
    print(new_ferry.distance_to_origin())


if __name__ == "__main__":
    main(sys.argv[1:])