"""
ctph.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 7 APR 23

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
        tracker1 = []
        signature2 = ""
        tracker2 = []
        indexer1 = 0
        indexer2 = 0

        with open(filepath, "rb") as file:
            while byte := file.read(1):
                byte = int.from_bytes(byte, byteorder='big')
                rolling_hash.update_rolling_hash(byte)
                traditional_hash1.update_hash(byte)
                traditional_hash2.update_hash(byte)
                if rolling_hash.hash % block_size == block_size - 1:
                    fnv_hash = str(hex(traditional_hash1.ls6b % 64)[2:])
                    signature1 += fnv_hash
                    tracker1.append({
                        "hash": fnv_hash,
                        "start": indexer1,
                        "end": file.tell() - 1
                    })
                    indexer1 = file.tell() - 1
                    traditional_hash1 = FNV_Hash()

                if rolling_hash.hash % (2 * block_size) == (2 * block_size) - 1:
                    fnv_hash = str(hex(traditional_hash2.ls6b % 64)[2:])
                    signature2 += fnv_hash
                    tracker2.append({
                        "hash": fnv_hash,
                        "start": indexer2,
                        "end": file.tell() - 1
                    })
                    indexer2 = file.tell() - 1
                    traditional_hash2 = FNV_Hash()
            file.close()

        if len(signature1) < 32:
            block_size = block_size / 2
        else:
            done = True

    signature = {
        "block_size": block_size,
        "signature1": signature1,
        "signature2": signature2,
        "tracker1": tracker1,
        "tracker2": tracker2
    }
    return signature
