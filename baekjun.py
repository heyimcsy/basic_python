from io import StringIO

import sys
import heapq

# 백준 3052
test_input = """39
40
41
42
43
44
82
83
84
85"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)
# N, M = map(int, sys.stdin.readline().split())

def sep(x):
    return int(x) % 42

number = list(map(sep, sys.stdin.readlines()))

print(len(set(number)))