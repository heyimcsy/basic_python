import math
from io import StringIO
import sys
from collections import deque

# 백준 2776
test_input = """1
5
4 1 5 2 3
5
1 3 7 9 5"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    _ = int(sys.stdin.readline())
    watched = sys.stdin.readline().strip().split()
    watched_dic = {i: 1 for i in watched}
    M = int(sys.stdin.readline().strip())
    memory = sys.stdin.readline().strip().split()
    for m in memory:
        if m in watched_dic:
            print(watched_dic[m])
        else:
            print(0)
