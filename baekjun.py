import math
from io import StringIO
import sys
from collections import deque

# 백준 12789
test_input = """5
3 4 1 2 5"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())
stack = deque()
deque_list = deque(list(map(int, sys.stdin.readline().split())))
count = 1

while deque_list or stack:
    if deque_list and deque_list[0] == count:
        deque_list.popleft()
        count += 1
    elif stack and stack[0] == count:
        stack.popleft()
        count += 1
    elif deque_list:
        stack.appendleft(deque_list.popleft())
    else:
        print('Sad')
        break
else:
    print('Nice')
