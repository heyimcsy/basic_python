import sys
import heapq
from collections import deque
from io import StringIO

# 테스트 입력을 문자열로 제공
test_input ="""5
0
2 3 2
0
0
0"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

# text = sys.stdin.read().splitlines()
# gifts = []
# heap = [-n for n in list(gifts)]
# N = int(text[0])
# for t in text[1:1+N]:
#     if t == '0':
#         if len(heap):
#             print(-heapq.heappop(heap))
#         else:
#             print(-1)
#     else:
#         for i in t.split()[1:]:
#             heapq.heappush(heap, -int(i))

text = sys.stdin.read().splitlines()
heap = []
N = int(text[0])
for t in text[1:1+N]:
    if t == '0':
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(-1)
    else:
        # push 방식을 유지
        for num in map(int, t.split()[1:]):
            heapq.heappush(heap, -num)  # 최대 힙 유지 (음수 변환)