import sys
import getopt
import copy


def get_three_dimensional_neighbor_states(a, b, c, states):
    neighbor_states = []

    if a > 0:
        neighbor_states.append(states[c][b][a - 1])
    if a < len(states[0][0]) - 1:
        neighbor_states.append(states[c][b][a + 1])

    if b > 0:
        neighbor_states += states[c][b - 1][max(a - 1, 0):min(a + 2, len(states[0][0]))]
    if b < len(states[0]) - 1:
        neighbor_states += states[c][b + 1][max(a - 1, 0):min(a + 2, len(states[0][0]))]

    if c > 0:
        lower_neighbor_states = states[c-1][max(b-1, 0):min(b+2, len(states[0]))]
        for s in lower_neighbor_states:
            neighbor_states += s[max(a-1, 0):min(a+2, len(states[0][0]))]
    if c < len(states) - 1:
        upper_neighbor_states = states[c+1][max(b-1, 0):min(b+2, len(states[0]))]
        for s in upper_neighbor_states:
            neighbor_states += s[max(a-1, 0):min(a+2, len(states[0][0]))]

    return neighbor_states

def get_three_dimensional_result_states(initial_states, iteration_times):
    old_states = [copy.deepcopy(initial_states)]
    for _ in range(iteration_times):
        new_length = len(old_states[0][0]) + 2
        new_layer_states = [[['.' for _ in range(new_length)] for _ in range(new_length)]]
        new_base_states = copy.deepcopy(old_states)
        for z, z_states in enumerate(old_states):
            for index in range(len(z_states)):
                new_base_states[z][index] = ['.'] + old_states[z][index] + ['.']
            old_states_fill = [['.' for _ in range(new_length)]]
            old_states_fill.extend(new_base_states[z])
            old_states_fill.append(copy.deepcopy(old_states_fill[0]))
            new_base_states[z] = old_states_fill
        new_base_states = new_layer_states + new_base_states + new_layer_states
        new_states = copy.deepcopy(new_base_states)
        for z, z_states in enumerate(new_base_states):
            for y, y_states in enumerate(z_states):
                for x, state in enumerate(y_states):
                    n_states = get_three_dimensional_neighbor_states(x, y, z, new_base_states)
                    if state == '#' and sum(s == '#' for s in n_states) not in [2, 3]:
                        new_states[z][y][x] = '.'
                    elif state == '.' and sum(s == '#' for s in n_states) == 3:
                        new_states[z][y][x] = '#'
        old_states = copy.deepcopy(new_states)

    return old_states


def get_four_dimensional_neighbor_states(a, b, c, d, states):
    neighbor_states = []
    for i in range(81):
        def ternary(n):
            if n == 0:
                return '0'
            nums = []
            while n:
                n, r = divmod(n, 3)
                nums.append(str(r))
            return ''.join(reversed(nums))
        text_i = ternary(i)
        text_i = '0' * (4-len(text_i)) + text_i
        s, t, u, v = list(map(lambda m: 1-int(m), list(text_i)))
        if all(0 <= p for p in [d+s, c+t, b+u, a+v]):
            if d + s < len(states):
                if c + t < len(states[0]):
                    if b + u < len(states[0][0]):
                        if a + v < len(states[0][0][0]):
                            neighbor_states.append(states[d+s][c+t][b+u][a+v])

    neighbor_states.remove(states[d][c][b][a])

    return neighbor_states

def get_four_dimensional_result_states(initial_states, iteration_times):
    old_states = [[copy.deepcopy(initial_states)]]
    for k in range(iteration_times):
        old_line_length = len(old_states[0][0][0])
        new_space_length = len(old_states[0]) + 2
        new_line_length = len(old_states[0][0][0]) + 2
        new_line_states = ['.' for _ in range(new_line_length)]
        new_layer_states = [copy.deepcopy(new_line_states) for _ in range(new_line_length)]
        new_space_states = [copy.deepcopy(new_layer_states) for _ in range(new_space_length)]
        new_base_states = copy.deepcopy(old_states)

        for w, w_states in enumerate(old_states):
            for z, z_states in enumerate(w_states):
                for index in range(old_line_length):
                    new_base_states[w][z][index].insert(0, '.')
                    new_base_states[w][z][index].append('.')
                new_base_states[w][z].insert(0, copy.deepcopy(new_line_states))
                new_base_states[w][z].append(copy.deepcopy(new_line_states))
            new_base_states[w].insert(0, copy.deepcopy(new_layer_states))
            new_base_states[w].append(copy.deepcopy(new_layer_states))
        new_base_states.insert(0, copy.deepcopy(new_space_states))
        new_base_states.append(copy.deepcopy(new_space_states))
        new_states = copy.deepcopy(new_base_states)
        for w, w_states in enumerate(new_base_states):
            for z, z_states in enumerate(w_states):
                for y, y_states in enumerate(z_states):
                    for x, state in enumerate(y_states):
                        n_states = get_four_dimensional_neighbor_states(x, y, z, w, new_base_states)
                        if state == '#' and sum(s == '#' for s in n_states) not in [2, 3]:
                            new_states[w][z][y][x] = '.'
                        elif state == '.' and sum(s == '#' for s in n_states) == 3:
                            new_states[w][z][y][x] = '#'
        old_states = copy.deepcopy(new_states)

    return old_states


# noinspection SpellCheckingInspection
def main(argv):

    try:
        opts, args = getopt.getopt(argv,"h:",["help"])
    except getopt.GetoptError:
        print('Usage: python3 Day_17.py [-h | --help]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('Usage: python3 Day_17.py [-h | --help]')
            print('Advent of Code 2020 Day 17')
            sys.exit()

    file_input = open('Input_17.txt', 'r')
    input_strings = file_input.readlines()
    file_input.close()
    initial_states = []
    for x in input_strings:
        initial_states.append(list(x.replace('\n', '')))
    result_states = get_three_dimensional_result_states(initial_states, 6)
    active_count = 0
    for z_states in result_states:
        for y_states in z_states:
            active_count += y_states.count('#')
    print(active_count)
    four_dimensional_result_states = get_four_dimensional_result_states(initial_states, 6)
    new_active_count = 0
    for w_states in four_dimensional_result_states:
        for z_states in w_states:
            for y_states in z_states:
                new_active_count += y_states.count('#')
    print(new_active_count)


if __name__ == "__main__":
    main(sys.argv[1:])