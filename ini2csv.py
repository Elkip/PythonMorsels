"""
    About: accepts an INI-like file and converts it to a CSV-like file
    Running: python ini2csv.py --collapsed [input file] [output file]

import sys


# simple way with no optinal arguments
def ini2csv():
    ini_filename, csv_filename = sys.argv[1:]

    with open(ini_filename) as ini_file:
        with open(csv_filename, mode="wt") as csv_file:
            for line in ini_file:
                if line.startswith("["):
                    # Remove brackets
                    section = line.strip()[1:-1]
                elif line.strip():
                    attr, value = line.split("=")
                    attr = attr.strip()
                    value = value.strip()
                    csv_file.write(f'{section},{attr},{value}\n')
"""

from argparse import ArgumentParser
from configparser import ConfigParser
import csv


def ini2csv():
    # argparse module is a user friendly way to parse command line args
    parser = ArgumentParser()
    parser.add_argument('ini_file')
    parser.add_argument('csv_file')
    # If the flag '--collapsed' is present store true
    parser.add_argument('--collapsed', action='store_true')
    args = parser.parse_args()
    print(args)

    config = ConfigParser()
    config.read(args.ini_file)

    print(config.sections())

    headers = None
    rows = []

    for name, section in config.items():
        if name == 'DEFAULT':
            continue
        if args.collapsed:
            if headers is None:
                headers = ['header', *section.keys()]
            rows.append([name, *section.values()])
        else:
            for key, value in section.items():
                rows.append([name, key, value])
    print(headers)
    print(rows)

    with open(args.csv_file, mode='wt') as csv_file:
        csv_writer = csv.writer(csv_file)
        if args.collapsed:
            csv_writer.writerow(headers)
        csv_writer.writerows(rows)


def main():
    ini2csv()


if __name__ == "__main__":
    main()
