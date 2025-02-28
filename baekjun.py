import math
from io import StringIO
import sys
from itertools import combinations

# 백준 1676
test_input = """10"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())
count = 0
if N <= 1:
    print(0)
else:
    for i in range(1, N):
        N = N * i
    number = list(str(N))

    for i in range(len(number)-1, -1, -1):
        char = number[i]
        if char == '0':
            count += 1
        else:
            break
    print(count)