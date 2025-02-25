import math
from io import StringIO
import sys
import re

# 백준 2941
test_input = """dz=ak"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

word = sys.stdin.readline().strip()

qro = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

first = ['c', 'd', 'l', 'n', 's', 'z']
w = 0
sum = 0
while w < len(word):
       if word[w : w + 3] == 'dz=' :
              w += 3
       elif word[w : w + 2] in qro:
              w+= 2
       else:
              w+=1
       sum += 1

print(sum)