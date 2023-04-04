"""
main.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 4 APR 23

Run the CTPH algorithm
"""
import argparse
from block_size import compute_initial_block_size


def main():
    arg_parser = argparse.ArgumentParser(add_help=False)
    arg_parser.add_argument('-i', '--ibs', action='store_true')
    arg_parser.add_argument('filepath1')
    arg_parser.add_argument('filepath2')
    args = arg_parser.parse_args()

    # target = open(args.filepath1, "rb")
    print("Target File:\t\t" + args.filepath1)
    # reference = open(args.filepath2, "rb")
    print("Reference File:\t\t" + args.filepath2)

    initial_block_size = compute_initial_block_size(args.filepath1)
    if args.ibs:
        print("Initial Block Size:\t" + str(initial_block_size))


if __name__ == '__main__':
    main()
