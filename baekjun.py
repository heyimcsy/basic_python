from io import StringIO
import sys

# 백준 1546
test_input = """3
10 20 30"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)
N = int(sys.stdin.readline())

tests = list(map(int, sys.stdin.readline().split()))
high_score = max(tests)

def res(x):
    return x / high_score *100

new_score = sum(list(map(res, tests))) / N
print(new_score)