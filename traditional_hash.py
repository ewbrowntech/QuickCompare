"""
traditional_hash.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 4 APR 23

Compute 32-bit FNV hash and preserve the LS6B
"""


class FNV_Hash:
    def __init__(self):
        self.hash = None
        self.ls6b = None
