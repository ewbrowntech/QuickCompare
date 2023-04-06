"""
rolling_hash.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 4 APR 23

Create the rolling hash used in the CTPH algorithm
"""
import array


class RollingHash:
    def __init__(self, block_size):
        self.x = 0
        self.y = 0
        self.z = 0
        self.c = 0
        self.size = block_size
        self.window = array.array('i', [0] * self.size)
        self.hash = None

    def update_rolling_hash(self, byte):
        self.y = self.y - self.x
        self.y = self.y + self.size * byte
        self.x = self.x + byte
        self.x = self.x - self.window[self.c % self.size]
        self.window[self.c % self.size] = byte
        self.c = self.c + 1
        self.z = self.z << 5
        self.z = self.z ^ byte
        self.hash = (self.x + self.y + self.z) & 0xffffffff
