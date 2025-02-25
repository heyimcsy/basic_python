import math
from io import StringIO
import sys

# 백준 10250
test_input = """2
6 12 18
30 50 72"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

M = int(sys.stdin.readline())

for _ in range(M):
    H, W, N = map(int, sys.stdin.readline().split())
    Y = H if N % H == 0 else N % H
    X = N // H if N % H == 0 else N // H + 1

    print(f"{Y}{X:02d}")
