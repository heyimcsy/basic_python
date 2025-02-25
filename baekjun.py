import math
from io import StringIO
import sys

# 백준 2475
test_input = """0 4 2 5 6"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

def cal(x):
    return int(x) ** 2

M = list(map(cal, sys.stdin.readline().split()))
print(sum(M) % 10)
