from io import StringIO
import sys

# 백준 3003
test_input = """0 1 2 2 2 7"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

chess = {0: 1, 1: 1, 2: 2, 3: 2, 4: 2, 5: 8}
new_chess = []
N = sys.stdin.readline().split()

for i in range(6):
    c = str(chess[i] - int(N[i]))
    new_chess.append(c)

print(' '.join(new_chess))