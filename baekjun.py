from io import StringIO
import sys

# 백준 11654
test_input = """A"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = sys.stdin.readline()

print(ord(N))