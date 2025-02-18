import sys
import heapq
from collections import deque
from io import StringIO

# 테스트 입력을 문자열로 제공
test_input ="""8
sbrus.txt
spc.spc
acm.icpc
korea.icpc
sample.txt
hello.world
sogang.spc
example.txt"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = list(map(int,sys.stdin.readline().split()))[0]
files = {}
for _ in range(N):
    text = sys.stdin.readline().split()[0].split('.')[1]
    if text in files:
        files[text] += 1
    else:
        files[text] = 1

for ext, count in sorted(files.items()):
    print(ext, count)