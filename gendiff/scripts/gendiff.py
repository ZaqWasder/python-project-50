import argparse
import json


def parse_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', metavar='FORMAT', choices=['plain', 'json'], help='set format of output')
    return parser.parse_args()


def main():
    args = parse_args()
    first_file = json.load(open(args.first_file))
    second_file = json.load(open(args.second_file))


if __name__ == "__main__":
    main()
