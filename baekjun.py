import math
from io import StringIO
import sys

# 백준 2745
test_input = """ZZZZZ 36"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N, B = sys.stdin.readline().split()

print(int(N, int(B)))