import sys
import heapq
from collections import deque
from io import StringIO

# 테스트 입력을 문자열로 제공
test_input ="""18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

input = sys.stdin.readline  # 빠른 입력을 위한 최적화
heap = []  # 우선순위 큐 (절댓값 기준 정렬)

N = int(input().strip())  # 연산 개수 입력
output = []  # 결과 저장 리스트

for _ in range(N):
    x = int(input().strip())

    if x != 0:
        # 절댓값 기준 정렬을 위해 (절댓값, 원래 값) 저장
        heapq.heappush(heap, (abs(x), x))
    else:
        # 힙이 비어있으면 0 출력, 아니면 최소값 출력
        if heap:
            output.append(str(heapq.heappop(heap)[1]))
        else:
            output.append("0")

# 한 번에 출력하여 I/O 최적화
sys.stdout.write("\n".join(output) + "\n")