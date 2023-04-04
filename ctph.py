"""
ctph.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 4 APR 23

Perform the Context-Triggered Piecewise Hashing algorithm
"""
from block_size import compute_initial_block_size
from rolling_hash import RollingHash
from traditional_hash import FNV_Hash


def perform_ctph(filepath):
    signature = ""
    block_size = compute_initial_block_size(filepath)

    done = False
    while not done:
        rolling_hash = RollingHash(block_size)
        traditional_hash1 = FNV_Hash
        traditional_hash2 = FNV_Hash
        signature1 = ""
        signature2 = ""
        
        done = True

    return signature
