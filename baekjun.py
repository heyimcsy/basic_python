import math
from io import StringIO
import sys

# 백준 2292
test_input = """54"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())

count = 1
cnt = 1
while N > count:
    count += 6 * cnt
    cnt += 1
print(cnt)