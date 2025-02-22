import math
import heapq
import sys
from io import StringIO

# 백준 10773
test_input ="""10
1
3
5
4
0
0
7
0
0
6"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])  # 첫 번째 줄에서 N 값 가져오기
stack = []

for i in range(1, N + 1):
    number = int(data[i])
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))
