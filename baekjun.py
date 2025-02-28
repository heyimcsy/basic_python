import math
from io import StringIO
import sys
import heapq

# 백준 1436 브루트 포스 알고리즘
test_input = """500"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)
N = int(sys.stdin.readline().strip())
count = 0
number = 666

while True:
    if '666' in str(number):
        count += 1
    if count == N:
        break
    number += 1

print(number)