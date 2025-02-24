from io import StringIO
import sys

# 백준 9086
test_input = """3
ACDKJFOWIEGHE
O
AB"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())

for _ in range(N):
    text = sys.stdin.readline().strip()
    f = [text[0]]
    f.append(text[-1])
    print("".join(f))