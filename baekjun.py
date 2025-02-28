import math
from io import StringIO
import sys

# 백준 2869
test_input = """2 1 5"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

A, B, V = map(int,sys.stdin.readline().split())

if (V - B) % (A - B) == 0:
    print((V - A) // (A - B) + 1)
else:
    print((V - A) // (A - B) + 2)