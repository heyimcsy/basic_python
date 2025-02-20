import sys
from io import StringIO

# 테스트 입력을 문자열로 제공
test_input ="""3 4
JLA
CRUO
3"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

_ = sys.stdin.readline().strip()
first = list(reversed(sys.stdin.readline().strip()))  # 첫 번째 그룹은 뒤집기
second = list(sys.stdin.readline().strip())  # 두 번째 그룹은 그대로
N = int(sys.stdin.readline().strip())

direction = {ant: 0 for ant in first}  # 첫 번째 그룹: 오른쪽(0)
direction.update({ant: 1 for ant in second})  # 두 번째 그룹: 왼쪽(1)

text = first + second

for _ in range(N):
    i = 0
    while i < len(text) - 1:
        if direction[text[i]] == -0 and direction[text[i + 1]] == 1:
            text[i], text[i + 1] = text[i+1], text[i]
            i += 1
        i += 1
print("".join(text))