import argparse


def part_1(input_string):
    terminal_outputs = input_string.split('\n')
    directories = {}
    currrent_path = ''
    for output in terminal_outputs:
        if output.startswith("$ cd "):
            next_directory = output.split(' ')[-1]
            if next_directory == '..':
                currrent_path = '/'.join(currrent_path.split('/')[:-2]) + '/'
                continue

            if next_directory == '/':
                currrent_path = '/'
                continue
            
            if currrent_path == '/':
                currrent_path += next_directory + '/'
                continue

            currrent_path += next_directory + '/'
            continue

        if output.startswith("$ ls"):
            directories.update({currrent_path: {
                'size': 0,
                'sub': []
            }})
            continue

        if output.startswith("dir "):
            new_dir = output.split(' ')[-1]
            directories[currrent_path]['sub'].append(currrent_path + new_dir + '/')
            continue
            
        size, name = output.split(' ')
        directories[currrent_path]['sub'].append(currrent_path + name)
        directories.update({currrent_path + name: {
            'size': int(size),
            'sub': []
        }})

    desired_total_size = 0
    while any([d['size'] == 0 for d in directories.values()]):
        for d in directories.values():
            if d['size'] == 0: # means its size has not yet calculated
                if all(directories[dsub]['size'] != 0 for dsub in d['sub'] if len(d['sub']) != 0):
                    # Only sum up if all child elements' size calculated
                    d['size'] = sum(directories[dsub]['size'] for dsub in d['sub'])
                    if (d['size']) <= 100000:
                        desired_total_size += d['size']
            continue
    print(desired_total_size)


def part_2(input_string):
    terminal_outputs = input_string.split('\n')
    directories = {}
    currrent_path = ''
    for output in terminal_outputs:
        if output.startswith("$ cd "):
            next_directory = output.split(' ')[-1]
            if next_directory == '..':
                currrent_path = '/'.join(currrent_path.split('/')[:-2]) + '/'
                continue

            if next_directory == '/':
                currrent_path = '/'
                continue
            
            if currrent_path == '/':
                currrent_path += next_directory + '/'
                continue

            currrent_path += next_directory + '/'
            continue

        if output.startswith("$ ls"):
            directories.update({currrent_path: {
                'size': 0,
                'sub': []
            }})
            continue

        if output.startswith("dir "):
            new_dir = output.split(' ')[-1]
            directories[currrent_path]['sub'].append(currrent_path + new_dir + '/')
            continue
            
        size, name = output.split(' ')
        directories[currrent_path]['sub'].append(currrent_path + name)
        directories.update({currrent_path + name: {
            'size': int(size),
            'sub': []
        }})

    while any([d['size'] == 0 for d in directories.values()]):
        for dir_name, d in directories.items():
            if d['size'] == 0 and all(directories[dsub]['size'] != 0 for dsub in d['sub'] if len(d['sub']) != 0):
                d['size'] = sum(directories[dsub]['size'] for dsub in d['sub'])
            continue
    
    space_total = 70000000
    space_requirement = 30000000
    space_used = directories['/']['size']
    space_freeing = space_requirement - (space_total - space_used)
    smallest_deleting_directory_size = space_total
    for dir_name, d in directories.items():
        if dir_name == '/':
            continue
        pass
        if space_freeing <= d['size'] < smallest_deleting_directory_size:
            smallest_deleting_directory_size = d['size']
        continue
    print(smallest_deleting_directory_size)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_07.txt', 'r')
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
