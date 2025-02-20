import sys
from io import StringIO

# 백준 2884
test_input ="""23 40"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

H, M = map(int, sys.stdin.readline().split(' '))

if M - 45 >= 0:
    M = M - 45
else:
    if H == 0:
        H = 23
    else:
        H = H - 1
    M = 60 + (M - 45)
time = [H, M]
print(" ".join(map(str, time)))
