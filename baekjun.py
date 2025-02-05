import sys
from collections import deque
from io import StringIO

# 테스트 입력을 문자열로 제공
test_input ="""15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

text = sys.stdin.read().splitlines()
queue = deque()
N = int(text[0])
lists = text[1:]

for command in lists:
    split_command = command.split()
    if split_command[0] == 'push':
        queue.append(int(split_command[1]))
    elif split_command[0] == 'pop':
        print(queue.popleft() if queue else -1)
    elif split_command[0] == 'size':
        print(len(queue))
    elif split_command[0] == 'empty':
        print(1 if not queue else 0)
    elif split_command[0] == 'front':
        print(queue[0] if queue else -1)
    elif split_command[0] == 'back':
        print(queue[-1] if queue else -1)
