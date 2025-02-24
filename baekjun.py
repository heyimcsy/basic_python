from io import StringIO
import sys

# 백준 1152
test_input = """The Curious Case of Benjamin Button"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

S = sys.stdin.readline().split()

print(len(S))