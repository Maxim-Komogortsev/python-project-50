#!/usr/bin/env/python3

from gendiff import generate_diff
import argparse


DESCRIPTION = "Compares two configuration files and shows the difference"


def create_parcer():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        'first_file',
        type=str,
        metavar='first_file'
    )
    parser.add_argument(
        'second_file',
        type=str,
        metavar='second_file'
    )
    parser.add_argument(
        '-f', '--format',
        metavar='FORMAT',
        default='stylish',
        choices=('stylish', 'plain', 'json'),
        help='set format of output (default: stylish)'
    )
    return parser


def main():
    parser = create_parcer()
    args = parser.parse_args()
    diff = generate_diff(
        args.first_file,
        args.second_file,
        args.format
    )
    print(diff)


if __name__ == '__main__':
    main()
