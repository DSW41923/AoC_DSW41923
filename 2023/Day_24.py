import argparse
import re

from decimal import *
from itertools import combinations


def part_1(input_string):
    hailstones = []
    for px, py, pz, vx, vy, vz in re.findall(r"(\d+), (\d+), (\d+) @ +([\d\-]+), +([\d\-]+), +([\d\-]+)", input_string):
        hailstones.append({
            'px': int(px),
            'py': int(py),
            'pz': int(pz),
            'vx': int(vx),
            'vy': int(vy),
            'vz': int(vz)
        })
    min_xy = 200000000000000
    max_xy = 400000000000000
    intersection = 0
    for hailstone0, hailstone1 in combinations(hailstones, 2):
        if hailstone0['vx'] * hailstone1['vy'] == hailstone0['vy'] * hailstone1['vx']:
            continue
        delta = hailstone0['vx'] * (-hailstone1['vy']) - hailstone0['vy'] * (-hailstone1['vx'])
        constant_0 = hailstone1['px'] - hailstone0['px']
        constant_1 = hailstone1['py'] - hailstone0['py']
        t = (constant_0 * (-hailstone1['vy']) - constant_1 * (-hailstone1['vx']))/delta
        s = (hailstone0['vx'] * constant_1 - hailstone0['vy'] * constant_0)/delta
        if (t > 0 and s > 0 and
            min_xy <= (hailstone0['px']+t*hailstone0['vx']) <= max_xy and
            min_xy <= (hailstone0['py']+t*hailstone0['vy']) <= max_xy):
            intersection += 1
    print(intersection)


def part_2(input_string):
    hailstones = []
    for px, py, pz, vx, vy, vz in re.findall(r"(\d+), (\d+), (\d+) @ +([\d\-]+), +([\d\-]+), +([\d\-]+)", input_string):
        hailstones.append({
            'px': Decimal(px),
            'py': Decimal(py),
            'pz': Decimal(pz),
            'vx': Decimal(vx),
            'vy': Decimal(vy),
            'vz': Decimal(vz)
        })
    coeffs = []
    for i in range(2):
        d0yz = hailstones[i]['pz']*hailstones[i]['vy']-hailstones[i]['py']*hailstones[i]['vz']
        d0zx = hailstones[i]['px']*hailstones[i]['vz']-hailstones[i]['pz']*hailstones[i]['vx']
        d0xy = hailstones[i]['py']*hailstones[i]['vx']-hailstones[i]['px']*hailstones[i]['vy']
        d1yz = hailstones[i+1]['pz']*hailstones[i+1]['vy']-hailstones[i+1]['py']*hailstones[i+1]['vz']
        d1zx = hailstones[i+1]['px']*hailstones[i+1]['vz']-hailstones[i+1]['pz']*hailstones[i+1]['vx']
        d1xy = hailstones[i+1]['py']*hailstones[i+1]['vx']-hailstones[i+1]['px']*hailstones[i+1]['vy']
        coeffs.append([hailstones[i+1]['vz']-hailstones[i]['vz'], 0, hailstones[i]['vx']-hailstones[i+1]['vx'], 
                       hailstones[i]['pz']-hailstones[i+1]['pz'], 0, hailstones[i+1]['px']-hailstones[i]['px'],
                       d1zx-d0zx])
        coeffs.append([hailstones[i]['vy']-hailstones[i+1]['vy'], hailstones[i+1]['vx']-hailstones[i]['vx'], 0, 
                       hailstones[i+1]['py']-hailstones[i]['py'], hailstones[i]['px']-hailstones[i+1]['px'], 0,
                       d1xy-d0xy])
        coeffs.append([0, hailstones[i]['vz']-hailstones[i+1]['vz'], hailstones[i+1]['vy']-hailstones[i]['vy'], 
                       0, hailstones[i+1]['pz']-hailstones[i]['pz'], hailstones[i]['py']-hailstones[i+1]['py'],
                       d1yz-d0yz])
    coeffs[1], coeffs[4] = coeffs[4], coeffs[1]
    result = [0 for _ in range(len(coeffs))]
    # Gauss Elimination
    for i in range(len(coeffs)):
        if coeffs[i][i] == 0.0:
            continue
            
        for j in range(i+1, len(coeffs)):
            ratio = coeffs[j][i]/coeffs[i][i]
            
            for k in range(len(coeffs)+1):
                coeffs[j][k] = coeffs[j][k] - ratio * coeffs[i][k]

    # Back Substitution
    result[len(coeffs)-1] = coeffs[len(coeffs)-1][len(coeffs)]/coeffs[len(coeffs)-1][len(coeffs)-1]

    for i in range(len(coeffs)-2,-1,-1):
        result[i] = coeffs[i][len(coeffs)]
        
        for j in range(i+1,len(coeffs)):
            result[i] = result[i] - coeffs[i][j]*result[j]
        if coeffs[i][i]:
            result[i] = result[i]/coeffs[i][i]
    print(int(result[0]+result[1]+result[2]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('Input_24.txt', 'r')
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
