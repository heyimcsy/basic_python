from io import StringIO
import sys

# 백준 9012
test_input = """6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()("""

# sys.stdin을 대체
sys.stdin = StringIO(test_input)

N = int(sys.stdin.readline())

for _ in range(N):
    stack = []
    text = sys.stdin.readline().strip()
    is_valid = True
    for c in text:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                is_valid = False
                break
            stack.pop()

    # 남아 있는 '('가 있으면 잘못된 괄호 문자열
    if is_valid and not stack:
        print("YES")
    else:
        print("NO")
