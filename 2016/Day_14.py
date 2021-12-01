import argparse
import hashlib
import re


def simple_md5_hash(string):
    m = hashlib.new('md5')
    m.update(string.encode())
    return m.hexdigest()


def stretched_md5_hash(string):
    for i in range(2016):
        string = simple_md5_hash(string)
    return string


def get_keys(salt, part=1):
    index = 0
    keys = []
    key_candidates = []
    while len(keys) < 64:
        new_key_candidate = salt + str(index)
        new_hash = simple_md5_hash(new_key_candidate)
        if part == 2:
            new_hash = stretched_md5_hash(new_hash)

        removing_candidates = []
        for candidate in key_candidates:
            if index - candidate[0] > 1000:
                removing_candidates.append(candidate)
                continue

            if candidate[1] in new_hash:
                keys.append((candidate[0], simple_md5_hash(salt + str(candidate[0]))))
                removing_candidates.append(candidate)
                continue

        new_key_candidates = []
        for kc in key_candidates:
            if kc not in removing_candidates:
                new_key_candidates.append(kc)

        key_candidates = new_key_candidates
        if char := re.findall(r"(\w)\1\1", new_hash):
            key_candidates.append((index, char[0] * 5))

        index += 1

    return keys


def part_1(salt):
    keys = sorted(get_keys(salt, part=1), key=lambda k: k[0])
    print(keys[63][0])


def part_2(salt):
    keys = sorted(get_keys(salt, part=2), key=lambda k: k[0])
    print(keys[63][0])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    salt = 'ihaygndm'

    if args.part == '1':
        part_1(salt)
    elif args.part == '2':
        part_2(salt)
    else:
        part_1(salt)
        part_2(salt)


if __name__ == "__main__":
    main()
