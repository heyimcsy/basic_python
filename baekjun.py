import math
from io import StringIO
import sys

# 백준 1193
test_input = """2"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())


line = 1
sum_line= 0
while N > line:
    N -= line
    sum_line += line
    line += 1

if line % 2 == 0:
    a = N
    b = line + 1 - N
else:
    a = line + 1 - N
    b = N

print(f'{a} / {b}')