import math
from io import StringIO
import sys

# 백준 2566
test_input = """3 23 85 34 17 74 25 52 65
10 7 39 42 88 52 14 72 63
87 42 18 78 53 45 18 84 53
34 28 64 85 12 16 75 36 55
21 77 45 35 28 75 90 76 1
25 87 65 15 28 11 37 28 74
65 27 75 41 7 89 78 64 39
47 47 70 45 23 65 3 41 44
87 13 82 38 31 12 29 29 80"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

matrix = []
for _ in range(9):
    line = list(map(int, sys.stdin.readline().split()))
    matrix.append(line)

number = max(map(max ,matrix))

print(number)
for i in range(9):
    for j in range(9):
        if matrix[i][j] == number:
            index = [str(i + 1), str(j + 1)]
            print(' '.join(index))
