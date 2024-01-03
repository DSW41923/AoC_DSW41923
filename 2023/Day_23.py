import argparse


def part_1(input_string):
    tiles = list(map(list, input_string.split('\n')))
    tiles_x_range = len(tiles)
    tiles_y_range = len(tiles[0])
    start = (0, 1)
    destination = (len(tiles)-1, len(tiles)-2)
    dirs = {'R':(0,1), 'L':(0,-1), 'D':(1,0), 'U':(-1,0)}
    newdirs = {'R' : ('U','D','R'),  'L' : ('D','U','L'), 'U' : ('L','R','U'),  'D': ('R','L','D')}
    fronts = [(start, 'D')]
    steps = 0
    result = 0
    while fronts:
        new_fronts = []
        steps += 1
        for front, dir in fronts:
            front_x, front_y = front
            for d in newdirs[dir]:
                next_pos = (front_x+dirs[d][0], front_y+dirs[d][1])
                if next_pos == destination:
                    result = max(result, steps)
                    continue
                if 0 <= next_pos[0] < tiles_x_range and 0 <= next_pos[1] < tiles_y_range:
                    if tiles[next_pos[0]][next_pos[1]] != '#':
                        if d == 'R' and tiles[next_pos[0]][next_pos[1]] != '<': new_fronts.append((next_pos, d))
                        if d == 'L' and tiles[next_pos[0]][next_pos[1]] != '>': new_fronts.append((next_pos, d))
                        if d == 'D' and tiles[next_pos[0]][next_pos[1]] != '^': new_fronts.append((next_pos, d))
                        if d == 'U' and tiles[next_pos[0]][next_pos[1]] != 'v': new_fronts.append((next_pos, d))
        fronts = new_fronts
    print(result)


def part_2(input_string):
    tiles = list(map(list, input_string.split('\n')))
    tiles_x_range = len(tiles)
    tiles_y_range = len(tiles[0])
    start = (0, 1)
    destination = (len(tiles)-1, len(tiles)-2)
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    nodes = {start: 1, destination: 1}
    for x in range(tiles_x_range):
        for y in range(tiles_y_range):
            if tiles[x][y] == '#': continue
            if (paths_count:=len([(x+dir[0], y+dir[1]) for dir in dirs if 0 <= x+dir[0] < tiles_x_range and
                         0 <= y+dir[1] < tiles_y_range and tiles[x+dir[0]][y+dir[1]] != '#'])) > 2:
                nodes.update({(x, y): paths_count})
    def find_edge_length(s, d):
        fronts = [(s, 0, '')]
        while fronts:
            new_fronts = []
            for front, step, visited in fronts:
                step += 1
                visited += str(front)
                front_x, front_y = front
                for dir in dirs:
                    next_pos = (front_x+dir[0], front_y+dir[1])
                    if next_pos == d:
                        return step
                    if next_pos in nodes:
                        continue
                    if 0 <= next_pos[0] < tiles_x_range and 0 <= next_pos[1] < tiles_y_range and tiles[next_pos[0]][next_pos[1]] != '#':
                        if str(next_pos) not in visited and (next_pos, visited) not in new_fronts:
                            new_fronts.append((next_pos, step, visited))
            fronts = new_fronts
        return None
    edges = {}
    for node, paths_count in nodes.items():
        found_path = 0
        for another_node in nodes.keys():
            if found_path == paths_count:
                break
            if node != another_node:
                if edge_len := find_edge_length(node, another_node):
                    edges.update({(node,another_node): edge_len})
                    edges.update({(another_node,node): edge_len})
                    found_path += 1
    for node, paths_count in nodes.items():
        if paths_count == 3:
            direction = {'U':None, 'R':None, 'D':None, 'L':None}
            for n in [e[1] for e in edges if e[0] == node]:
                if (edge_len := find_edge_length((node[0]-1, node[1]), n)) and tiles[node[0]-1][node[1]] != '#':
                    direction['U'] = n
                elif (edge_len := find_edge_length((node[0], node[1]+1), n)) and tiles[node[0]][node[1]+1] != '#':
                    direction['R'] = n
                elif (edge_len := find_edge_length((node[0]+1, node[1]), n)) and tiles[node[0]+1][node[1]] != '#':
                    direction['D'] = n
                elif (edge_len := find_edge_length((node[0], node[1]-1), n)) and tiles[node[0]][node[1]-1] != '#':
                    direction['L'] = n
            if not direction['U']:
                del edges[(node,direction['L'])]
            if not direction['R']:
                del edges[(node,direction['U'])]
            if not direction['D']:
                del edges[(node,direction['L'])]
            if not direction['L']:
                del edges[(node,direction['U'])]
    fronts = [(start, 0, '')]
    result = 0
    while fronts:
        new_fronts = []
        for front, step, visited in fronts:
            visited += str(front)
            next_positions = [e[1] for e in edges if e[0] == front]
            for next_pos in next_positions:
                next_step = step + edges[(front,next_pos)]
                if next_pos == destination:
                    result = max(result, next_step)
                    continue
                if str(next_pos) not in visited:
                    new_fronts.append((next_pos, next_step, visited))
        fronts = new_fronts
    print(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_23.txt', 'r')
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
