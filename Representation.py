import string
import random

class String:
    def __init__(self, binary_str) -> None:
        self.binary_str = binary_str

    def count(self, s):
        return self.binary_str.count(s)

    def __repr__(self) -> str:
        return self.binary_str

def count_ones(binary_str: String):
    print(binary_str)
    return binary_str.count('1')

def trap(self):
    pass
