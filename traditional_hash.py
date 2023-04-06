"""
traditional_hash.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 6 APR 23

Compute 32-bit FNV hash and preserve the LS6B
"""
from struct import pack
from base64 import b64encode


class FNV_Hash:
    def __init__(self):
        self.hash = 0x811c9dc5  # Offset basis
        self.data = []
        self.ls6b = None

    def update_hash(self, byte):
        self.data.append(byte)

        # Use the FNV-1a hashing algorithm as described by Landon Noll
        # http://www.isthe.com/chongo/tech/comp/fnv/index.html#FNV-1a
        OFFSET_BASIS = 0x811c9dc5
        FNV_PRIME = 0x01000193

        self.hash = OFFSET_BASIS
        for byte in self.data:
            self.hash = self.hash ^ byte  # XOR operation
            self.hash = (self.hash * FNV_PRIME) % 2**32

        # Preserve only the LS6B, as done in spamsum
        # NOTE: While this amount of entropy is acceptable for comparing simple text, it may be insufficient for
        #       avoiding collisions when comparing something larger, like a program binary
        self.ls6b = self.hash & 0x3f

    # Encode the L6
    # def get_hash(self):
    #     packed = bytes([self.ls6b])
    #
    #     print("Packed: " + str(packed))
    #     # packed_ls6b = pack("!B", self.ls6b)  # Pack the LS6b as a single unsigned 8-bit integer in big-endian form
    #     encoded = b64encode(bytes([self.ls6b]))
    #     print(encoded)
    #     return b64encode(packed)  # Encode this integer in base 64
