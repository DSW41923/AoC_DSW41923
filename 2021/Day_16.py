import argparse

from functools import reduce


def parse_packet(transmission, parsed_packets, max_packet=None, is_sub_packet=False):
    i, c = 0, 0
    while c != max_packet and i <= len(transmission) - 11:
        c += 1
        version = int(transmission[i:i + 3], 2)
        type_id = int(transmission[i + 3:i + 6], 2)

        if type_id == 4:
            content = ''
            for j in range(i+6, len(transmission), 5):
                content += transmission[j:j + 5]
                if content[-5] == '0':
                    parsed_packets.append({
                        'version': version,
                        'type': type_id,
                        'content': content,
                        'sub_packets': []
                    })
                    if is_sub_packet:
                        i = i + (6 + len(content))
                    else:
                        i = i + (6 + len(content)) + (4 - (6 + len(content)) % 4)
                    break
            continue

        length_type_id = int(transmission[i + 6])
        if length_type_id == 0:
            length = int(transmission[i + 7:i + 22], 2)
            content = transmission[i + 22:i + 22 + length]
            sub_packets = []
            parse_packet(content, sub_packets, is_sub_packet=True)
            new_parsed_packet = {
                'version': version,
                'type': type_id,
                'content': content,
                'sub_packets': sub_packets
            }
            parsed_packets.append(new_parsed_packet)
            i = i + 22 + length

        if length_type_id == 1:
            max_sub_packets = int(transmission[i + 7:i + 18], 2)
            content = transmission[i + 18:]
            sub_packets = []
            parsed_length = parse_packet(content, sub_packets, max_sub_packets, is_sub_packet=True)
            content = transmission[i + 18: i + 18 + parsed_length]
            new_parsed_packet = {
                'version': version,
                'type': type_id,
                'content': content,
                'sub_packets': sub_packets
            }

            parsed_packets.append(new_parsed_packet)
            i = i + 18 + parsed_length

    return i


def sum_version(packets):
    version_sum = 0
    for packet in packets:
        version_sum += packet['version']
        version_sum += sum_version(packet['sub_packets'])

    return version_sum


def update_packet_value(packets):
    for packet in packets:
        if packet['type'] == 0:
            update_packet_value(packet['sub_packets'])
            packet.update({
                'value': sum(p['value'] for p in packet['sub_packets'])
            })

        if packet['type'] == 1:
            update_packet_value(packet['sub_packets'])
            packet.update({
                'value': reduce(lambda x, y: x*y, [p['value'] for p in packet['sub_packets']])
            })
        if packet['type'] == 2:
            update_packet_value(packet['sub_packets'])
            packet.update({
                'value': min(p['value'] for p in packet['sub_packets'])
            })
        if packet['type'] == 3:
            update_packet_value(packet['sub_packets'])
            packet.update({
                'value': max(p['value'] for p in packet['sub_packets'])
            })
        if packet['type'] == 4:
            packet.update({
                'value': int(''.join([packet['content'][i] for i in range(len(packet['content'])) if i % 5 != 0]), 2)
            })
        if packet['type'] == 5:
            update_packet_value(packet['sub_packets'])
            packet.update({
                'value': 1 if packet['sub_packets'][0]['value'] > packet['sub_packets'][1]['value'] else 0
            })
        if packet['type'] == 6:
            update_packet_value(packet['sub_packets'])
            packet.update({
                'value': 1 if packet['sub_packets'][0]['value'] < packet['sub_packets'][1]['value'] else 0
            })
        if packet['type'] == 7:
            update_packet_value(packet['sub_packets'])
            packet.update({
                'value': 1 if packet['sub_packets'][0]['value'] == packet['sub_packets'][1]['value'] else 0
            })


def part_1(input_string):
    transmission = ''.join(map(lambda x: bin(int(x, 16))[2:].zfill(4), list(input_string)))
    parsed_packets = []
    parse_packet(transmission, parsed_packets)
    print(sum_version(parsed_packets))


def part_2(input_string):
    transmission = ''.join(map(lambda x: bin(int(x, 16))[2:].zfill(4), list(input_string)))
    parsed_packets = []
    parse_packet(transmission, parsed_packets)
    update_packet_value(parsed_packets)
    print(parsed_packets[0]['value'])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    input_string = "020D64AEE52E55B4C017938FBBAC2D6002A53D21F9E90C18023600B80021D0862DC17000432" \
                   "32C2284D3B0105007251DE33CF281802D0E7001A0958C3B6EB542D2014340010B89112E2288" \
                   "03518E2047E0004322B4128352DFE72BFE1CC77000E226B92FF7F7F0F4899CCEB788FBA632A" \
                   "444019349E40A801CA941898B661ECBC40820061A78E254024C126797B31A804B27C0582B2D" \
                   "7D4AF02791E431531100B2458A6219D29CB6C4247F7D6DB27BCBA4065138014C05B00801CC0" \
                   "513280108047020106460079801000332200B60002832801C200718012801503801A800B028" \
                   "01723F9B90009D6600D44A87B0CC8010B89D0661F980331F20A44470076767F8EF75AA94F5E" \
                   "1E6E9790C9008BF801AB8002171CA2A45C100661FC508B911C8043EC00C224BB8A753A6677F" \
                   "DB7B8EA85932F4600BE0039138612F684AB86392889C4A201253C013100623D464834200CC1" \
                   "787D09E76FC78200A16603A543E6D9E695E4C74C012D004646D08CAF74391B4232BDD1E4FFE" \
                   "E033805B3DAB074ACF351399FCCEA5F592697E1CB802B2D1D0BCFE410C015B004E46BE17973" \
                   "C949C213153005A6932C0129BDF675DD2CBF3482401BE7802D37AA4DFE6F549BD4A42363A20" \
                   "0D5F40149985FEDF2ACF35AB4BD3003004A730F74019B8803F08A0943B1007A21C2487C0002" \
                   "DC578BC600A497B35A8050020F24432444401415002AF07A7F7FE004DB93001A931FC33A802" \
                   "B37FB517A4A52254010E2374C637895BF7E5CC66F53EB0CC2F4C92080292B1E7A0DB26BE600" \
                   "8CE1ACC801804938F530A1227F2A6A4004349A31009F7801A900021908A18C5D100722C43C8" \
                   "F9312CFD4040269934949661E0096FE75092ACA4F0B6A005CD6CBE1218027258AA3F0043937" \
                   "7F5D566E338D121C0239DD9C4942FA4E8F73DFA62656402704E523896FAE9E00B4E779DE6BF" \
                   "15595C56DBF0ACD391802F400FA4FEADD769FD5BAE7318FCF32AB8"

    if args.part == '1':
        part_1(input_string)
    elif args.part == '2':
        part_2(input_string)
    else:
        part_1(input_string)
        part_2(input_string)


if __name__ == "__main__":
    main()
