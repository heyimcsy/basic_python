import math
from io import StringIO
import sys

# 백준 2581
test_input = """60
100"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
numbers = []
for number in range(N, M + 1):
    if number < 2:
        continue
    is_true = True
    for n in range(2, number):
        if number % n == 0:
            is_true = False
            break
    if is_true:
        numbers.append(number)

if len(numbers) == 0:
    print(-1)
else:
    print(sum(numbers))
    print(numbers[0])