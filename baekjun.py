import sys
from io import StringIO

# 테스트 입력을 문자열로 제공
test_input ="""6
6
9
7
6
4
6"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

# # 코드 실행
# text = sys.stdin.read().splitlines()
# print(text)
#
# tall = 0
# count = 0
# for number in text[:0:-1]:
#     number = int(number)
#     if number > tall:
#         tall = number
#         count += 1
# print(count)

text = sys.stdin.read().splitlines()

# heights = list(map(int, text[1:]))
# stack = [heights[-1]]
# # 뒤에서부터 탐색
# for height in reversed(heights):
#     if stack[-1] < height:
#         print('wile',stack)
#         stack.append(height)
# print(len(stack))

heights = list(map(int, text[1:]))
stack = []
count = 0

for height in reversed(heights):
    if not stack or stack[-1] < height:
        stack.append(height)
        count += 1

print(count)