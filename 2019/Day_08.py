import argparse


def part_1(input_string):
    img_w = 25
    img_h = 6
    img_bit = img_w * img_h
    min_layer = None
    min_count = img_bit
    for i in range(len(input_string)//img_bit):
        cur_layer = list(input_string[i*img_bit:(i+1)*img_bit])
        cur_layer_count = cur_layer.count('0')
        if cur_layer_count < min_count:
            min_layer = cur_layer
            min_count = cur_layer_count
    print(min_layer.count('1')*min_layer.count('2'))


def part_2(input_string):
    img_w = 25
    img_h = 6
    img_bit = img_w * img_h
    layers = []
    for i in range(len(input_string)//img_bit):
        layers.append(list(input_string[i*img_bit:(i+1)*img_bit]))
    img = [[-1 for _ in range(img_w)] for _ in range(img_h)]
    for h in range(img_h):
        for w in range(img_w):
            pixel_id = h*img_w+w
            pixels = [l[pixel_id] for l in layers]
            for p in pixels:
                if p == '2':
                    continue
                if p == '0':
                    img[h][w] = '#'
                    break
                if p == '1':
                    img[h][w] = '.'
                    break
            if img[h][w] not in ['#', '.']:
                print(h, w, pixel_id, pixels)
    print('\n'.join(list(map(lambda i:''.join(i), img))))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2019/Input_08.txt', 'r')
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
