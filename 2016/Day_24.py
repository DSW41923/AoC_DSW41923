import argparse
import itertools


def get_points_data(map_data):
    visitable_points = []
    target_points = {}
    for x, row_points in enumerate(map_data):
        for y, point in enumerate(row_points):
            if point == '#':
                continue

            if point.isdigit():
                target_points.update({point: (x, y)})
                continue

            if point == '.':
                visitable_points.append((x, y))
                continue

            raise

    return visitable_points, target_points


def get_graph(visitable_points, target_points):
    max_x, max_y = max([p[0] for p in visitable_points]), max([p[1] for p in visitable_points])

    graph = {}
    for point_index, start in target_points.items():
        front_points = [start]
        visited_points = [start]
        graph_data = {}
        steps = 1
        while len(graph_data) < len(target_points) - 1:

            new_front_points = []
            for fp_x, fp_y in front_points:
                next_points = [(x, y) for x, y in
                               [(fp_x - 1, fp_y), (fp_x + 1, fp_y), (fp_x, fp_y - 1), (fp_x, fp_y + 1)]
                               if 0 < x <= max_x and 0 < y <= max_y]
                for next_point in next_points:

                    if next_point not in visited_points + new_front_points:

                        for i, target_point in target_points.items():
                            if next_point == target_point:
                                graph_data.update({i: steps})
                                visited_points.append(next_point)

                        if next_point not in visitable_points:
                            continue

                        new_front_points.append(next_point)

            front_points = new_front_points
            visited_points.extend(front_points)
            steps += 1

        graph.update({point_index: graph_data})

    return graph


def get_all_routes(points, start='', end=''):
    other_points = [p for p in points if p != start]
    return map(lambda r: tuple(start + ''.join(r) + end), itertools.permutations(other_points))


def get_min_route(routes, graph):
    min_route = ''
    min_route_steps = 1000
    for route in routes:
        if route[0] != '0':
            continue

        route_steps = 0
        for p in range(len(route) - 1):
            route_steps += graph[route[p]][route[p + 1]]
        if route_steps < min_route_steps:
            min_route_steps = route_steps
            min_route = ''.join(route)

    return min_route, min_route_steps


def part_1(input_string):
    map_data = input_string.split('\n')
    visitable_points, target_points = get_points_data(map_data)
    graph = get_graph(visitable_points, target_points)
    all_routes = get_all_routes(target_points.keys(), start='0')
    min_route, min_route_steps = get_min_route(all_routes, graph)
    print(min_route, min_route_steps)


def part_2(input_string):
    map_data = input_string.split('\n')
    visitable_points, target_points = get_points_data(map_data)
    graph = get_graph(visitable_points, target_points)
    all_routes = get_all_routes(target_points.keys(), start='0', end='0')
    min_route, min_route_steps = get_min_route(all_routes, graph)
    print(min_route, min_route_steps)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('../inputs/2016/Input_24.txt', 'r')
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
