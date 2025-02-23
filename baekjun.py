from io import StringIO

import sys
import heapq

# 백준 10813
test_input ="""5 4
1 2
3 4
1 4
2 2"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)
N, M = map(int, sys.stdin.readline().split())

baskets = {i: i for i in range(1, N + 1)}
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    baskets[i], baskets[j] = baskets[j], baskets[i]
print(*baskets.values())