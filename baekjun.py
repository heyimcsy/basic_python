import sys
from io import StringIO

# 백준 2753
test_input ="""2401"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

Y = int(sys.stdin.readline())

if Y % 100 != 0 and Y % 4 == 0:
    print(1)
elif Y % 100 == 0 and Y % 400 == 0:
    print(1)
elif Y % 100 == 0 and Y % 400 != 0:
    print(0)
else:
    print(0)
