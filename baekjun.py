import math
from io import StringIO

import sys
import heapq

# 백준 10811
test_input = """5 4
1 2
3 4
1 4
2 2"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)
N, M = map(int, sys.stdin.readline().split())

baskets = {i: i for i in range(1, N+1)}

for _ in range(M):
    f, s = map(int, sys.stdin.readline().split())
    count = math.ceil((s -f) /2)
    for i in range(count):
        baskets[f + i] , baskets[s - i] = baskets[s - i] , baskets[f + i]

print(*baskets.values())