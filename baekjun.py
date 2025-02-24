from io import StringIO
import sys

# 백준 27866
test_input = """Sprout
3"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

S = sys.stdin.readline()
i = int(sys.stdin.readline())

print(S[i - 1])
