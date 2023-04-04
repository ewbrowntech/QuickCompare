"""
ctph.py

@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 4 APR 23

Perform the Context-Triggered Piecewise Hashing algorithm
"""
from block_size import compute_initial_block_size


def perform_ctph(filepath):
    signature = ""
    initial_block_size = compute_initial_block_size(filepath)
    
    return signature
