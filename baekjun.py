from io import StringIO
import sys

# 백준 11718
test_input = """Hello
Baekjoon
Online Judge"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)
def strip(x):
    return x.strip()
S = list(map(strip, sys.stdin.readlines()))

for i in range(len(S)):
    print(S[i])