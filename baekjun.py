from io import StringIO
import sys

# 백준 10809
test_input = """baekjoon"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

S = sys.stdin.readline()

alpha = {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1,
         'f': -1, 'g': -1, 'h': -1, 'i': -1, 'j': -1,
         'k': -1, 'l': -1, 'm': -1, 'n': -1, 'o': -1,
         'p': -1, 'q': -1, 'r': -1, 's': -1, 't': -1,
         'u': -1, 'v': -1, 'w': -1, 'x': -1, 'y': -1, 'z': -1}
for i in range(len(S)):
    char = S[i]
    if alpha[char] == -1:
        alpha[char] = i

print(*alpha.values())