import math
from io import StringIO
import sys

# 백준 5086
test_input = """8 16
32 4
17 5
0 0"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

text = sys.stdin.readlines()
for i in range(len(text)-1):
    A, B = map(int,text[i].split())
    if A > B and A % B == 0:
        print('multiple')
    elif B > A and B % A == 0:
        print('factor')
    else:
        print('neither')