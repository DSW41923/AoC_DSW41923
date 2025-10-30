import argparse

from copy import deepcopy
from Day_11 import parse_data, run_program_v7


class IntCodeComputer(object):
    def __init__(self, program_code='', id=0, relative_offset=0, index=0, inputs=[]):
        self.relative_offset = relative_offset
        self.memory = {}
        if program_code != '':
            codes = list(map(int, program_code.split(',')))
            for i, c in enumerate(codes):
                self.memory.update({
                    i: c
                })
        self.index = index
        self.inputs = inputs.copy()
        self.outputs = []
        self.id = id
        self.finished = False

    def set_whole_memory(self, memory):
        self.memory = deepcopy(memory)

    def set_relative_offset(self, relative_offset):
        self.relative_offset = relative_offset

    def set_index(self, index):
        self.index = index

    def set_inputs(self, inputs):
        self.inputs = deepcopy(inputs)

    def set_outputs(self, outputs):
        self.outputs = deepcopy(outputs)

    def set_finished(self, finished):
        self.finished = finished

    def set_memory(self, pos, val):
        self.memory[pos] = val

    def add_input(self,val):
        self.inputs.append(val)

    def print_outputs(self):
        print(self.outputs)

    def get_outputs(self):
        return self.outputs

    def clear_outputs(self):
        self.outputs.clear()

    def run(self):
        while not self.finished:
            cur_value = self.memory.get(self.index, 0)
            # print(self.index, cur_value, self.memory.get(self.index+1, 0), self.memory.get(self.index+2, 0), self.memory.get(self.index+3, 0), self.relative_offset)
            opcode = cur_value % 100
            param_codes = [(cur_value // (100*(10**i))) % 10 for i in range(3)]
            params_id = [0 for _ in range(3)]
            for i in range(3):
                if param_codes[i] == 0:
                    params_id[i] = self.memory.get(self.index+1+i, 0)
                elif param_codes[i] == 1:
                    params_id[i] = self.index+1+i
                elif param_codes[i] == 2:
                    params_id[i] = self.relative_offset + self.memory.get(self.index+1+i, 0)

            if opcode == 99:
                self.index += 1
                self.finished = True
            elif opcode == 1:
                self.memory[params_id[2]] = self.memory.get(params_id[0], 0) + self.memory.get(params_id[1], 0)
                self.index += 4
            elif opcode == 2:
                self.memory[params_id[2]] = self.memory.get(params_id[0], 0) * self.memory.get(params_id[1], 0)
                self.index += 4
            elif opcode == 3:
                if len(self.inputs) > 0:
                    self.memory[params_id[0]] = self.inputs.pop(0)
                    self.index += 2
                else:
                    break
            elif opcode == 4:
                self.outputs.append(int(self.memory.get(params_id[0], 0)))
                self.index += 2
            elif opcode == 5:
                if self.memory.get(params_id[0], 0) != 0:
                    self.index = self.memory.get(params_id[1], 0)
                else:
                    self.index += 3
            elif opcode == 6:
                if self.memory.get(params_id[0], 0) == 0:
                    self.index = self.memory.get(params_id[1], 0)
                else:
                    self.index += 3
            elif opcode == 7:
                self.memory[params_id[2]] = (self.memory.get(params_id[0], 0) < self.memory.get(params_id[1], 0))
                self.index += 4
            elif opcode == 8:
                self.memory[params_id[2]] = (self.memory.get(params_id[0], 0) == self.memory.get(params_id[1], 0))
                self.index += 4
            elif opcode == 9:
                self.relative_offset += self.memory.get(params_id[0], 0)
                self.index += 2
            else:
                print(self.index, opcode)
                import pdb; pdb.set_trace()

    def copy(self):
        new_computer = IntCodeComputer()
        new_computer.set_whole_memory(self.memory)
        new_computer.set_relative_offset(self.relative_offset)
        new_computer.set_index(self.index)
        new_computer.set_inputs(self.inputs)
        new_computer.set_outputs(self.outputs)
        new_computer.set_finished(self.finished)
        return new_computer


def part_1(input_string):
    codes_dict = parse_data(input_string)
    cur = 0
    relative_offset = 0
    outputs = []
    while True:
        cur, relative_offset, codes_dict, output = run_program_v7(cur, relative_offset, codes_dict, input_num=0)
        if output == None:
            break
        else:
            outputs.append(output)
    tiles = [[] for _ in range(5)]
    for i in range(0, len(outputs), 3):
        x, y, tile_id = outputs[i:i+3]
        tiles[tile_id].append((x, y))
    print(len(tiles[2]))


def part_2(input_string):
    computer = IntCodeComputer(input_string)
    computer.set_memory(0, 2)
    computer.run()
    outputs = computer.get_outputs()
    score = paddle_x = ball_x = 0
    tiles = [[] for _ in range(5)]
    for i in range(0, len(outputs), 3):
        x, y, data = outputs[i:i+3]
        if x == -1 and y == 0:
            score = data
            continue
        if data == 3:
            paddle_x = x
        if data == 4:
            ball_x = x
        tiles[data].append((x, y))
    computer.clear_outputs()

    while True:
        joystick_move = 0
        if ball_x > paddle_x:
            joystick_move = 1
        elif ball_x < paddle_x:
            joystick_move = -1
        
        computer.add_input(joystick_move)
        computer.run()
        outputs = computer.get_outputs()
        for i in range(0, len(outputs), 3):
            x, y, data = outputs[i:i+3]
            if x == -1 and y == 0:
                score = data
                continue
            if data == 3:
                paddle_x = x
            if data == 4:
                ball_x = x
            
            for j in range(5):
                if (x, y) in tiles[j] and j != data:
                    tiles[j].remove((x, y))
            tiles[data].append((x, y))
        computer.clear_outputs()
        if len(tiles[2]) == 0:
            print(score)
            break


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_13.txt', 'r')
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
