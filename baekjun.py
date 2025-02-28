import math
from io import StringIO
import sys
from collections import deque

# 백준 2164
test_input = """6"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())
cards = deque(range(1, N + 1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
print(cards[0])
