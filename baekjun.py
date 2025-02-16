import sys
import heapq
from collections import deque
from io import StringIO

# 테스트 입력을 문자열로 제공
test_input ="""3 5
2 1 6
3 2 3 5
1 1
3 2 1 4 5"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

# N, M = map(int,sys.stdin.readline().split())
# orders = []
#
# for _ in range(N):
#     data = list(map(int, sys.stdin.readline().split()))
#     orders.append(set(data[1:]))
#
# eat_count = [0] * N
# eaten_sushi = [set() for _ in range(N)]
#
# sushi_list = list(map(int, sys.stdin.readline().split()))
#
# for sushi in sushi_list:
#     for i in range(N):
#         if sushi in orders[i] and sushi not in eaten_sushi[i]:
#             eat_count[i] += 1
#             eaten_sushi[i].add(sushi)
#             break
# print(" ".join(map(str, eat_count)))

N, M = map(int, sys.stdin.readline().split())

orders = []
sushi_map = {}  # {초밥 종류: [먹을 수 있는 손님 리스트]}
for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    k, sushi_list = data[0], data[1:]
    orders.append(set(sushi_list))  # 각 손님의 초밥 목록을 set으로 저장
    for sushi in sushi_list:
        if sushi not in sushi_map:
            sushi_map[sushi] = []
        heapq.heappush(sushi_map[sushi], i)  # 손님 인덱스를 힙에 저장

# 결과 저장 배열
eat_count = [0] * N

# 초밥 제공 처리
sushi_list = list(map(int, sys.stdin.readline().split()))
for sushi in sushi_list:
    if sushi in sushi_map and sushi_map[sushi]:  # 해당 초밥을 먹을 수 있는 손님이 있으면
        customer = heapq.heappop(sushi_map[sushi])  # 가장 먼저 먹을 손님 찾기
        if sushi in orders[customer]:  # 확인 후 제거
            orders[customer].remove(sushi)
            eat_count[customer] += 1

# 결과 출력
print(" ".join(map(str, eat_count)))