import argparse
import heapq

from copy import deepcopy
from functools import lru_cache


def count_change(string):
    change = 0
    for i in range(len(string)-1):
        if string[i] != string [i+1]:
            change += 1
    return change


def get_preset_data():
    directional_pad = {
        '^': {
            'v': 'v',
            '>': 'A'
        },
        '>': {
            '^': 'A',
            '<': 'v'
        },
        'v': {
            '^': '^',
            '>': '>',
            '<': '<'
        },
        '<': {
            '>': 'v',
        },
        'A': {
            'v': '>',
            '<': '^'
        }
    }
    directional_pad_dict = {}
    for d1 in directional_pad:
        if d1 not in directional_pad_dict:
            directional_pad_dict[d1] = {}
        for d2 in directional_pad:
            if d2 == d1:
                directional_pad_dict[d1].update({
                    d2: ['']
                })
                continue
            else:
                cur = [(d1, '', set())]
                while cur:
                    cur_pad, path, visited = cur.pop()
                    visited.add(cur_pad)
                    for m, d in directional_pad[cur_pad].items():
                        if d == d2:
                            if d not in directional_pad_dict[d1]:
                                directional_pad_dict[d1].update({
                                    d: [path+m]
                                })
                            else:
                                if all([len(path+m) < len(dd) for dd in directional_pad_dict[d1][d]]):
                                    directional_pad_dict[d1][d] = [path+m]
                                elif all([len(path+m) == len(dd) for dd in directional_pad_dict[d1][d]]):
                                    if all([count_change(path+m) < count_change(dd) for dd in directional_pad_dict[d1][d]]):
                                        directional_pad_dict[d1][d] = [path+m]
                                    elif all([count_change(path+m) == count_change(dd) for dd in directional_pad_dict[d1][d]]):
                                        directional_pad_dict[d1][d] += [path+m]
                                        cur.append((d, path+m, deepcopy(visited)))
                        else:
                            if d not in visited:
                                cur.append((d, path+m, deepcopy(visited)))
    num_pad = {
        '0': {
            '^': '2',
            '>': 'A'
        },
        '1': {
            '^': '4',
            '>': '2'
        },
        '2': {
            '^': '5',
            '>': '3',
            'v': '0',
            '<': '1'
        },
        '3': {
            '^': '6',
            'v': 'A',
            '<': '2'
        },
        '4': {
            '^': '7',
            'v': '1',
            '>': '5'
        },
        '5': {
            '^': '8',
            '>': '6',
            'v': '2',
            '<': '4'
        },
        '6': {
            '^': '9',
            'v': '3',
            '<': '5'
        },
        '7': {
            'v': '4',
            '>': '8'
        },
        '8': {
            '<': '7',
            'v': '5',
            '>': '9'
        },
        '9': {
            '<': '8',
            'v': '6',
        },
        'A': {
            '^': '3',
            '<': '0'
        },
    }
    num_pad_dict = {}
    for d1 in num_pad:
        if d1 not in num_pad_dict:
            num_pad_dict[d1] = {}
        for d2 in num_pad:
            if d2 == d1:
                num_pad_dict[d1].update({
                    d2: ['']
                })
                continue
            else:
                cur = [(d1, '', set())]
                while cur:
                    cur_pad, path, visited = cur.pop()
                    visited.add(cur_pad)
                    for m, d in num_pad[cur_pad].items():
                        if d == d2:
                            if d not in num_pad_dict[d1]:
                                num_pad_dict[d1].update({
                                    d: [path+m]
                                })
                            else:
                                if all([len(path+m) < len(dd) for dd in num_pad_dict[d1][d]]):
                                    num_pad_dict[d1][d] = [path+m]
                                elif all([len(path+m) == len(dd) for dd in num_pad_dict[d1][d]]):
                                    if all([count_change(path+m) < count_change(dd) for dd in num_pad_dict[d1][d]]):
                                        num_pad_dict[d1][d] = [path+m]
                                    elif all([count_change(path+m) == count_change(dd) for dd in num_pad_dict[d1][d]]):
                                        num_pad_dict[d1][d] += [path+m]
                                        cur.append((d, path+m, deepcopy(visited)))
                        else:
                            if d not in visited:
                                cur.append((d, path+m, deepcopy(visited)))
    return directional_pad_dict, num_pad_dict


def num_pad_to_directional_pad(code, num_pad_dict):
    code = 'A' + code
    buttons_list = [(0, '')]
    results = []
    while buttons_list:
        consumed, buttons = heapq.heappop(buttons_list)
        next_options = num_pad_dict[code[consumed]][code[consumed+1]]
        for option in next_options:
            new_consumed = consumed + 1
            new_buttons = buttons + option + 'A'
            if new_consumed < (len(code)-1):
                heapq.heappush(buttons_list, (new_consumed, new_buttons))
            elif new_consumed == (len(code)-1):
                results.append(new_buttons)
    return results


def directional_pad_up_level(code, directional_pad_dict, existed_result=None, optimization=False):
    if not optimization:
        code = 'A' + code
    buttons_list = [(0, '')]
    results = []
    while buttons_list:
        consumed, buttons = heapq.heappop(buttons_list)
        next_options = directional_pad_dict[code[consumed]][code[consumed+1]]
        for option in next_options:
            new_consumed = consumed + 1
            new_buttons = buttons + option + 'A'
            if new_consumed < (len(code)-1):
                if existed_result and len(new_buttons) > len(existed_result):
                    continue
                heapq.heappush(buttons_list, (new_consumed, new_buttons))
            elif new_consumed == (len(code)-1):
                if not results:
                    results.append(new_buttons)
                else:
                    if existed_result and len(new_buttons) > len(existed_result):
                        continue
                    if all([len(new_buttons) == len(nrb) for nrb in results]):
                        results.append(new_buttons)
                    elif all([len(new_buttons) < len(nrb) for nrb in results]):
                        # new_result_buttons.append(new_buttons)
                        results = [new_buttons]
    return results


def part_1(input_string):
    directional_pad_dict, num_pad_dict = get_preset_data()
    codes = input_string.split('\n')
    result = 0
    for code in codes:
        result_buttons = num_pad_to_directional_pad(code, num_pad_dict)
        for _ in range(2):
            new_result_buttons = []
            for b in result_buttons:
                if new_result_buttons:
                    new_results = directional_pad_up_level(b, directional_pad_dict, new_result_buttons[0])
                    for new_result in new_results:
                        if all([len(new_result) == len(nrb) for nrb in new_result_buttons]):
                            new_result_buttons.append(new_result)
                        elif all([len(new_result) < len(nrb) for nrb in new_result_buttons]):
                            new_result_buttons = [new_result]
                else:
                    new_result_buttons.extend(directional_pad_up_level(b, directional_pad_dict))
            result_buttons = new_result_buttons
        result += (int(code[:-1]) * len(result_buttons[0]))
    print(result)


def part_2(input_string):
    directional_pad_dict, num_pad_dict = get_preset_data()
    # Improve direction pad dict
    # Inspiration below
    # numpad  = {
    #     '7': (0, 0), '8': (0, 1), '9': (0, 2),
    #     '4': (1, 0), '5': (1, 1), '6': (1, 2),
    #     '1': (2, 0), '2': (2, 1), '3': (2, 2),
    #                  '0': (3, 1), 'A': (3, 2),
    # }
    # dirpad = {
    #                  '^': (0, 1), 'A': (0, 2),
    #     '<': (1, 0), 'v': (1, 1), '>': (1, 2),
    # }
    # def create_graph(keypad, invalid_coords):
    #     graph = {}
    #     for a, (x1, y1) in keypad.items():
    #         for b, (x2, y2) in keypad.items():
    #             path = '<' * (y1 - y2) + 'v' * (x2 - x1) + '^' * (x1 - x2) + '>' * (y2 - y1)
    #             if invalid_coords == (x1, y2) or invalid_coords == (x2, y1):
    #                 path = path[::-1]
    #             graph[(a, b)] = path + 'A'
    #     return graph

    # numpad_graph = create_graph(numpad, (3, 0))
    # dirpad_graph = create_graph(dirpad, (0, 0))
    directions = ['>', '^', 'v', '<']
    for direction in directional_pad_dict:
        for dd in directional_pad_dict[direction]:
            if len(directional_pad_dict[direction][dd]) > 1: # Need optimization
                ddd_list = list(directional_pad_dict[direction][dd][0])
                ddd_list.sort(key=lambda n: directions.index(n),reverse=True)
                directional_pad_dict[direction][dd] = ''.join(ddd_list)
            else:
                directional_pad_dict[direction][dd] = directional_pad_dict[direction][dd][0]
    for num in num_pad_dict:
        for nn in num_pad_dict[num]:
            if len(num_pad_dict[num][nn]) > 1: # Need optimization
                nnn_list = list(num_pad_dict[num][nn][0])
                nnn_list.sort(key=lambda n: directions.index(n),reverse=True)
                num_pad_dict[num][nn] = ''.join(nnn_list)
            else:
                num_pad_dict[num][nn] = num_pad_dict[num][nn][0]

    robots_count = 25
    codes = input_string.split('\n')
    result = 0
    for code in codes:
        @lru_cache(maxsize=None)
        def recursive_solve(buttons, remaining):
            if remaining == 0:
                return len(buttons)
            buttons = 'A' + buttons
            recursive_result = 0
            for i in range(len(buttons)-1):
                recursive_result += recursive_solve(directional_pad_dict[buttons[i]][buttons[i+1]] + 'A', remaining-1)
            return recursive_result
        l1_code = 'A' + code
        l1_buttons_count = 0
        for i in range(len(l1_code)-1):
            l1_buttons_count += recursive_solve(num_pad_dict[l1_code[i]][l1_code[i+1]] + 'A', robots_count)
        result += (int(code[:-1]) * l1_buttons_count)
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2024/Input_21.txt', 'r')
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
