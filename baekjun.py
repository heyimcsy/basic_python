import math
import heapq
import sys
from io import StringIO

# 백준 31860
test_input ="""2 5 3
10
18"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N, M, K = map(int, sys.stdin.readline().split(" "))
count = 0
satisfy = 0
satisfy_list = []
works = []
for i in range(N):
    work = int(sys.stdin.readline().strip())
    works.append(-work)

heapq.heapify(works)
while -works[0] > K:
    count += 1
    max_work = -heapq.heappop(works)
    satisfy = math.trunc((satisfy / 2) + max_work)
    satisfy_list.append(satisfy)
    max_work = max_work - M
    heapq.heappush(works, -max_work)

print(count)
print(*satisfy_list, sep='\n')

