"""
block_size.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 4 APR 23

Compute the initial block size for the algorithm
"""
import math
import os


def compute_initial_block_size(filepath):
    filesize = os.stat(filepath).st_size
    min_block_size = 3
    ss_length = 64

    initial_block_size = min_block_size * math.pow(2, (math.log2(filesize / (ss_length * min_block_size))))
    return initial_block_size
