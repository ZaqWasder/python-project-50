import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.parse_args()

#    parser.add_argument('-h', '--help', help='show this help message and exit')


if __name__ == "__main__":
    main()
