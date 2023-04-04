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
    arg_parser.add_argument('filepath1')
    arg_parser.add_argument('filepath2')
    args = arg_parser.parse_args()

    print("Target File:\t" + args.filepath1)
    print("Reference File:\t" + args.filepath2)

    block_size = compute_initial_block_size()


if __name__ == '__main__':
    main()
