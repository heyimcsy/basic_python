import sys
from io import StringIO

# 백준 11382
test_input ="""77 77 7777"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

A, B, C = map(int, sys.stdin.readline().split(' '))
print(A+B+C)
