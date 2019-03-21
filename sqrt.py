# Given an integral number, determine if it is a square numbers

import math

def is_square(n):
    return n >= 0 and math.sqrt(n) % 1 == 0
