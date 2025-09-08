import argparse


# def parse_tree_data(data, sub_tree_count):
#     if len(data) == 0:
#         return 0, 0
#     if sub_tree_count == 0:
#         child_count = data[0]
#         metadata_count = data[1]
#         result = sum(data[2:2+metadata_count])
#         return 2+metadata_count, result
#     total_sub_tree_data_len = 0
#     metadata_count = 0
#     result = 0
#     for _ in range(sub_tree_count):
#         child_count = data[0]
#         metadata_count = data[1]
#         sub_tree_data_len, result = parse_tree_data(data[2:], child_count)
#         total_sub_tree_data_len += sub_tree_data_len
#         result += sum(data[sub_tree_data_len:sub_tree_data_len+metadata_count])
#         data = data[sub_tree_data_len:]
#     return 2+total_sub_tree_data_len+metadata_count, result


class Tree:
    def __init__(self, child_count, metadata_count):
        self.children = []
        self.child_count = child_count
        self.metadata = []
        self.metadata_count = metadata_count
        self.value = None

    def __str__(self):
         return str((self.child_count, len(self.children), self.metadata_count, self.metadata))

    def set_metadata(self, metadata):
        self.metadata = metadata

    def add_child(self, node):
        self.children.append(node)

    def add_children(self, nodes):
        self.children.extend(nodes)

    def evaluate_value(self):
        if self.child_count == 0:
            self.value = sum(self.metadata)
        else:
            self.value = 0
            for m in self.metadata:
                if 0 < m <= self.child_count:
                    if not self.children[m-1].value:
                        self.children[m-1].evaluate_value()
                    self.value += self.children[m-1].value


def part_1(input_string):
    data = list(map(int, input_string.split(' ')))
    result = 0
    trees = [(data[0], data[1])]
    cur = 2
    while cur < len(data):
        if trees[-1][0] > 0:
            child_count = data[cur+0]
            metadata_count = data[cur+1]
            trees.append((child_count, metadata_count))
            cur += 2
        else:
            child_count, metadata_count = trees.pop()
            result += sum(data[cur:cur+metadata_count])
            if trees:
                trees[-1] = (trees[-1][0]-1, trees[-1][1])
            cur += metadata_count

    print(result)


def part_2(input_string):
    data = list(map(int, input_string.split(' ')))
    nodes = [(Tree(data[0], data[1]), data[0], data[1])]
    root = None
    cur = 2
    while cur < len(data):
        if nodes[-1][1] > 0:
            child_count = data[cur+0]
            metadata_count = data[cur+1]
            nodes.append((Tree(child_count, metadata_count), child_count, metadata_count))
            cur += 2
        else:
            node, child_count, metadata_count = nodes.pop()
            metadata = data[cur:cur+metadata_count]
            node.set_metadata(metadata)
            if nodes:
                nodes[-1][0].add_child(node)
                nodes[-1] = (nodes[-1][0], nodes[-1][1]-1, nodes[-1][2])
            else:
                root = node
            cur += metadata_count

    root.evaluate_value()
    print(root.value)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2018/Input_08.txt', 'r')
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
