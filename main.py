"""
main.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 4 APR 23

Run the CTPH algorithm
"""
import argparse
from block_size import compute_initial_block_size
from ctph import perform_ctph


def main():
    arg_parser = argparse.ArgumentParser(add_help=False)
    arg_parser.add_argument('-i', '--ibs', action='store_true')
    arg_parser.add_argument('-s', '--signature', action='store_true')
    arg_parser.add_argument('filepath1')
    arg_parser.add_argument('filepath2')
    args = arg_parser.parse_args()

    # target = open(args.filepath1, "rb")
    print("Target File:\t" + args.filepath1)
    # reference = open(args.filepath2, "rb")
    print("Reference File:\t" + args.filepath2)
    print()

    if args.ibs:
        print("----- Initial Block Size -----")
        initial_block_size = compute_initial_block_size(args.filepath1)
        print("Target Initial Block Size:\t" + str(initial_block_size))
        initial_block_size = compute_initial_block_size(args.filepath2)
        print("Reference Initial Block Size:\t" + str(initial_block_size))
        print("\n")

    target_signature = perform_ctph(args.filepath1)
    reference_signature = perform_ctph(args.filepath2)
    if args.signature:
        print("--------- Signatures ---------")
        print("Target Signature:")
        print_signature(target_signature)
        print("\nReference Signature:")
        print_signature(reference_signature)
        print("\n")


def print_signature(signature):
    print(str(signature["block_size"]) + " : " + signature["signature1"] + " : " + signature["signature2"])


if __name__ == '__main__':
    main()
