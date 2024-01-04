import argparse
import re


def part_1(input_string):
    input_data = input_string.split('\n')
    seeds_data, maps_data = input_data[0], input_data[2:]
    seeds = list(map(int, re.findall(r"(\d+)", seeds_data)))
    maps_data = "\n".join(maps_data).split('\n\n')
    for map_data in maps_data:
        mapping = []
        for dest, source, range_len in re.findall(r"(\d+) (\d+) (\d+)\n?", map_data):
            dest, source, range_len = tuple(map(int, (dest, source, range_len)))
            mapping.append((source, source + range_len - 1, dest))
        mapping.sort(key=lambda m:m[0])
        for i in range(len(seeds)):
            for source_low, source_high, dest in mapping:
                if source_low <= seeds[i] <= source_high:
                    seeds[i] = dest+(seeds[i]-source_low)
                    break

    print(min(seeds))


def part_2(input_string):
    input_data = input_string.split('\n')
    seeds_data, maps_data = input_data[0], input_data[2:]
    seeds = []
    for seed_start, seed_range in re.findall(r"(\d+) (\d+)", seeds_data):
        seed_start, seed_range = tuple(map(int, (seed_start, seed_range)))
        seeds.append((seed_start, seed_start + seed_range - 1))
    maps_data = "\n".join(maps_data).split('\n\n')
    for map_data in maps_data:
        converted = []
        mapping = []
        for dest, source, range_len in re.findall(r"(\d+) (\d+) (\d+)\n?", map_data):
            dest, source, range_len = tuple(map(int, (dest, source, range_len)))
            mapping.append((source, source + range_len - 1, dest))
        mapping.sort(key=lambda m:m[0])
        while seeds:
            seed_start, seed_end = seeds.pop(0)
            for mapping_id, mapping_data in enumerate(mapping):
                source_low, source_high, dest = mapping_data
                if source_high < seed_start:
                    if mapping_id == (len(mapping) - 1):
                        converted.append((seed_start, seed_end))
                        break
                    continue
                if seed_end < source_low:
                    if mapping_id == 0:
                        converted.append((seed_start, seed_end))
                        break
                elif seed_start < source_low:
                    converted.append((seed_start, source_low-1))
                    if seed_end <= source_high:
                        converted.append((dest, dest+(seed_end-source_low)))
                        break
                    else:
                        converted.append((dest, dest+(source_high-source_low)))
                        seeds.append((source_high+1, seed_end))
                        break
                else:
                    if seed_end <= source_high:
                        converted.append((dest+(seed_start-source_low), dest+(seed_end-source_low)))
                        break
                    else:
                        converted.append((dest+(seed_start-source_low), dest+(source_high-source_low)))
                        seeds.append((source_high+1, seed_end))
                        break
        seeds = converted

    seeds.sort(key=lambda m:m[0])
    print(seeds[0][0])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_05.txt', 'r')
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
