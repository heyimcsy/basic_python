import math
from io import StringIO
import sys
from itertools import combinations

# 백준 2798
test_input = """5 21
5 6 7 8 9"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)
N, M = map(int, sys.stdin.readline().split())
cards = list(sorted(map(int, sys.stdin.readline().split())))
print(cards)
max_sum = 0

for combo in combinations(cards, 3):
    current = sum(combo)
    if current <= M:
        max_sum = max(max_sum, current)
print(max_sum)
