import sys
from io import StringIO

# 테스트 입력을 문자열로 제공
test_input ="""5
5
4
3
2
1"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

# 코드 실행
text = sys.stdin.read().splitlines()
print(text)

tall = 0
count = 0
for number in text[:0:-1]:
    number = int(number)
    if number > tall:
        tall = number
        count += 1
print(count)
