import sys
from io import StringIO

# 백준 1009
test_input ="""5
1 6
3 7
6 2
7 100
9 635"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())

for i in range(N):
    F, S = list(map(int,sys.stdin.readline().split(" ")))
    if F % 10 == 0:
        print(10)
    else:
        last_digit = pow(F, S, 10)
        print(last_digit)