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
    block_size = compute_initial_block_size(filepath)
    file = open(filepath, "rb")

    done = False
    while not done:
        rolling_hash = RollingHash(block_size)
        traditional_hash1 = FNV_Hash()
        traditional_hash2 = FNV_Hash()
        signature1 = ""
        signature2 = ""

        with open(filepath, "rb") as file:
            while byte := file.read(1):
                byte = int.from_bytes(byte, byteorder='big')
                rolling_hash.update_rolling_hash(byte)
                # print("Rolling Hash: " + str("%08x" % rolling_hash.hash))
                traditional_hash1.update_hash(byte)
                traditional_hash2.update_hash(byte)
                # if rolling_hash.hash % block_size == block_size - 1:
                #     signature1 +=
            file.close()
        done = True

    return str(block_size) + " : " + signature1 + " : " + signature2
