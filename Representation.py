import string
import random

class String:
    def __init__(self, binary_str) -> None:
        self.binary_str = binary_str

    def count_ones(self):
        return self.binary_str.count('1')
    
    def trap(self):
        pass
    
    def __repr__(self) -> str:
        return self.binary_str
