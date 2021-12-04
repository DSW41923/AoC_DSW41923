import argparse


def get_last_elf(elves_num):
    # Mathematically solve for part 2 rules
    last_elf = 0
    for i in range(1, elves_num+1):
        if last_elf + 1 < i // 2:
            last_elf = (last_elf + 1) % i
            continue

        if last_elf + 1 >= i // 2:
            last_elf = (last_elf + 2) % i
            continue

    return last_elf + 1


def part_1(elves_num):
    elves = list(range(elves_num))
    while len(elves) > 1:
        previous_elves_num = len(elves)
        elves = elves[::2]
        if previous_elves_num % 2 == 1:
            elves = elves[1:]

    print(elves[0] + 1)


def part_2(elves_num):
    print(get_last_elf(elves_num))
    # Below is another way to solve this part.
    # Theoretically correct, but take too much time to run.
    # And very slow!
    # elves = list(range(elves_num))
    # stealing_elf_num = 0
    # while len(elves) > 1:
    #     stealed_elf_index = (elves.index(stealing_elf_num) + len(elves) // 2) % len(elves)
    #     del elves[stealed_elf_index]
    #     stealing_elf_num = elves[(elves.index(stealing_elf_num) + 1) % len(elves)]
    #
    # print(elves[0] + 1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    elves_num = 3018458

    if args.part == '1':
        part_1(elves_num)
    elif args.part == '2':
        part_2(elves_num)
    else:
        part_1(elves_num)
        part_2(elves_num)


if __name__ == "__main__":
    main()
