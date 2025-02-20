import sys
from io import StringIO

# 백준 2739
test_input ="""2"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())
for i in range(9):
    result = N * (i + 1)
    print(f'{N} * {i + 1} = {result}')