import math
from io import StringIO
import sys

# 백준 10988
test_input = """levvel"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

word = sys.stdin.readline().strip()

check = True
half = math.floor(len(word) / 2)
for i in range(half):
    if word[i] != word[- (i + 1)]:
        check = False
        break
print(1 if check else 0)
