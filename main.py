"""
main.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 4 APR 23

Run the CTPH algorithm
"""
import argparse


def main():
    arg_parser = argparse.ArgumentParser(add_help=False)
    arg_parser.add_argument('filepath1')
    arg_parser.add_argument('filepath2')
    args = arg_parser.parse_args()

    print("Target File:\t" + args.filepath1)
    print("Reference File:\t" + args.filepath2)
    print()


if __name__ == '__main__':
    main()
