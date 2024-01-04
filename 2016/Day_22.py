import argparse
import re


def get_nodes(input_string):
    nodes = []
    for node_name, size, used, avail in re.findall(
            r'/dev/grid/([nodexy\-0-9]+)\s+(\d+)T\s+(\d+)T\s+(\d+)T', input_string):
        node_x, node_y = map(int, re.match(r'node-x(\d+)-y(\d+)', node_name).groups())
        nodes.append({
            'name': node_name,
            'location': {'x': node_x, 'y': node_y},
            'size': int(size),
            'used': int(used),
            'avail': int(avail)
        })

    return nodes


def get_nodes_array(nodes):
    max_x, max_y = max([node['location']['x'] for node in nodes]), max([node['location']['y'] for node in nodes])
    nodes_array = [[(None, None) for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for node in nodes:
        nodes_array[node['location']['y']][node['location']['x']] = (node['used'], node['size'])
    return nodes_array


def get_manhatton_distance(p0, p1):
    return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])


def part_1(input_string):
    nodes = get_nodes(input_string)

    viable_pairs_count = 0
    for node in nodes:
        if node['used'] != 0:
            for another_node in nodes:
                if node['name'] != another_node['name'] and node['used'] <= another_node['avail']:
                    viable_pairs_count += 1

    print(viable_pairs_count)


def part_2(input_string):
    # Use another way to do this
    # Find empty disk
    # Find wall and hole
    # Calculate steps to move empty beside goal
    # Calculate steps to move those to accessible node

    nodes = get_nodes(input_string)
    nodes_array = get_nodes_array(nodes)
    target_node = (0, len(nodes_array[0]) - 1)
    accessible_node = (0, 0)
    max_x, max_y = len(nodes_array[0]) - 1, len(nodes_array) - 1
    empty_node = ([(y, x) for y, row_nodes in enumerate(nodes_array)
                   for x, node in enumerate(row_nodes) if node[0] == 0])[0]
    empty_node_y, empty_node_x = empty_node

    wall_nodes = []
    for y, row_nodes in enumerate(nodes_array):
        for x, node in enumerate(row_nodes):
            if node[0] > nodes_array[empty_node_y][empty_node_x][1]:
                wall_nodes.append((y, x))

    wall_nodes_x, wall_nodes_y = set([node[1] for node in wall_nodes]), set([node[0] for node in wall_nodes])
    hole_node = (None, None)
    if len(wall_nodes_x) != 1 and len(wall_nodes_y) != 1:
        print("Too complicated!")
        return

    if len(wall_nodes_y) == 1:
        hole_nodes = [(list(wall_nodes_y)[0], x) for x in range(max_x + 1) if x not in wall_nodes_x]
        hole_node = ([(y, x) for (y, x) in hole_nodes if (max_x-x) == min([max_x - x for y, x in hole_nodes])])[0]

    if len(wall_nodes_x) == 1:
        hole_nodes = [(y, list(wall_nodes_x)[0]) for y in range(max_y + 1) if y not in wall_nodes_y]
        if len(hole_nodes) > 1:
            hole_node = ([(y, x) for (y, x) in hole_nodes if y == min([y for y, x in hole_nodes])])[0]

    steps = get_manhatton_distance(empty_node, hole_node) + get_manhatton_distance(target_node, hole_node)
    steps += (5 * (target_node[1] - accessible_node[1] - 1))
    print(steps)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2016/Input_22.txt', 'r')
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
