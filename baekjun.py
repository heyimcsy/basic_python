import math
from io import StringIO
import sys

# 백준 2720
test_input = """3
124
25
194"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())

for _ in range(N):
    changes = {'Q': 0,'D': 0, 'N': 0, 'P':0 }
    change = int(sys.stdin.readline().strip())
    if change > 24:
        count = math.floor(change / 25)
        changes['Q'] = count
        change -= 25 * count
    if change > 9:
        count = math.floor(change / 10)
        changes['D'] = count
        change -= 10 * count
    if change > 4:
        count = math.floor(change / 5)
        changes['N'] = count
        change -= 5 * count
    if change < 5:
        count = math.floor(change / 1)
        changes['P'] = count

    print(*changes.values())