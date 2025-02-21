import math
import heapq
import sys
from io import StringIO

# 백준 28278
test_input ="""9
4
1 3
1 5
3
2
5
2
2
5"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline().strip())
stack = []
for i in range(N):
    line = sys.stdin.readline().strip()

    if "1" in line:
        number = int(line.split(" ")[1])
        stack.append(number)
    elif line == "2":
        print(stack.pop() if len(stack) else -1)
    elif line == "3":
        print(len(stack))
    elif line == "4":
        print(0 if len(stack) else 1)
    else:
        print(stack[-1] if len(stack) else -1)