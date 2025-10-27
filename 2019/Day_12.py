import argparse
import re

from itertools import combinations
from math import lcm


def parse_data(input_string):
    moons = []
    for x, y, z in re.findall(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>", input_string):
        x, y, z = tuple(map(int, (x, y, z)))
        moons.append({
            'pos': (x, y, z),
            'vel': (0, 0, 0)
        })
    return moons


def step_movement(moons):
    for i in range(3):
        for m0, m1 in combinations(moons, 2):
            if m0['pos'][i] < m1['pos'][i]:
                m0['vel'] = list(m0['vel'])
                m0['vel'][i] += 1
                m0['vel'] = tuple(m0['vel'])
                m1['vel'] = list(m1['vel'])
                m1['vel'][i] -= 1
                m1['vel'] = tuple(m1['vel'])
            elif m0['pos'][i] > m1['pos'][i]:
                m0['vel'] = list(m0['vel'])
                m0['vel'][i] -= 1
                m0['vel'] = tuple(m0['vel'])
                m1['vel'] = list(m1['vel'])
                m1['vel'][i] += 1
                m1['vel'] = tuple(m1['vel'])
    for m in moons:
        m['pos'] = tuple(m['pos'][i]+m['vel'][i] for i in range(3))
    return moons


def one_d_step_movement(moons):
    for m0, m1 in combinations(moons, 2):
        if m0['pos'] < m1['pos']:
            m0['vel'] += 1
            m1['vel'] -= 1
        elif m0['pos'] > m1['pos']:
            m0['vel'] -= 1
            m1['vel'] += 1
    for m in moons:
        m['pos'] += m['vel']
    return moons


def part_1(input_string):
    moons = parse_data(input_string)
    for _ in range(1000):
        moons = step_movement(moons)
    result = 0
    for m in moons:
        result += (sum([abs(p) for p in m['pos']])*sum([abs(v) for v in m['vel']]))
    print(result)


def part_2(input_string):
    repetitions = [0 for _ in range(3)]
    for i in range(3):
        moons = parse_data(input_string)
        moons = [{'pos': m['pos'][i], 'vel': 0} for m in moons]
        initial_moons = str(moons)
        repetition = 0
        while True:
            repetition += 1
            moons = one_d_step_movement(moons)
            if str(moons) == initial_moons:
                repetitions[i] = repetition
                break
    print(lcm(*repetitions))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_12.txt', 'r')
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
