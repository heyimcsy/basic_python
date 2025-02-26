import math
from io import StringIO
import sys

# 백준 1316
test_input = """5
ab
aa
aca
ba
bb"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())
check = 0
for _ in range(N):
    word = sys.stdin.readline().strip()
    alphabet_dict = {chr(i): 0 for i in range(97, 123)}
    group_word = True
    for i in range(len(word)):
        if alphabet_dict[word[i]] == 0:
            alphabet_dict[word[i]] = 1
        elif alphabet_dict[word[i]] == 1 and word[i-1] != word[i]:
            group_word = False

    if group_word:
        check += 1
print(check)

