import sys
import heapq
from collections import deque
from io import StringIO

# 테스트 입력을 문자열로 제공
test_input ="""1 1 100000
1"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

text = sys.stdin.read().splitlines()

N, H, T = map(int, text[0].split())
people = map(int, text[1:1+N])
heap = [-n for n in list(people)]
count = 0
heapq.heapify(heap)
for i in range(T):
    if -heap[0] < H or -heap[0] == 1:
        break
    number = -heapq.heappop(heap)
    height = int(number / 2)
    heapq.heappush(heap, -height)
    count += 1
popNumber = -heap[0]
if popNumber >= H:
    print('NO')
    print(popNumber)
else:
    print('YES')
    print(count)



import heapq as hq
import sys
input = sys.stdin.readline

n, h, t = map(int,input().split())
g = []
cnt = 0
for _ in range(n):
    hq.heappush(g,-int(input()))

while t>0:
    x = hq.heappop(g)
    if -x< h:
        hq.heappush(g,-x)
        break
    if x<-1:
        hq.heappush(g,int(x/2))
    else:
        hq.heappush(g,-1)
    cnt +=1
    t -= 1

talleset = -hq.heappop(g)

if talleset<h:
    print("YES")
    print(cnt)
else:
    print("NO")
    print(talleset)

    import heapq
import sys

[n, H, T] = list(map(int, sys.stdin.readline().split()))
titans = []
count = 0

for i in range(n):
    titans.append(-int(sys.stdin.readline().strip()))


heapq.heapify(titans)

for i in range(T):
    tallest = -heapq.heappop(titans)

    if tallest < H:
        heapq.heappush(titans, -tallest)
        break
    if tallest <= 1:
        heapq.heappush(titans, -tallest)
        break

    heapq.heappush(titans, -(tallest // 2))
    count+=1

if -titans[0] < H:
    print("YES")
    print(count)
else:
    print("NO")
    print(-titans[0])