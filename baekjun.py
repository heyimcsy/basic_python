import math
from io import StringIO
import sys

# 백준 2563
test_input = """3
3 7
15 7
5 2"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())
background = {}
for _ in range(N):
    width, height = map(int,sys.stdin.readline().split())

    for w in range(width, width+10):
        for h in range(height, height+10):
            background[w,h] = 1
print(len(background.values()))
