import math
from io import StringIO
import sys

# 백준 2738
test_input = """3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)


N, M = map(int, sys.stdin.readline().split())
text = sys.stdin.readlines()

for i in range(N):
    first_t = text[i].split()
    second_t = text[i + N].split()
    numbers = []
    for j in range(M):
        n_sum = int(first_t[j]) + int(second_t[j])
        numbers.append(str(n_sum))

    print(' '.join(numbers))