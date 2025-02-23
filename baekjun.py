from io import StringIO

import sys
import heapq

# 백준 11279
test_input ="""13
0
1
2
0
0
3
2
1
0
0
0
0
0"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)


N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if not stack:
            print(0)
        else:
            print(heapq.heappop(stack) * -1)
    else:
        heapq.heappush(stack, -x)
