import sys
from io import StringIO

# 테스트 입력을 문자열로 제공
test_input ="""3
BANANA 2
PLUM 4
BANANA 3"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

# 코드 실행

text = sys.stdin.read().splitlines()
print(text)
fruits = {'BANANA': 0, 'PLUM': 0, 'LIME': 0, 'STRAWBERRY': 0}
for i in range(int(text[0])):
    fruit, count = text[i + 1].split(' ')
    fruit = str(fruit)
    count = int(count)
    if fruit in fruits:
        fruits[fruit] = fruits[fruit] + count
        print(fruits)
if 5 in fruits.values():
    print('YES')
else:
    print('NO')

# test_list = [[10]*5 for i in range(5)]
# print(test_list)
#
# for i in range(5):
#     a = list(input())
#     a_len = len(a)
#     for j in range(a_len):
#         test_list[i][j] = a[j]
#
# for i in range(10):
#     for j in range(5):
#         if test_list[j][i] == 10:
#             continue
#         else:
#             print(test_list[j][i],end='')

# 각 줄에서 조건 검사
# for t in text:
#     print(t[::1])
    # if not any(sub in t for sub in substrings):
    #     reversedText = ''.join(reversed(t))
    #     print(reversedText)


# import sys
# from io import StringIO
#
# # 테스트 입력을 문자열로 제공
# test_input = """Hello, World!
# This is a test."""
#
# # sys.stdin을 대체
# sys.stdin = StringIO(test_input)
#
# # 코드 실행
# input_text = sys.stdin.read()
# print("입력받은 내용:")
# print(input_text)
