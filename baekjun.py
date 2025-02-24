from io import StringIO
import sys

# 백준 2743
test_input = """pulljima"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

S = len(sys.stdin.readline().strip())

print(S)
