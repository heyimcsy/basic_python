import math
from io import StringIO
import sys
import heapq

# 백준 1927
test_input = """9
0
12345678
1
2
0
0
0
0
32"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())

numbers = []
for _ in range(N):
    number = int(sys.stdin.readline())
    if number == 0:
        if len(numbers):
            n = heapq.heappop(numbers)
            print(n)
        else:
            print(0)
    else:
        heapq.heappush(numbers, number)
