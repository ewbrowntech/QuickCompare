"""
ctph.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 6 APR 23

Perform the Context-Triggered Piecewise Hashing algorithm
"""
from block_size import compute_initial_block_size
from rolling_hash import RollingHash
from traditional_hash import FNV_Hash


# Implement the spamsum algorithm described by Jesse Kornblum in
# "Identifying Almost Identical Files using Context Triggered Piecewise Hashing"
# https://doi.org/10.1016/j.diin.2006.06.015
def perform_ctph(filepath):
    block_size = compute_initial_block_size(filepath)

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
                traditional_hash1.update_hash(byte)
                traditional_hash2.update_hash(byte)
                if rolling_hash.hash % block_size == block_size - 1:
                    signature1 += str(hex(traditional_hash1.ls6b % 64)[2:])
                    traditional_hash1 = FNV_Hash()

                if rolling_hash.hash % (2 * block_size) == (2 * block_size) - 1:
                    signature2 += str(hex(traditional_hash2.ls6b % 64)[2:])
                    traditional_hash2 = FNV_Hash()
            file.close()

        if len(signature1) < 32:
            block_size = block_size / 2
        else:
            done = True

    return str(block_size) + " : " + signature1 + " : " + signature2
