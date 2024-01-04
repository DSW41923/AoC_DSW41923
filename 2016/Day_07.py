import argparse
import re


def part_1(input_string):
    tls_supported_ip_count = 0
    for ip in input_string:
        tls_supported = None
        for partial_ip in re.findall(r'[a-z]+', ip):
            if re.search(r'(\w)(?!\1)(\w)\2\1', partial_ip):
                tls_supported = True
                break
        for bracket_ip in re.findall(r'\[[a-z]+]', ip):
            if re.search(r'(\w)(?!\1)(\w)\2\1', bracket_ip):
                tls_supported = False
                break
        if tls_supported:
            tls_supported_ip_count += 1
    print("There are {} IPs in the puzzle input support TLS.".format(tls_supported_ip_count))


def part_2(input_string):
    ssl_supported_ip_count = 0
    for ip in input_string:
        bracket_ips = re.findall(r'\[([a-z]+)]', ip)
        outer_ips = [s for s in re.findall(r'[a-z]+', ip) if s not in bracket_ips]
        aba_candidates = []
        ssl_supported = False
        for outer_ip in outer_ips:
            for i in range(0, len(outer_ip)):
                partial_outer_ip = outer_ip[i:i+3]
                if re.search(r'(\w)(?!\1)(\w)\1', partial_outer_ip):
                    aba_candidates.append(partial_outer_ip)
        for aba in aba_candidates:
            bab = aba[1] + aba[0] + aba[1]
            for bracket_ip in bracket_ips:
                if bab in bracket_ip:
                    ssl_supported = True
                    break
        if ssl_supported:
            ssl_supported_ip_count += 1
    print("There are {} IPs in the puzzle input support SSL.".format(ssl_supported_ip_count))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--part",
                        help="Specify puzzle 1 or puzzle 2 to be solved. Run both by default.",
                        required=False)
    args = parser.parse_args()
    file_input = open('inputs/2016/Input_07.txt', 'r')
    input_string = file_input.readlines()
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
