from io import StringIO

import sys
import heapq

# 백준 10810
test_input ="""5 4
1 2 3
3 4 4
1 4 1
2 2 2"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)
N, M = map(int, sys.stdin.readline().split())
baskets = {i: 0 for i in range(1, N + 1)}

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    for n in range(i, j+1):
        baskets[n] = k
print(*baskets.values())