import sys
from io import StringIO

# 테스트 입력을 문자열로 제공
test_input ="""0 1 0 1
1 1 1 0
0 0 1 1"""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

# 코드 실행
text = sys.stdin.read().splitlines()
print(text)

for n in text:
    print(n.count('0'))
    if n.count('0') == 1:
        print('A')
    elif n.count('0') == 2:
        print('B')
    elif n.count('0') == 3:
        print('C')
    elif n.count('0') == 4:
        print('D')
    else:
        print('E')
