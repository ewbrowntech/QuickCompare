"""
block_size.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 4 APR 23

Compute the initial block size for the algorithm
"""
import math
import os


# The "block size" is the trigger value used in this Context-"Triggered" Piecewise Hashing algorithm.
# The initial block size is that which is computed before any of the input is read
def compute_initial_block_size(filepath):
    filesize = os.stat(filepath).st_size

    # The minimum block size represents the smallest amount of data that will be hashed at a time by the rolling hash
    MIN_BLOCK_SIZE = 3

    # The spamsum length represents the length of the signature created by the algorithm. A longer signature conveys
    # more information about its respective file, but is more computationally expensive to compare against another
    SS_LENGTH = 64

    # This is an implementation of Equation 4 in the referenced paper
    initial_block_size = MIN_BLOCK_SIZE * (2 ** (math.log2(filesize / (SS_LENGTH * MIN_BLOCK_SIZE))))

    # We will round to the nearest power of 2 to enable more efficient bitwise operations
    initial_block_size = 2 ** math.floor(math.log2(initial_block_size))

    return initial_block_size
