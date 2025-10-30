import argparse
import re

from math import ceil


def parse_data(input_string):
    reactions = {
        "ORE": {
            'amount': 1,
            'materials': {}
        }
    }
    for materials, product in re.findall(r"([\w\d ,]+) => ([\w\d ,]+)", input_string):
        materials = materials.split(', ')
        product_amount, product_chemical = product.split(' ')
        product_amount = int(product_amount)
        reactions.update({
            product_chemical:
            {
                'amount': product_amount,
                'materials': {}
            }
        })
        for material in materials:
            material_amount, material_chemical = material.split(' ')
            material_amount = int(material_amount)
            reactions[product_chemical]['materials'].update({
                material_chemical: material_amount
            })
    for chemical in reactions:
        prior = []
        for reaction in reactions:
            if chemical in reactions[reaction]['materials']:
                prior.append(reaction)
        reactions[chemical].update({
            'prior': prior
        })
    # for k, v in reactions.items():
    #     print(k, v)
    return reactions


def retract_materials(reactions):
    retracted_chemicals = ["FUEL"]
    while len(reactions["FUEL"]['materials']) > 1:
        material_chemicals = list(reactions["FUEL"]['materials'].keys())
        # print(retracted_chemicals, material_chemicals)
        for material_chemical in material_chemicals:
            if material_chemical == "ORE" or any([p not in retracted_chemicals for p in reactions[material_chemical]["prior"]]):
                continue
            amount = reactions["FUEL"]['materials'].pop(material_chemical)
            material_reaction = reactions[material_chemical]
            multiplier = ceil(amount / material_reaction['amount'])
            for m in material_reaction['materials']:
                if m in reactions["FUEL"]['materials']:
                    reactions["FUEL"]['materials'][m] += material_reaction['materials'][m] * multiplier
                else:
                    reactions["FUEL"]['materials'][m] = material_reaction['materials'][m] * multiplier
            retracted_chemicals.append(material_chemical)
            # print(reactions["FUEL"])
        # import pdb; pdb.set_trace()
    return reactions


def part_1(input_string):
    reactions = parse_data(input_string)
    reactions = retract_materials(reactions)
    print(reactions["FUEL"]['materials']["ORE"])


def part_2(input_string):
    limit = 1000000000000
    result = 0
    result_range = (0, 0)
    usage = 0
    while True:
        reactions = parse_data(input_string)
        for m in reactions["FUEL"]['materials']:
            reactions["FUEL"]['materials'][m] *= result
        reactions = retract_materials(reactions)
        usage = reactions["FUEL"]['materials']["ORE"]
        if usage < limit and result > 0:
            result *= 2
        elif usage > limit:
            result_range = (result//2, result)
            break
        else:
            result += 1
    l, r = result_range
    while l < r:
        mid = (l+r)//2
        reactions = parse_data(input_string)
        for m in reactions["FUEL"]['materials']:
            reactions["FUEL"]['materials'][m] *= mid
        reactions = retract_materials(reactions)
        usage = reactions["FUEL"]['materials']["ORE"]
        if usage > limit:
            r = mid-1
        elif usage < limit:
            l = mid+1
        else:
            print(mid)
            break
    assert l == r
    print(r)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_14.txt', 'r')
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
