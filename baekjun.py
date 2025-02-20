import sys
from io import StringIO

# 백준 9498
test_input ="""94"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

S = int(sys.stdin.readline())

if S >= 90:
    print("A")
elif S >= 80:
    print("B")
elif S >= 70:
    print("C")
elif S >= 60:
    print("D")
else:
    print("F")

