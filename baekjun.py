import math
from io import StringIO
import sys

# 백준 2903
test_input = """5"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())

point = 2
for _ in range(N):
    point = (point * 2) - 1
print(point*point)