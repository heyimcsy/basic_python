import math
from io import StringIO
import sys

# 백준 11005
test_input = """60466175 36"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N, B = map(int, sys.stdin.readline().split())

def solution(n, b):
    rev_base = ''
    arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while n:
        rev_base += str(arr[n % b])
        n //= b
    return rev_base[::-1]
print(solution(N, B))